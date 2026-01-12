# Skeleton file for HW5 - spring  2025 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw5_ID.py).
import math
from platform import node
import random


#####################################
# Linked List   (code from lecture) #
#####################################

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return str(self.value)


class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.size = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += p.__repr__() + ", "
            p = p.next
        return "[" + out[:-2] + "]"  # discard the extra ", " at the end

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.size += 1


    def __len__(self):
        ''' called when using Python's len() '''
        return self.size

    def index(self, val):
        ''' find index of (first) node with value val in list
            return None of not found '''
        p = self.head
        i = 0  # we want to return the location
        while p != None:
            if p.value == val:
                return i
            else:
                p = p.next
                i += 1
        return None  # in case val not found

    def __getitem__(self, i):
        ''' called when reading L[i]
            return value of node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        return p.value

    def __setitem__(self, i, val):
        ''' called when using L[i]=val (indexing for writing)
            assigns val to node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        p.value = val
        return None

    def insert(self, i, val):
        ''' add new node with value val before index 0<=i<=len '''
        assert 0 <= i <= len(self)
        if i == 0:
            self.add_at_start(val)  # makes changes to self.head
        else:
            p = self.head
            for j in range(0, i - 1):  # get to position i-1
                p = p.next
            # now add new element
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.size += 1

    def append(self, val):
        self.insert(self.size, val)

    def pop(self, i):
        ''' delete element at index 0<=i<len '''
        assert 0 <= i < len(self)
        if i == 0:
            self.head = self.head.next  # bypass first element
        else:  # i >= 1
            p = self.head
            for j in range(0, i - 1):
                p = p.next

            # now p is the element BEFORE index i
            p.next = p.next.next  # bypass element at index i

        self.size -= 1


##############################################
# Binary Search Tree     (code from lecture) #
##############################################

class TreeNode():
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class BinarySearchTree():
    def __init__(self, root=None, size=0):
        self.root = root
        self.size = size


    def __repr__(self):  # you don't need to understand the implementation of this method
        def printree(root):
            if not root:
                return ["#"]

            root_key = str(root.key)
            left, right = printree(root.left), printree(root.right)

            lwid = len(left[-1])
            rwid = len(right[-1])
            rootwid = len(root_key)

            result = [(lwid + 1) * " " + root_key + (rwid + 1) * " "]

            ls = len(left[0].rstrip())
            rs = len(right[0]) - len(right[0].lstrip())
            result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

            for i in range(max(len(left), len(right))):
                row = ""
                if i < len(left):
                    row += left[i]
                else:
                    row += lwid * " "
                    
                row += (rootwid + 2) * " "

                if i < len(right):
                    row += right[i]
                else:
                    row += rwid * " "

                result.append(row)

            return result

        return '\n'.join(printree(self.root))


    def lookup(self, key):
        ''' return value of node with key if exists, else None '''
        node = self.root
        while node != None:
            if key == node.key:
                return node.val  # found!
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None


    def insert(self, key, val):
        ''' insert node with key,val into tree.
            if key already there, just update its value '''

        parent = None  # this will be the parent of the new node
        node = self.root

        while node != None:  # keep descending the tree
            if key == node.key:
                node.val = val  # update the val for this key
                return

            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if parent == None:  # was empty tree, need to update root
            self.root = TreeNode(key, val)
        elif key < parent.key:
            parent.left = TreeNode(key, val)  # "hang" new node as left child
        else:
            parent.right = TreeNode(key, val)  # "hang"    ...     right child

        self.size += 1
        return None


    def minimum(self):
        ''' return value of node with minimal key '''

        if self.root == None:
            return None  # empty tree has no minimum
        node = self.root
        while node.left != None:
            node = node.left
        return node.val


    def depth(self):
        ''' return depth of tree, uses recursion '''
        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)

##############
# QUESTION 1 #
##############
class LLLNode:
    def __init__(self, val):
        self.next_list = []
        self.val = val

    def __repr__(self):
        st = "Value: " + str(self.val) + "\n"
        st += "Neighbors:" + "\n"
        for p in self.next_list:
            st += " - Node with value: " + str(p.val) + "\n"
        return st[:-1]


class LogarithmicLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        node = LLLNode(val)
        if len(self) == 0:
            self.head = node
            self.len = 1
            return None
        
        temp = self.head
        node.next_list.append(temp)
        for i in range(0, int(math.log2(self.len)) + 1):
            if i < len(temp.next_list):
                node.next_list.append(temp.next_list[i])
                temp = temp.next_list[i]
            else:
                break
        self.head = node
        self.len += 1
        return None

    def __getitem__(self, i):
        if i == 0:
            return self.head.val
        log_idx = i//2
        temp = self.head.next_list[log_idx]
        return temp.val if i % 2 == 0 else temp.next_list[0].val

    # Optional - improve this code!
    def __contains__(self, val):
        p = self.head
        k = 1
        while k != 0:
            if p.val == val:
                return True
            k = 0
            m = len(p.next_list)
            while k < m and p.next_list[k].val <= val:
                k += 1
            if k > 0:
                p = p.next_list[k - 1]
        return False

##############
# QUESTION 2 #
##############

def gen1(): 
    s = 0
    while True:
        for x in range(-s, s + 1):
            y_abs = s - abs(x)
            y_values = {y_abs, -y_abs}
            for y in y_values:
                yield (x, y)
        s += 1

def gen2(g):
    sum = 0
    while True:
        x = next(g)
        sum += x
        yield sum

def gen3(g):
    pass  # replace this with your code (or don't, if there does not exist such generator with finite delay)

def gen4(g):
    yield True # first value is always True
    prev = next(g)
    x = next(g)
    yield True # second value is always True and determines the direction

    monotonous = True
    if x >= prev:
        while True:
            try:
                prev = x
                x = next(g)
                if x < prev:
                    monotonous = False
                yield monotonous
            except StopIteration:
                break
            
    else:
        while True:
            try:
                prev = x
                x = next(g)
                if x > prev:
                    monotonous = False
                yield monotonous
            except StopIteration:
                break

def gen5(g1, g2):
    pass  # replace this with your code (or don't, if there does not exist such generator with finite delay)

def gen6(g1, g2):
    pass  # replace this with your code (or don't, if there does not exist such generator with finite delay)

def gen7():
    i = 1
    while True:
        def gen_inner():
            yield 0
            j = i
            while True:
                if j%i == 0:
                    yield j
                j += i         
        yield gen_inner
        i += 1

##############
# QUESTION 3 #
##############

# TODO: analyze time complexity of lowest_common_ancestor
def lowest_common_ancestor(t, n1, n2):
    def lca_helper(node, n1, n2):
        if node is None:
            return None
        
        if node.key == n1 or node.key == n2:
            return node
        if n2 < node.key:
            return lca_helper(node.left, n1, n2)
        if n1 > node.key:
            return lca_helper(node.right, n1, n2)
        
        left_lca = lca_helper(node.left, n1, n2)
        right_lca = lca_helper(node.right, n1, n2)
        if left_lca and right_lca:
            return node
        return left_lca if left_lca is not None else right_lca
    return lca_helper(t.root, n1, n2)

def build_balanced(n):
    tree = BinarySearchTree()
    def bb_helper(sub_tree):
        if len(sub_tree) == 0:
            return
        if len(sub_tree) == 1:
            tree.insert(sub_tree[0], sub_tree[0])
        else:
            mid = len(sub_tree) // 2
            tree.insert(sub_tree[mid], sub_tree[mid])
            bb_helper(sub_tree[:mid])
            bb_helper(sub_tree[mid + 1:])
    bb_helper([i+1 for i in range(2**n - 1)])
    return tree

def subtree_sum(t, k):
    def sum(node):
        if node is None:
            return 0
        return node.key + sum(node.left) + sum(node.right)

    def helper(node, k, curr_depth=1):
        if node is None:
            return 0
        if node.key == k:
            return sum(node)
        elif node.key < k:
            return helper(node.right, k)
        else:
            return helper(node.left, k)
    
    return helper(t.root, k)

tree = build_balanced(4)
print(tree)
print("tree.size: ", tree.size)
print(subtree_sum(tree, 6))

##############
# QUESTION 4 #
##############
def prefix_suffix_overlap(lst, k):
    pass  # replace this with your code


class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        pass  # replace this with your code


def prefix_suffix_overlap_hash1(lst, k):
    pass  # replace this with your code

def almost_prefix_suffix_overlap_hash1(lst, k):
    pass  # replace this with your code


##############
# QUESTION 5 #
##############


class Rational1:
    """ represent a rational number using nominator and denominator """
    
    def __init__(self, n, d):
        assert isinstance(n,int) and isinstance(d,int)
        g = math.gcd(n,d)
        self.n = n//g # nominator
        self.d = d//g # denominator

    def __repr__(self):
        if self.d == 1:
            return "<Rational " + str(self.n) + ">"
        else:
            return "<Rational " + str(self.n) + "/" + str(self.d) + ">"

    def is_int(self):
        return self.d == 1

    def floor(self):
        return self.n // self.d
    
          
    def __eq__(self,other):
        if isinstance(other, Rational1):
            return self.n == other.n and self.d == other.d
        elif isinstance(other, int):
            return self.n == other and self.d == 1
        else:
            return False
    
    def __add__(self, other):
        # Add your code here #
        pass

    def __mul__(self, other):
        # Add your code here #
        pass    

    def divides(self, other):
        # Add your code here #
        pass

    def __lt__(self, other):
        # Add your code here #
        pass
 

class Rational2:
    """ represent a rational number using quotient, remainder and denominator """

    def __init__(self, n, d):
        assert isinstance(n,int) and isinstance(d,int)
        g = math.gcd(n,d)
        n,d = n//g, d//g
        self.q = n//d # quotient
        self.r = n%d  # remainder
        self.d = d    # denominator

    def __repr__(self):
        if self.r == 0:
            return "<Rational " + str(self.q) + ">"
        else:
            n = self.q * self.d + self.r
            return "<Rational " + str(n) + "/" + str(self.d) + ">"

    def is_int(self):
        return self.r == 0

    def floor(self):
        return self.q
  
    def __eq__(self,other):
        if isinstance(other, Rational2):
            return self.q == other.q and \
               self.r == other.r and \
               self.d == other.d
        elif isinstance(other, int):
            return self.q == other and self.r == 0 
        else:
            return False
        
    def __add__(self, other):
        # Add your code here #
        pass

    def __mul__(self, other):
        # Add your code here #
        pass

    def divides(self, other):
        # Add your code here #
        pass

    def __lt__(self, other):
        # Add your code here #
        pass


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash( (self.x, self.y) )

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        pass


##############
# TESTS      #
##############
def test():
    # Q1
    lst = LogarithmicLinkedList()
    lst.add_at_start(1)
    lst.add_at_start("hello")
    lst.add_at_start(True)
    if lst[0] != True or len(lst) != 3:
        print("1 - error in LogarithmicLinkedList")

    # Q4
    t = build_balanced(4)

    if t.size != 15 or t.depth() != 3:
        print("4 - error in build_balanced")

    if lowest_common_ancestor(t, 4, 7).key != 4 or lowest_common_ancestor(t, 2, 12).key != 8:
        print("4 - error in lowest_common_ancestor or build_balanced")

    if subtree_sum(t, 6) != 18 or subtree_sum(t, 12) != 84:
        print("4 - error in subtree_sum")
    # Q4
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("5 - error in prefix_suffix_overlap")

    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)
    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("5 - error in Dict.find")

    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("5 - error in prefix_suffix_overlap_hash1")


# test()