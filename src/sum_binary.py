#!/usr/bin/env python3

class newNode:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def addTree(root):
    if (root == None):
        return 0
    return (root.key + addTree(root.left) + addTree(root.right))

def addTreeRight(root):
    if (root == None):
        return 0
    return (addTree(root.right))

def addTreeLeft(root):
    if (root == None):
        return 0
    return (addTree(root.left))

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.right.right = newNode(8)
    
    sum_all = addTree(root)
    sum_right = addTreeRight(root) 
    sum_left = addTreeLeft(root)
    
    print(f'Suma of all nodes is: {sum_all}')
    print(f'Suma of all right nodes is: {sum_right}')
    print(f'Suma of all left nodes is: {sum_left}')
