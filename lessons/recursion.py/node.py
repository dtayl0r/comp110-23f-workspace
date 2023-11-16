"""Node class for a linked list."""

from __future__ import annotations

class Node:

    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            # base case
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + "->" + str(self.next)

    

node_c = Node(2, None)
node_b = Node(1, node_c)
node_a = Node(0, node_b)