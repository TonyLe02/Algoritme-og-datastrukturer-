from collections import deque

# Create a deque
d = deque()

# Push numbers 1 to 20 to the end of the deque
for i in range(1, 21):
    d.append(i)

# Print the deque after pushing numbers
print("After pushing numbers 1 to 20:")
for i in d:
    print(i, end=' ')

print()

# Pop an element from the beginning of the deque (queue operation)
print("Pop from the beginning (queue operation):", d.popleft())

# Pop an element from the end of the deque (stack operation)
print("Pop from the end (stack operation):", d.pop())

# Print the deque after popping numbers
print("After popping numbers:")
for i in d:
    print(i, end=' ')

print()
