from collections import deque

print('*' * 20 + ' stack ' + '*' * 20)
stack = deque()

for i in range(1, 6):
    stack.append(i)
    print(stack)

for i in range(5):
    print(stack.pop())

print('*' * 20 + ' queue ' + '*' * 20)
queue = deque()
for i in range(1, 6):
    queue.append(i)
    print(queue)

for i in range(5):
    print(queue.popleft()) 