# There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

# Implement the TaskManager class:

# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

# Note that a user may be assigned multiple tasks.


from typing import List
from sortedcontainers import SortedList

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        # Defined a sorted list that will contain tuples
        self.sortList = SortedList()
        # Defined a taskInfo dictionary for mapping task
        self.taskInfo = {}

        # Iterate through each pairs in tasks
        for u, t, p in tasks:
            # Add to sortList by re-arranging as Priority, Task, User
            self.sortList.add((p, t, u))
            # Map the task with (priority, userId)
            self.taskInfo[t] = (p, u)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Add the new task to sortList, which will automatically sort the new input based on priority
        self.sortList.add((priority, taskId, userId))
        # Map it to taskInfo dictionary
        self.taskInfo[taskId] = (priority, userId)


    def edit(self, taskId: int, newPriority: int) -> None:
        # Get the old priority & user using taskID from taskInfo
        oldPriority, user = self.taskInfo[taskId]

        # Drop the record from sortList
        self.sortList.discard((oldPriority, taskId, user))
        # Add the new priority to sortList
        self.sortList.add((newPriority, taskId, user))

        # Update the taskId in taskInfo with new priority
        self.taskInfo[taskId] = (newPriority, user)


    def rmv(self, taskId: int) -> None:
        # Get priority & user from taskId
        oldPriority, user = self.taskInfo[taskId]

        # Drop the record from sortList & taskInfo
        self.sortList.discard((oldPriority, taskId, user))
        del self.taskInfo[taskId]


    def execTop(self) -> int:
        # Check if sortList is already empty -> return -1
        if not self.sortList:
            return -1
        
        # Get the last record which has highest priority
        p, t, u = self.sortList[-1]
        # Pop out the record & return that user
        self.sortList.pop(-1)

        return u