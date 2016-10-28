"""Simple linked list class for learning."""

class Node:
    """Simple linked list."""
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    @classmethod
    def from_list(cls, other_list):
        """TODO: Create a linked list from a standard python list."""

    @property
    def value(self):
        """Get the node's current value."""
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self._next_node

    @next_node.setter
    def next_node(self, new_next_node):
        self._next_node = new_next_node

    def print(self):
        """TODO: Print the entire list to standard output."""
