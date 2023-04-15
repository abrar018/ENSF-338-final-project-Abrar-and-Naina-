from trees.AVL import AVL
from nodes.Tnode import Tnode
from trees.BST import BST



#BST Tests!!!!!

# Create BST object and test its functionalities
bst = BST()

# Test default constructor
bst1 = bst.default_constructor()

# Test overload constructor 1
bst2 = bst.overload_constructor_val(10)

# Test overload constructor 2
root = Tnode(20)
bst3 = bst.overload_constructor_obj(root)

# Test setter and getter for root
root1 = Tnode(30)
bst.set_root(root1)
print(bst.get_root().data)

# Test Insert function
bst.insert(40)
bst.insert(50)

# Test Delete function
bst.Delete(10)

# Test Search function
node = bst.Search(40)
if node is not None:
    print("Found node with value", node.data)
else:
    print("Node not found")

# Test printing elements in ascending order
print("Printing elements in ascending order for BST:")
bst.printInOrder()

# Test breadth first traversal function
print("\nPrinting elements in breadth-first order for BST:")
bst.printBF()









# AVL Tests!!!!!!

# Create an empty AVL tree
avl = AVL()

# Insert some values into the AVL tree
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)



# Create an AVL tree from an existing BST
bst = AVL()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)


# Test setter and getter for root
root1 = Tnode(30)
bst1.set_root(root1)
print(bst1.get_root().data)




# Search for a value in the AVL tree
print("Searching for 30:", avl.search(30))


# Print the AVL tree in order
print("\nAVL tree from BST in order:")
avl.printInOrder()

# Print the AVL tree in breadth-first order
print("\nAVL tree from BST in breadth-first order:")
avl.printBF()



