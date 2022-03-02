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
    def insertafter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def append(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
if __name__ =='__main__':
    llist =linkedlist()
    llist.append(9)
    llist.push(3)
    llist.append(1)
    llist.push(4)
    llist.insertafter(llist.head.next,8)
    llist.printlist()


