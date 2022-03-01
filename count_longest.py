# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Deven Mistry
# ASSIGNMENT:   Project 2: Stacks & Queues

# function for finding the longest queue
def count_longest(queue):
    result = [0]
    # indexing data
    for index,data in enumerate(queue):
        count = 0
        # iterating through queue
        for value in queue[index:]:
            if(value == data):
                count += 1
                result.append(count)
            else:
                result.append(count)
                break
    return max(result)
 # displaying test cases
if __name__ == '__main__':
    print(count_longest(['h','e','l','l','o']))
    print(count_longest(['m','m','m','m','m']))
    print(count_longest(['h','e','e','e']))
    print(count_longest([]))

