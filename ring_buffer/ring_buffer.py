from double_link_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()


#check if storage is full
#if not add item to tail
#updates current count
#if it is full remove the first entry (head)
# add new item to tail
# if removed head was current set current to the tail
    def append(self, item):
       if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
       elif self.storage.length == self.capacity:
            remove = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if remove == self.current:
                self.current = self.storage.tail



    def get(self):
         list_buffer_contents = []
         node = self.current
         list_buffer_contents.append(node.value)

         if node.next is not None:
            node_2 = node.next
         else:
            node_2 = self.storage.head

         while node_2 != node:
            list_buffer_contents.append(node_2.value)
            if node_2.next is not None:
                node_2 = node_2.next
            else:
                node_2 = self.storage.head

         return list_buffer_contents
