print("Task 1___________________________________________________________________________________")

"""Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
            
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")   
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_beginning(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        self.head = prev    
                           
    def our_sort(self):
        llist_sorted = LinkedList()
        current = self.head

        while current:
            next_node = current.next  

            if llist_sorted.head is None:
                llist_sorted.insert_at_beginning(current.data)
            else:
                sorted_current = llist_sorted.head
                sorted_prev = None
                inserted = False  

                while sorted_current:
                    if sorted_current.data > current.data:
                        new_node = Node(current.data)
                        new_node.next = sorted_current
                        if sorted_prev is not None:
                            sorted_prev.next = new_node
                        else:
                            llist_sorted.head = new_node
                        inserted = True
                        break

                    sorted_prev = sorted_current
                    sorted_current = sorted_current.next

                if not inserted:
                    new_node = Node(current.data)
                    sorted_prev.next = new_node
            current = next_node
        self.head = llist_sorted.head


def merge_sort_list(listA, listB):
    current = listA.head
    while current:
        if current.next is None:
            break
        next_node = current.next            
        current = next_node       
    current.next = listB.head
    
    listA.our_sort()

    return listA

print("USING_____________________________________________________")

llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

print("FUNC 1")
llist.reverse()
llist.print_list()


print("FUNC 2")
llist.our_sort()
llist.print_list()



print("FUNC 3")
llist1 = LinkedList()
llist1.insert_at_beginning(135)
llist1.insert_at_beginning(115)
llist1.insert_at_beginning(9)
llist1.insert_at_beginning(35)

result = merge_sort_list(llist, llist1)
result.print_list()


