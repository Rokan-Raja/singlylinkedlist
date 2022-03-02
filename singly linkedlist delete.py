class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def append(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_data
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def deletenode(self,new_data):
        temp=self.head
        if temp is not None:
            if temp.data == new_data:
                self.head = temp.next
                temp = None
                return
            while temp is not None:
                if temp.data == new_data:
                    break
                prev = temp
                temp = temp.next
            if temp == None:
                return
            prev.next = temp.next
            temp = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=",")
            temp = temp.next

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(6)
    llist.push(9)
    llist.append(8)
    llist.push(4)
    llist.append(7)
    llist.printlist()
    llist.deletenode(6)
    print("\nLinked List after Deletion of 1:")
    llist.printlist()


