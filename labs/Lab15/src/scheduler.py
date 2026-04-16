"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        """Initialize the scheduler."""
        self.heap = []
        self.count = 0

    def add_task(self, priority, description):
        """Add a task to the scheduler.

        Args:
            priority: An integer priority (lower = more urgent).
            description: A string describing the task.
        """
        heapq.heappush(self.heap, (priority, self.count, description))
        self.count = self.count + 1

    def next_task(self):
        """Remove and return the highest-priority task's description.

        Returns:
            The description string, or None if empty.
        """
        if len(self.heap) == 0:
            return None

        item = heapq.heappop(self.heap)
        description = item[2]
        return description

    def peek(self):
        """Return the highest-priority task's description without removing it.

        Returns:
            The description string, or None if empty.
        """
        if len(self.heap) == 0:
            return None

        item = self.heap[0]
        description = item[2]
        return description

    def __len__(self):
        """Return the number of pending tasks."""
        return len(self.heap)

    def is_empty(self):
        """Return True if there are no pending tasks."""
        return len(self.heap) == 0