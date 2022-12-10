import random


class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data,end="-->")
            temp = temp.next

    def search(self,data):

        temp = self.head
        index = 0

        if temp==None:
            return "Not Found"
       
        while(temp.data != data):
            index = index+1
            temp = temp.next
            if temp==None:
                return "Not Found"
        return index

    def insert_at_first(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.head.data = data
    
    def insert_at_last(self,data):
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.tail.data = data

    def insert_between_nodes(self,data,index):
        node_pre = self.head
        count = 0
        while(count!=index-1):
            count = count+1
            node_pre = node_pre.next
        node_aft = node_pre.next
        node = Node(data)
        node.next = node_aft
        node_pre.next = node
        node_pre.next.data = data

    def remove_at_first(self):
        temp = self.head
        if temp==None:
            return "Not Found"
        self.head = self.head.next
        del temp
    
    def remove_at_last(self):
        if self.head==None:
            return "Not Found"
        node_pre = self.head
        temp = self.head.next
        while(temp.next!=None):
            temp = temp.next
            node_pre = node_pre.next
        node_pre.next = None
        del temp
        self.tail = node_pre
    
    def remove_between_nodes(self,index):
        if self.head==None:
            return "Not found"
        node_pre = self.head
        count = 0
        while(count!=index-1):
            count = count+1
            node_pre = node_pre.next
        node_del = node_pre.next
        node_aft = node_del.next
        node_pre.next = node_aft
        del node_del

    def adding_items_in_llist(self,items):
        if self.head == None:
            self.head = Node(items)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = Node(items)
            self.tail = temp.next



# llist = LinkedList()
# llist.head = Node(100)
# second_block = Node(2)
# third_block = Node(35)
# llist.tail = Node(47)

# llist.head.next = second_block
# second_block.next = third_block
# third_block.next = llist.tail

def random_seq():
    llist = LinkedList()
    lst = []
    for x in range(random.randint(2,9)):
        num = random.randint(10,99)
        lst.append(num)
        llist.adding_items_in_llist(num)
    
    execution(llist,len(lst))

def random_sorted():
    llist = LinkedList()
    lst = []
    length = random.randint(2,9)
    for x in range(length):
        num = random.randint(10,99)
        lst.append(num)
    lst.sort()
    for item in lst:
        llist.adding_items_in_llist(item)
    execution(llist,len(lst))

def random_fixed_size():
    llist = LinkedList()
    lst = []
    length = int(input("Enter the number of items to be in the linked list : "))
    for x in range(length):
        num = random.randint(10,99)
        lst.append(num)
    lst.sort()
    for item in lst:
        llist.adding_items_in_llist(item)
    execution(llist,len(lst))

def user_defined_list():
    llist = LinkedList()
    lst = []
    length = int(input("Enter the number of items to be in the linked list : "))
    for x in range(length):
        num = int(input("Enter the number : "))
        lst.append(num)
        llist.adding_items_in_llist(num)
    execution(llist,len(lst))

def execution(llist,length):

    print("Before inserting element at first position")
    print(llist.display())
    llist.insert_at_first(89)
    print("After inserting element at first position")
    print(llist.display())

    print("Before inserting element at last position")
    print(llist.display())
    llist.insert_at_last(89)
    print("After inserting element at last position")
    print(llist.display())

    print("Before inserting element based on index")
    print(llist.display())
    llist.insert_between_nodes(89,random.randint(2,length))
    print("After inserting element based on index")
    print(llist.display())

    print("Before removing of first element")
    print(llist.display())
    llist.remove_at_first()
    print("After removing of first element")
    print(llist.display())

    print("Before removing of last element")
    print(llist.display())
    llist.remove_at_last()
    print("After removing of last element")
    print(llist.display())

    print("Before removing of element based on index")
    print(llist.display())
    llist.remove_between_nodes(random.randint(2,length))
    print("After removing of element based on index")
    print(llist.display())

    print("Searching for index")
    print(llist.display()) 
    print(llist.search(random.randint(10,99)))


random_seq()
random_sorted()
random_fixed_size()
user_defined_list()



