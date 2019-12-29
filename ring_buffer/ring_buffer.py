from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If the list is empty
        if self.storage.length == 0:
            self.storage.add_to_head(item) 
        # if the list is not full. 
        elif self.storage.length < self.capacity:
            self.storage.add_to_head(item)

        # If the list is full
        elif self.storage.length == self.capacity:
            if self.current is None:
                self.current = 1
            elif self.current == self.capacity:
                self.current = 1
            else:
                self.current += 1
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)
            # self.storage.move_to_front(self.storage.tail)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        if self.current is None or self.current == 0:
            node = self.storage.tail

            while True:
                list_buffer_contents.append(node.value)
                node = node.prev
                if node is None:
                    break
            return list_buffer_contents
        
        else:
            # move up the right number of offsets
            offset = self.capacity - self.current
            node = self.storage.tail
            for i in range(offset):
                node = node.prev
            while True:
                list_buffer_contents.append(node.value)
                node = node.prev
                if node is None:
                    break
            node = self.storage.tail
            for i in range(offset):
                list_buffer_contents.append(node.value)
                node = node.prev
            return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
