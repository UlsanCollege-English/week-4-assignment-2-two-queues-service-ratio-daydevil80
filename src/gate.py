# src/gate.py
from collections import deque

class Gate:
    def __init__(self):
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0  # current index in the pattern
        self._fast = deque()  # fastpass queue
        self._reg = deque()   # regular queue

    def arrive(self, line, person_id):
        if line == "fastpass":
            self._fast.append(person_id)
        elif line == "regular":
            self._reg.append(person_id)
        else:
            raise ValueError("Unknown line type")

    def serve(self):
        if not self._fast and not self._reg:
            raise IndexError("Both lines empty")

        # Keep looping until we find a non-empty queue
        while True:
            line_type = self._pattern[self._idx]
            self._idx = (self._idx + 1) % 4

            if line_type == "fastpass" and self._fast:
                return self._fast.popleft()
            elif line_type == "regular" and self._reg:
                return self._reg.popleft()
            # If the chosen line is empty, continue to next pattern slot

    def peek_next_line(self):
        if not self._fast and not self._reg:
            return None

        temp_idx = self._idx
        while True:
            line_type = self._pattern[temp_idx]
            temp_idx = (temp_idx + 1) % 4
            if line_type == "fastpass" and self._fast:
                return "fastpass"
            elif line_type == "regular" and self._reg:
                return "regular"
