#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану..
#  Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся  элементы, которые не меньше медианы, 
# в другой – не больше медианы. 
# Задачу можно решить без сортировки исходного массива. 
# Но если это слишком сложно, то используйте метод сортировки, который не
#  рассматривался на уроках

import random as rnd
class Node(object):

    def __init__(self, lst):
        self.lst = lst
        self.left = None
        self.right = None

    def compare(self, new_lst):
        if new_lst >= self.lst:
            if self.right:
                self.right.compare(new_lst)
            else:
                self.right = Node(new_lst)
        if new_lst < self.lst:
            if self.left:
                self.left.compare(new_lst)
            else:
                self.left = Node(new_lst)

    def nodesort(self):
        if self.left:
            self.left = self.left.nodesort()
        else:
            self.left = []
        if self.right:
            self.right = self.right.nodesort()
        else:
            self.right = []
        return self.left + [self.lst] + self.right

class SortedTree(object):
    def __init__(self):
        self.root = None
    def push(self, lst):
        if self.root:
            self.root.compare(lst)
        else:
            self.root = Node(lst)
    def merge(self):
        return self.root.nodesort()

def median(lst):
    sorted_tree = SortedTree()
    num_lst = len(lst)
    for elem in lst:
        sorted_tree.push(elem)
    middle = (num_lst //2) 
    treeresult = sorted_tree.merge()
    return treeresult[middle]

def findlefpart(lst, median):
    leftpart = []
    for i in lst:
        if i < median:
            leftpart.append(i)
    return leftpart

def findrightpart(lst, median):
    rightpart = []
    for i in lst:
        if i > median:
            rightpart.append(i)
    return rightpart





arraysize  = int(input("Введите размер: ")) 
arraysize = 2*arraysize+1
array = [rnd.randint(0, 101) for _ in range (arraysize)]
print (array)

m = median(array)
lp= findlefpart(array, m)
rp = findrightpart(array, m)


print (f"leftpart: {lp} median: {m} rightpart {rp}")