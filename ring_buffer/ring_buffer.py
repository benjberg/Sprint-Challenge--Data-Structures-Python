from DLL import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

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
        get_all = []
        for i in self.storage:
            if i != None:
                get_all.append(i)

                return get_all