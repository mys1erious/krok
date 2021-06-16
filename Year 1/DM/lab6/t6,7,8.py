class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        #self.parent = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if node.val > root.val:
            if root.right is None:
                root.right = node
                root.right.parent = root
            else:
                insert(root.right, node)
        elif node.val < root.val:
            if root.left is None:
                root.left = node
                root.left.parent = root
            else:
                insert(root.left, node)


def in_order(root, array=[]):
    if root:
        in_order(root.left)
        array.append(root.val)
        in_order(root.right)
    return array


arr = ['Google', 'Amazon', 'Apple', 'IBM', 'SAP', 'Oracle', 'Facebook', 'Nvidia', 'Baidu',
       'Alibaba', 'HP', 'Accenture', 'Microsoft']


r = Node(arr[0])
for i in arr:
    insert(r, Node(i))


insert(r, Node('Infosys'))


sortedArr = in_order(r)
print('Sorted array:\n', sortedArr)
