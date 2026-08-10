class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    