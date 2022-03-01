# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Deven Mistry
# ASSIGNMENT:   Project 2: Stacks & Queues

# function for queues
def matcher(expr):
  stack = []
  for c in expr:
    if c in '[({':
      stack.append(c)
    elif c in '])}':
      # detecting stack length
      if len(stack) == 0:
        return False
      if '])}'.index(c) != '[({'.index(stack.pop()):
        return False
  return len(stack) == 0

# test cases
print(matcher('[()]'))
print(matcher('[('))
print(matcher('hello'))
