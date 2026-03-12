# Data Structures & Systems Design Assignment

This repository contains solutions for the **Data Structures & Systems Design assessment** for an AI/ML (Agentic AI) Internship role. The assignment focuses on implementing efficient data structures, algorithm design, and explaining system-level reasoning.

---

# Problems Implemented

## 1. LRU Cache Implementation

A **Least Recently Used (LRU) Cache** is implemented with the following operations:

- `get(key)`  
  Returns the value of the key if it exists in the cache. Accessing a key marks it as recently used.

- `put(key, value)`  
  Inserts or updates a key-value pair. If the cache reaches its capacity, the least recently used item is evicted.

### Design Approach

The cache is implemented using:

- **Hash Map (Dictionary)** → provides O(1) key lookup
- **Doubly Linked List** → maintains the order of recently used elements

The most recently used node is moved to the front of the list, while the least recently used node stays near the tail and is removed when the capacity is exceeded.

This combination ensures both `get()` and `put()` run in **O(1) time complexity**.

---

## 2. Event Scheduler

This module implements basic scheduling logic for meeting events represented as:
(start_time, end_time)

Example:
[(9,10), (10,11), (11,12)]

### Functions

#### `can_attend_all(events)`

Determines whether a person can attend all events without any overlap.

Approach:
- Sort events by start time
- Compare adjacent intervals
- If a start time is earlier than the previous end time, an overlap exists

---

#### `min_rooms_required(events)`

Calculates the **minimum number of meeting rooms required** to schedule all events.

Approach:
- Separate start times and end times
- Sort both lists
- Use a two-pointer technique to track overlapping meetings

The maximum number of simultaneous meetings determines the required number of rooms.

---

# Time Complexity Analysis

### LRU Cache

| Operation | Complexity |
|-----------|------------|
| get() | O(1) |
| put() | O(1) |

Space Complexity: **O(capacity)**

---

### Event Scheduler

| Function | Complexity |
|----------|------------|
| can_attend_all() | O(n log n) |
| min_rooms_required() | O(n log n) |

The complexity is dominated by sorting operations.

---

# System Design Discussion

## Trade-offs

A **hash map** allows fast key lookup but cannot maintain order of usage.  
A **doubly linked list** maintains order but cannot perform fast searches.

Combining both provides constant-time lookup and constant-time insertion/deletion.

---

## Future Improvements

To assign specific room numbers (e.g., Room A, Room B), the scheduler could use a **priority queue (min heap)** that tracks the earliest finishing meeting room and reuses it when available.

---

## Concurrency Considerations

If multiple threads access the cache simultaneously, race conditions may occur while modifying shared structures.

To make the cache thread-safe, synchronization mechanisms such as **locks (e.g., `threading.Lock`)** can be used around `get()` and `put()` operations.

---

# Repository Structure
data-structures-systems-design-assignment
│
├── assignment_lru_scheduler.py
└── README.md


---

# Author

Vidhi Pandey
