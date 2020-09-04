class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)
        

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding hte node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if new_val > current.value:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right

        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        # Case 1: We have just inserted  the root node.
        # if we're enforcing that the root must be black, we change its color. We are not enforcing this, so we are all done!
        if node.parent == None:
            return

        # Case 2: We inserted under a black parent node.
        # Thinkig through this, we can observe the following: We inserted a red node beneath a black node.
        # The new children (NULL nodes) are black by definition, and our red node replaced a black NULL node.
        # So thte number of black nodes for any paths from parents is unchanged. Nothing to do in this case, either.
        if node.parent.color == 'black':
            return

        # from here, we know parent's color is red.
        # Case 3: The parent and its sibling of the newly inserted node are both red
        # We're done with free cases. In this specific case, we can flip the color of the parent and its sibling.
        # We know they're both red in this case, which means the grandparent is black.
        # It wil also need to flip. At that point we will have a freshly painted red node at the grandparent.
        # At that point, we need to do the same evaluation. 
        # If the grandparent turns red, and its sibling is also red, that's case 3 again.
        # Guess what that means! Time for more recursion.
        # We will define the grandparent and pibling (a parent's sibling) methods later, for now let's focus on the core logic.
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        gp = grandparent(node)
        # small change, if there is no grandparent, case 4 and 5 won't apply
        if gp == None:
            return

        # Case 4: The newly inserted node has a red parent, but that parent has a black sibling
        # These last cases get more interesting. The criteria above actually govern case 4 and 5.
        # What separates them is if the newly inserted node is on the inside or the outside of the sub tree.
        # We define inside and outside like this:
        # inside : 
        # EITHER :  the new node is a left child of its parent, but its parent is a right child, or
        #           the new node is a right child of its parent, but its parent is a left child
        # outside:
        #           the opposite of inside, the new node and its parent are on the same side of the grandparent
        # Case 4 is to handle the inside scenario. In this case, we need to rotate.
        # As we will see, this will not finish balancing the tree, but will now qualify for case 5.
        # We rotate against the inside-ness of the new node. If the new node qualifies for case 4, it needs to move into its parent's spot.
        # if it's on the right of parent, that's a rotate left. If it's on the left of the parent, that's a rotate right.
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5: Now that case 4 is resolved or if we didn't qualify for case 4 and have an outside sub-tree already, 
        # we need to rotate again. If our new node is a left child of a left child, we rotate right.
        # If our new node is a right of a right, we rotate left. This is done on the gradparent node.
        # But after this rotation, our colors will be off.
        # remember that for cases 3, 4, and 5, the parent of the new node is red.
        # But we will have rotated a red node with ared child up, which violates our rule of all red nodes having two black children.
        # So after rotating, we switch the colors of the original parent and grandparent nodes.
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    # To implement rotate_left and rotate_right, think about what we want to accomplish.
    # We want to take one of the node's children and have it take the place of its parent.
    # The given node will move down to a child of the newly parental node.
    def rotate_left(self, node):
        # save off the parent of the sub-tree we're rotating.
        p = node.parent

        node_moving_up = node.right
        # after 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if  p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p



    def search(self, find_val):
        pass

# Rotations
'''
At this point, we are only making a BST, with extra attributes.
To make this a red-black tree, we need to add the extra sauce that makes red-black trees awesome.
We will sketch out some more code for rebalancing the tree based on the case, and fill them in one at a time.

First, we need to change our insert_helper to return the node that was inserted so we can interrogate (정보를 얻다) it when rebalancing.
'''

# Testing
# First, we'll need a way to visualize the tree. The below will nest, but remember the first child is always the left child.
def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

# For cases 1 and 2, we can insert the first few nodes and see the tree behaves the same as a BST.
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)

# Inserting 13 should flip 6 and 19 to black, as it hits our Case 3 logic.
tree.insert(13)
print_tree(tree.root)

# Observe that 13 was inserted as red, and then because of Case 3, 6 and 19 flipped to black. 
# # 9 was also assigned red, but that was not a net change. 
# Because we're not enforcing the optional "root is always black rule", this is acceptable.
# Now let's cause some rotations. When we insert 16, it goes under 13, but 13 does not have a red sibling. 
# 16 rotates into 13's spot, because it's currently an inside sub-tree. 
# Then 16 rotates into 19's spot. After these rotations, the ordering of the BST has been preserved and our tree is balanced.
tree.insert(16)
print_tree(tree.root)



