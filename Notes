# Python Notes: Using `collections.deque`

## Introduction

`collections.deque` is a double-ended queue that supports adding and removing elements from both ends with approximately equal efficiency. This makes it an ideal choice for implementing queues and stacks in Python.

## Basic Operations

### Creating a `deque`

```python
from collections import deque

# Create an empty deque
dq = deque()
```

### Adding Elements

- **Append to the right (end):**

```python
dq.append(1)  # deque([1])
dq.append(2)  # deque([1, 2])
```

- **Append to the left (front):**

```python
dq.appendleft(3)  # deque([3, 1, 2])
```

### Removing Elements

- **Pop from the right (end):**

```python
last_element = dq.pop()  # last_element = 2, deque([3, 1])
```

- **Pop from the left (front):**

```python
first_element = dq.popleft()  # first_element = 3, deque([1])
```

### Checking if `deque` is empty

```python
if len(dq) == 0:
    print("deque is empty")
else:
    print("deque is not empty")
```

or simply:

```python
if dq:
    print("deque is not empty")
else:
    print("deque is empty")
```

