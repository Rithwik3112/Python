class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def add_front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            lastnode=self.head
            while lastnode.next is not None:
                lastnode=lastnode.next
            lastnode.next = newnode
    def display(self):
        currntnode=self.head
        while currntnode is not None:
            print(f"{currntnode.data}-> ", end="")
            currntnode=currntnode.next
        print("the end ")
if __name__=='__main__':
    ll=linked_list()
    ll.add_front(3)
    ll.add_front(4)
    ll.add_end(6)
    ll.add_end(5)
    ll.add_end(8)
    ll.add_end("re")
    ll.display()








