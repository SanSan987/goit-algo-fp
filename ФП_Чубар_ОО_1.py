class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

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

    def search_element(self, data: int) -> Node | None:
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


# Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Алгоритм сортування для однозв'язного списку (сортування злиттям)
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = LinkedList()
        right = LinkedList()
        left.head = self.head
        right.head = next_to_middle

        left.merge_sort()
        right.merge_sort()

        sorted_list = self.sorted_merge(left.head, right.head)
        self.head = sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        
        return result


# Функція для об'єднання двох відсортованих однозв'язних списків
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next


# Приклади використання
llist1 = LinkedList()
llist2 = LinkedList()

# Вставляємо вузли у список 1
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

# Вставляємо вузли у список 2
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

# Об'єднуємо два відсортовані списки
merged_head = merge_sorted_lists(llist1.head, llist2.head)

# Створюємо новий зв'язний список для зручного друку результату
merged_list = LinkedList()
merged_list.head = merged_head

print("Об'єднаний відсортований список:")
merged_list.print_list()

# Приклад реверсування списку
print("\nРеверсування списку:")
llist1.reverse()
llist1.print_list()

# Приклад сортування злиттям
print("\nСортування злиттям:")
llist1.merge_sort()
llist1.print_list()


# Результат виконання (копія з теміналу):
# Об'єднаний відсортований список:
# 1
# 2
# 3
# 4
# 5
# 6

# Реверсування списку:
# 6
# 5
# 4
# 3
# 2
# 1

# Сортування злиттям:
# 1
# 2
# 3
# 4
# 5
# 6