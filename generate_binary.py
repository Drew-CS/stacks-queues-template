# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Deven Mistry
# ASSIGNMENT:   Project 2: Stacks & Queues

from queue import Queue

def generate_binary_numbers(n):
  binary_queue = Queue()
  #temporary queue to generate binary numbers
  q = Queue()
  q.put('1')
  for i in range(n):
    front = str(q.get())
    q.put(front + '0')
    q.put(front + '1')
    binary_queue.put(front)
  return binary_queue

print(generate_binary_numbers(8).queue)
