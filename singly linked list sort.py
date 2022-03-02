class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def sortlist(self):
        current = self.head
        index = None
        if (self.head == None):
            return
        else:
            while (current != None):
                index = current.next
                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
    def printlist(self):
        temp = self.head;
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next


if __name__ == "__main__":
    llist =linkedlist()
    llist.add(4)
    llist.add(8)
    llist.add(2)
    llist.add(3)
    print("Before Sorting")
    llist.printlist()
    print("\nAfter Swapping")
    llist.sortlist()
    llist.printlist()