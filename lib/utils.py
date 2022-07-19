from Block import *
from HashedNode import *

def create_tree(leaves,og_tree=[]) -> HashedNode:
    """
    Builds a Merkle tree using a list of strings to form the values of the HashedNodes.

    Returns the root of the Tree
    """

    og_tree = []
    for i in leaves:
        og_tree.append(HashedNode(i))

    while len(og_tree)!=1:
        aux = []

        for i in range(0,len(og_tree),2):
            left_node = og_tree[i]

            if i+1 < len(og_tree):
                right_node = og_tree[i+1]
            else:
                aux.append(og_tree[i])
                break
           
            concatenatedHash = left_node.hashed_value + right_node.hashed_value
            parent = HashedNode(concatenatedHash)
            parent.left = left_node
            parent.right = right_node
            aux.append(parent)

        og_tree = aux 

    return og_tree[0]

def add_node(root_node, input_value) -> HashedNode:
    """
    Adds a new node to a merkle tree.

    Returns the root node of the merkle tree
    """

    return create_tree(input_value, root_node)

