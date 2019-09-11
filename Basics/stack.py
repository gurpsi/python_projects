class stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        """
        :param item: The item to be added in to the stack.
        :return: Nothing

        The runtime for this is O(1), or constant time because appending
        to the last of the list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        """
        :return: Removes and returns the last item form the list, i.e. the top item of the stack.

        The runtime is constant as we are removing the last item form the list. O(1)
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

