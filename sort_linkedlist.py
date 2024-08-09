from linked_list import create_node 
class merge_list():
    def __init__(self) -> None:
        self.dummy = create_node("hello world")
        self.tail = self.dummy 
    def sort_list(self, l1, l2):
        while l1 and l2:
            if l1.data < l2.data:
                self.tail.next = l1
                l1 = l1.next
            else:
                self.tail.next = l2
                l2 = l2.next 
        while l1:
            self.tail = l1
            l1 = l1.next
        while l2:
            self.tail = l2
            l2 = l2.next
        return self.dummy

def sort_list(l1, l2):
    dummy = create_node(0)
    tail = dummy
    while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next 
    while l1:
            tail = l1
            l1 = l1.next
    while l2:
            tail = l2
            l2 = l2.next
    return tail.data
A = create_node(1)
B=create_node(2)
C = create_node(5)
D = create_node(2)
E = create_node(3)
F = create_node(4)
A.next = B
B.next = C

D.next = E
E.next = F
q = merge_list()
print(sort_list(A, D))