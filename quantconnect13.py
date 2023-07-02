# refer to https://youtu.be/_BHi5Y2Aow4  , Algorithmic Trading Using Python #6 - Indicators & Historical Data




#SECTION A : Testing logic flow and inaction of if elif else statements used in conjunction
x = 5
#  so this is the logic used in quantconnect, essentially even if it passes the first if, if it fails the nested if it will just ingore all the othet elif and else which is why they opt to use this structure instead of just if statements
if x > 3:
    if x > 5:
        print("foo")
elif x > 4:
    print("bar")
else:
    print("baz")



# SECTION B: deque # https://www.geeksforgeeks.org/deque-in-python/ , can append left and right at O(1) while list append right is O(1) but to insert left is O(n)
from collections import deque

queue = deque([1, 2, 3], maxlen=5)
print(queue)
print(queue[0])
queue.appendleft(6)
print(queue)
queue.append(4)
print(queue)

# creating a deque with max length based on period
# if maxlen is specified as a paramter for dequeue, when dequeue is full when new items added same amount removed from the other end
# https://docs.python.org/3/library/collections.html
queue.appendleft(100)
print(queue)