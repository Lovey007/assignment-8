from collections import deque

class Frame:
    def __init__(self, frame_id):
        self.frame_id = frame_id
        self.occupied = False
        self.process_id = None
        self.page_number = None

    def __repr__(self):
        if self.occupied:
            return f"P{self.process_id}:Page{self.page_number}"
        return "Free"

class Process:
    def __init__(self, pid, memory_required, page_size):
        self.pid = pid
        self.memory_required = memory_required
        self.page_size = page_size
        self.num_pages = -(-memory_required // page_size)  # ceiling division
        self.page_table = {}  # page_number -> frame_id

    def __repr__(self):
        return f"Process {self.pid}: {self.memory_required} bytes, {self.num_pages} pages"

class MemoryManager:
    def __init__(self, total_memory, frame_size):
        self.total_memory = total_memory
        self.frame_size = frame_size
        self.total_frames = total_memory // frame_size
        self.frames = [Frame(i) for i in range(self.total_frames)]
        self.processes = {}
        self.frame_queue = deque()  # FIFO for page replacement

    def allocate_process(self, process):
        print(f"\nAllocating memory for {process}")
        allocated_pages = 0
        for page_num in range(process.num_pages):
            free_frame = self.find_free_frame()
            if free_frame is not None:
                self.assign_frame(free_frame, process.pid, page_num)
                process.page_table[page_num] = free_frame.frame_id
                allocated_pages += 1
            else:
                # FIFO Replacement Strategy
                victim = self.frame_queue.popleft()
                print(f"Memory full! Replacing frame {victim.frame_id} (P{victim.process_id}:Page{victim.page_number})")
                old_process = self.processes[victim.process_id]
                del old_process.page_table[victim.page_number]
                self.assign_frame(victim, process.pid, page_num)
                process.page_table[page_num] = victim.frame_id
                allocated_pages += 1
        self.processes[process.pid] = process
        print(f"Allocated {allocated_pages}/{process.num_pages} pages.")

    def find_free_frame(self):
        for frame in self.frames:
            if not frame.occupied:
                return frame
        return None

    def assign_frame(self, frame, pid, page_num):
        frame.occupied = True
        frame.process_id = pid
        frame.page_number = page_num
        self.frame_queue.append(frame)

    def display_memory_status(self):
        print("\n--- Frame Allocation Status ---")
        for i, frame in enumerate(self.frames):
            print(f"Frame {i}: {frame}")

    def display_page_tables(self):
        print("\n--- Page Tables ---")
        for pid, process in self.processes.items():
            print(f"\nProcess {pid}:")
            for page, frame in process.page_table.items():
                print(f"  Page {page} -> Frame {frame}")



total_memory = int(input("Enter total physical memory size (in bytes): "))
frame_size = int(input("Enter frame size (in bytes): "))

mm = MemoryManager(total_memory, frame_size)

num_processes = int(input("Enter number of processes: "))
for pid in range(1, num_processes + 1):
    mem = int(input(f"Enter memory required by Process {pid} (in bytes): "))
    process = Process(pid, mem, frame_size)
    mm.allocate_process(process)

mm.display_page_tables()
mm.display_memory_status()



