# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Deven Mistry
# ASSIGNMENT:   Project 2: Stacks & Queues

from collections import deque

# this method return the reversed queue
def reverse(Q):
        # Queue length
        length = len(Q)
        # 2nd queue
        queue = deque()
        # Queue iteration
        for i in range(length):
                # Last element
                for j in range(length - 1):
                        a = Q.popleft()
                        Q.appendleft(a)
                # Added to the new queue
                queue.appendleft(Q.popleft())
        # Queue returned
        return queue

# Declare a queue
Que = deque()

# Elements add into que
Que.append(1)
Que.append(2)
Que.append(3)
Que.append(4)

# call the reverse function
queue = reverse(Que)

# Print the reversed queue
while (len(queue) > 0):
        print(queue.popleft(), end = " ")
