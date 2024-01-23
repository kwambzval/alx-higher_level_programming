#!/usr/bin/python3
"""
This module contains a class Node that defines a node of a singly linked list,
and a class SinglyLinkedList that defines a singly linked list.
"""


class Node:
    """
    This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize Node instance with data and next_node.

        Args:
            data (int): The data of the Node. Must be an integer.
            next_node (Node, optional): The next node in
            the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the Node instance.

        Returns:
            int: The data of the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node instance.

        Args:
            value (int): The data of the Node. Must be an integer.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node of the Node instance.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node of the Node instance.

        Args:
            value (Node): The next node in the linked list.
            Can be None or must be a Node.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize SinglyLinkedList instance with head.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted
        position in the list (increasing order).

        Args:
            value (int): The data of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """
        Return a string that represents the SinglyLinkedList instance.

        Returns:
            str: A string that represents the SinglyLinkedList instance.
        """
        nodes = []
        tmp = self.__head
        while tmp is not None:
            nodes.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(nodes)
