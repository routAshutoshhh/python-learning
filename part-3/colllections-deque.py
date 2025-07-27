from collections import deque
d = deque()

d.append(1)
d.append(2)

print(d)

#appending the elements in the left side of the deque- basically appending the elemnents into the start of the deque
d.appendleft(0)

print(d)

#removing and popping the final elements of the deque
d.pop()
print(d)

#poping the first elements of the deque  or from the left side of the deque
d.popleft()
print(d)


d.clear()
print(d)

#extending the deque  with any list or aadding the elements from the left  side

d.extend([3, 4, 5 ])
print(d)
d.extendleft([0, -1, -2])
print(d)