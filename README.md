# assignment-8
---
```markdown
#  Memory Management Simulation using Paging

This Python program simulates **memory management** using **paging** with support for **FIFO page replacement** when physical memory is full.

##  Features

- Accepts total physical memory size and frame size
- Accepts multiple processes with varying memory requirements
- Divides each process into pages
- Allocates memory frames using paging
- Handles memory full scenario using FIFO page replacement
- Displays page tables and memory status

---

##  How to Run

```bash
python memory_paging_simulator.py
```

Make sure you have Python 3.x installed.

---

##  Example Execution

###  Sample Input

```
Enter total physical memory size (in bytes): 512
Enter frame size (in bytes): 128
Enter number of processes: 3
Enter memory required by Process 1 (in bytes): 256
Enter memory required by Process 2 (in bytes): 384
Enter memory required by Process 3 (in bytes): 256
```

###  Sample Output

```
Allocating memory for Process 1: 256 bytes, 2 pages
Allocated 2/2 pages.

Allocating memory for Process 2: 384 bytes, 3 pages
Allocated 2/3 pages.
Memory full! Replacing frame 0 (P1:Page0)
Allocated 3/3 pages.

Allocating memory for Process 3: 256 bytes, 2 pages
Memory full! Replacing frame 1 (P1:Page1)
Memory full! Replacing frame 2 (P2:Page0)
Allocated 2/2 pages.

--- Page Tables ---

Process 1:
  Page 0 -> Replaced
  Page 1 -> Replaced

Process 2:
  Page 1 -> Frame 3
  Page 2 -> Frame 1

Process 3:
  Page 0 -> Frame 0
  Page 1 -> Frame 2

--- Frame Allocation Status ---
Frame 0: P3:Page0
Frame 1: P2:Page2
Frame 2: P3:Page1
Frame 3: P2:Page1
```

---

##  Code Structure

- `memory_paging_simulator.py`: Main program with classes for `Frame`, `Process`, and `MemoryManager`.

---

##  Notes

- Page replacement strategy used: **FIFO**
- Page size = frame size
- Page table entries show: `Page -> Frame`
- Replaced pages are removed from the page table.

---
