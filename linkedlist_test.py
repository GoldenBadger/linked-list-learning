"""Tests for linkedlist.py."""

import unittest

from linkedlist import Node

class TestLinkedList(unittest.TestCase):
    """Test the Node class."""

    def test_creation1(self):
        """Test manual assignment of next node."""
        first = Node(100)
        second = Node(200)
        first.next_node = second
        self.assertEqual(first.next_node, second)

    def test_creation2(self):
        """Test assignment of next node via constructor."""
        second = Node(200)
        first = Node(100, second)
        self.assertEqual(first.next_node, second)

    def test_print(self):
        """Test printing of a linked list."""
        second = Node(200)
        first = Node(100, second)
        self.assertEqual(first.print(), "[100, 200]")

    def test_from_list(self):
        """Test the creation of a linked list from a standard Python list."""
        linked_list = Node.from_list([1, 2, 3, 4, 5])
        self.assertEqual(linked_list.value, 1)
        self.assertEqual(linked_list.next_node.value, 2)

if __name__ == "__main__":
    unittest.main()
