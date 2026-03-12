"""
Author: Vidhi Pandey
Assignment: Data Structures & Systems Design
Role: AI/ML Agentic AI Internship
"""
"""
Assignment: Data Structures & Systems Design

Problem 1: LRU Cache

Explanation:
To achieve O(1) performance for both get() and put(), I used two data structures:
a hash map (dictionary) and a doubly linked list.

The hash map stores key → node mappings, allowing constant-time lookup
when retrieving values.

The doubly linked list maintains the order of usage. The most recently
used node is moved to the front of the list, while the least recently
used node stays near the tail.

When the cache exceeds its capacity, the node at the tail (least recently
used) is removed. This combination allows both lookup and updates to
run in constant time.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._insert(node)

        return node.value

    def put(self, key, value):

        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]

        node = Node(key, value)
        self._insert(node)

        self.cache[key] = node

        if len(self.cache) > self.capacity:

            lru = self.tail.prev
            self._remove(lru)

            del self.cache[lru.key]
cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # 10

cache.put(3, 30)

print(cache.get(2))  # -1

# ---------------------------
# Problem 2: Event Scheduler
# ---------------------------

"""

Explanation:
To determine if a person can attend all events, the events are sorted
by start time. After sorting, each event is compared with the previous
one. If the start time of the current event is earlier than the end
time of the previous event, an overlap exists.

For calculating the minimum number of meeting rooms, start times and
end times are separated and sorted. Two pointers track meeting starts
and endings. If a meeting starts before the earliest meeting ends,
a new room is needed. Otherwise, a room becomes free and can be reused.
"""
def can_attend_all(events):
    # sort events by start time
    events.sort(key=lambda x: x[0])

    for i in range(1, len(events)):
        prev_end = events[i-1][1]
        curr_start = events[i][0]

        if curr_start < prev_end:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    start_times = sorted([e[0] for e in events])
    end_times = sorted([e[1] for e in events])

    rooms = 0
    max_rooms = 0
    start_pointer = 0
    end_pointer = 0

    while s < len(events):
        if start_times[s] < end_times[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1

    return max_rooms
events = [(9,10), (10,11), (11,12)]

print(can_attend_all(events))        # True
print(min_rooms_required(events))    # 1

"""
Final Discussion & Analysis

1. Time and Space Complexity

LRU Cache

get(key):
Time Complexity: O(1)
The key lookup is performed using a hash map, which allows constant-time access.
If the key exists, the node is removed from its current position in the doubly
linked list and moved to the front, which also takes constant time.

put(key, value):
Time Complexity: O(1)
Insertion and updates are done using the hash map for quick lookup and the
doubly linked list for maintaining usage order. If the cache exceeds its
capacity, the least recently used element (at the tail of the list) is removed
in constant time.

Space Complexity:
O(capacity), since the cache stores at most the number of elements defined by
its capacity.

# ---------------------------
# Problem 2: Event Scheduler
# ---------------------------

can_attend_all(events):
Time Complexity: O(n log n)
The events must first be sorted by start time. After sorting, a single linear
scan is used to check for overlaps.

Space Complexity: O(1) (excluding sorting overhead).

min_rooms_required(events):
Time Complexity: O(n log n)
Sorting the start times and end times dominates the complexity. The two-pointer
traversal afterward runs in linear time.

Space Complexity: O(n) because we store separate start and end time arrays.


2. Trade-offs: Hash Map + Doubly Linked List for LRU Cache

A hash map alone allows fast key lookup but does not maintain the order in which
items are used. A linked list alone can maintain order but requires O(n) time to
locate elements.

Combining both structures solves this problem efficiently. The hash map provides
direct access to nodes in constant time, while the doubly linked list maintains
the order of usage and allows constant-time insertion and deletion. A doubly
linked list is preferred over a singly linked list because it allows removal of
a node when only the node reference is available.


3. Future Proofing: Assigning Specific Room Numbers

To assign specific room numbers to events, the scheduler could maintain a
priority queue (min heap) that tracks the earliest finishing meeting in each
room.

Each entry in the heap could store:
(end_time, room_id)

When scheduling a new event:
- If the earliest finishing room becomes free before the new meeting starts,
  reuse that room.
- Otherwise, allocate a new room.

This approach ensures efficient scheduling while also tracking which room is
assigned to each meeting.


4. Concurrency: Making the LRU Cache Thread-Safe

If multiple threads access the cache simultaneously, race conditions could occur
when modifying the shared hash map and linked list.

To make the cache thread-safe, synchronization mechanisms such as locks
(e.g., threading.Lock in Python) should be used around the get() and put()
operations to ensure that only one thread modifies the cache at a time.

In high-performance systems, more advanced approaches such as read-write locks
or concurrent data structures may be used to reduce contention while still
maintaining consistency.
"""