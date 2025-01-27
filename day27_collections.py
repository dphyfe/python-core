# Day 27: collections module for my practice

from collections import defaultdict, Counter, namedtuple, deque

# My defaultdict (1)
my_dict = defaultdict(list)
my_dict["a"].append(1)
my_dict["a"].append(2)
my_dict["b"].append(3)
print(f"My defaultdict: {dict(my_dict)}")

# My Counter (2)
my_data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
my_count = Counter(my_data)
print(f"My count: {my_count}")
print(f"My most common: {my_count.most_common(2)}")

# My namedtuple (3)
MyPoint = namedtuple("Point", ["x", "y"])
my_p = MyPoint(3, 4)
print(f"My point: {my_p}")
print(f"My x: {my_p.x}")

# My deque (4)
my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
print(f"My deque: {list(my_deque)}")

# My deque pop (5)
my_dq = deque([1, 2, 3])
my_right = my_dq.pop()
my_left = my_dq.popleft()
print(f"My popped right: {my_right}, left: {my_left}")

# My Counter subtraction (6)
my_c1 = Counter(["a", "b", "c", "a"])
my_c2 = Counter(["a", "b"])
my_result = my_c1 - my_c2
print(f"My subtracted: {my_result}")

# My defaultdict with int (7)
my_counter = defaultdict(int)
my_counter["apple"] += 1
my_counter["apple"] += 1
print(f"My counter: {dict(my_counter)}")

# My namedtuple as dict (8)
MyRecord = namedtuple("Record", ["id", "name"])
my_rec = MyRecord(1, "David")
my_dict_form = my_rec._asdict()
print(f"My dict form: {my_dict_form}")

# My Counter update (9)
my_c1 = Counter(["a", "b", "a"])
my_c2 = Counter(["a", "c"])
my_c1.update(my_c2)
print(f"My updated: {my_c1}")

# My deque maxlen (10)
my_limited = deque([1, 2], maxlen=3)
my_limited.append(3)
my_limited.append(4)
print(f"My limited deque: {list(my_limited)}")
