# import tkinter as tk
# from tkinter import ttk
# import random

# class SortingVisualizer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sorting Algorithm Visualizer")
#         self.array = []
#         self.canvas_width = 800
#         self.canvas_height = 400
#         self.bar_width = 0
#         self.speed = 50  # Animation speed in ms
#         self.is_sorting = False
        
#         # Setup GUI
#         self.setup_gui()
#         self.generate_array()

#     def setup_gui(self):
#         # Control Frame
#         control_frame = ttk.Frame(self.root)
#         control_frame.pack(pady=10)

#         # Algorithm Selection
#         ttk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
#         self.algo_var = tk.StringVar(value="Bubble Sort")
#         algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
#         algo_menu = ttk.Combobox(control_frame, textvariable=self.algo_var, values=algorithms, state="readonly")
#         algo_menu.pack(side=tk.LEFT, padx=5)

#         # Buttons
#         ttk.Button(control_frame, text="Generate New Array", command=self.generate_array).pack(side=tk.LEFT, padx=5)
#         ttk.Button(control_frame, text="Start Sorting", command=self.start_sorting).pack(side=tk.LEFT, padx=5)

#         # Speed Scale
#         ttk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=5)
#         self.speed_scale = ttk.Scale(control_frame, from_=10, to=200, orient=tk.HORIZONTAL, command=self.update_speed)
#         self.speed_scale.set(self.speed)
#         self.speed_scale.pack(side=tk.LEFT, padx=5)

#         # Canvas for visualization
#         self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
#         self.canvas.pack(pady=10)

#     def update_speed(self, value):
#         self.speed = int(float(value))

#     def generate_array(self):
#         if not self.is_sorting:
#             self.array = [random.randint(10, 300) for _ in range(30)]
#             self.draw_bars()

#     def draw_bars(self, compare=None, swap=None, sorted_indices=None):
#         self.canvas.delete("all")
#         self.bar_width = self.canvas_width // len(self.array)
#         sorted_indices = sorted_indices or []

#         for i, height in enumerate(self.array):
#             x0 = i * self.bar_width
#             y0 = self.canvas_height
#             x1 = (i + 1) * self.bar_width
#             y1 = self.canvas_height - height

#             color = "blue"  # Default color
#             if i in sorted_indices:
#                 color = "green"  # Sorted
#             elif compare and i in compare:
#                 color = "red"  # Comparing
#             elif swap and i in swap:
#                 color = "yellow"  # Swapping

#             self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

#     def start_sorting(self):
#         if not self.is_sorting:
#             self.is_sorting = True
#             algo = self.algo_var.get()
#             if algo == "Bubble Sort":
#                 self.bubble_sort()
#             elif algo == "Selection Sort":
#                 self.selection_sort()
#             elif algo == "Insertion Sort":
#                 self.insertion_sort()
#             elif algo == "Merge Sort":
#                 self.merge_sort(0, len(self.array) - 1)
#             elif algo == "Quick Sort":
#                 self.quick_sort(0, len(self.array) - 1)
#             self.root.after(self.speed * 10, self.stop_sorting)

#     def stop_sorting(self):
#         self.is_sorting = False
#         self.draw_bars(sorted_indices=list(range(len(self.array))))

#     def bubble_sort(self):
#         def step(i, j):
#             if i < len(self.array) - 1:
#                 if j < len(self.array) - i - 1:
#                     self.draw_bars(compare=[j, j + 1])
#                     if self.array[j] > self.array[j + 1]:
#                         self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
#                         self.draw_bars(swap=[j, j + 1])
#                     self.root.after(self.speed, lambda: step(i, j + 1))
#                 else:
#                     self.draw_bars(sorted_indices=[len(self.array) - i - 1])
#                     self.root.after(self.speed, lambda: step(i + 1, 0))
#         step(0, 0)

#     def selection_sort(self):
#         def step(i, j, min_idx):
#             if i < len(self.array) - 1:
#                 if j < len(self.array):
#                     self.draw_bars(compare=[j, min_idx])
#                     if self.array[j] < self.array[min_idx]:
#                         min_idx = j
#                     self.root.after(self.speed, lambda: step(i, j + 1, min_idx))
#                 else:
#                     self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
#                     self.draw_bars(swap=[i, min_idx], sorted_indices=[i])
#                     self.root.after(self.speed, lambda: step(i + 1, i + 2, i + 1))
#         step(0, 1, 0)

#     def insertion_sort(self):
#         def step(i, j, key):
#             if i < len(self.array):
#                 if j >= 0 and self.array[j] > key:
#                     self.draw_bars(compare=[j, j + 1])
#                     self.array[j + 1] = self.array[j]
#                     self.draw_bars(swap=[j, j + 1])
#                     self.root.after(self.speed, lambda: step(i, j - 1, key))
#                 else:
#                     self.array[j + 1] = key
#                     self.draw_bars(sorted_indices=[k for k in range(i + 1)])
#                     self.root.after(self.speed, lambda: step(i + 1, i, self.array[i + 1] if i + 1 < len(self.array) else None))
#         if len(self.array) > 1:
#             step(1, 0, self.array[1])

#     def merge_sort(self, left, right):
#         def merge(l, m, r):
#             left_arr = self.array[l:m + 1]
#             right_arr = self.array[m + 1:r + 1]
#             i = j = 0
#             k = l

#             def merge_step():
#                 nonlocal i, j, k
#                 if i < len(left_arr) and j < len(right_arr):
#                     self.draw_bars(compare=[l + i, m + 1 + j])
#                     if left_arr[i] <= right_arr[j]:
#                         self.array[k] = left_arr[i]
#                         i += 1
#                     else:
#                         self.array[k] = right_arr[j]
#                         j += 1
#                     self.draw_bars(swap=[k])
#                     k += 1
#                     self.root.after(self.speed, merge_step)
#                 elif i < len(left_arr):
#                     self.array[k] = left_arr[i]
#                     self.draw_bars(swap=[k])
#                     i += 1
#                     k += 1
#                     self.root.after(self.speed, merge_step)
#                 elif j < len(right_arr):
#                     self.array[k] = right_arr[j]
#                     self.draw_bars(swap=[k])
#                     j += 1
#                     k += 1
#                     self.root.after(self.speed, merge_step)

#             merge_step()

#         if left < right:
#             mid = (left + right) // 2
#             self.merge_sort(left, mid)
#             self.merge_sort(mid + 1, right)
#             merge(left, mid, right)

#     def quick_sort(self, low, high):
#         def partition(l, h, callback):
#             pivot = self.array[h]
#             i = l - 1

#             def partition_step(j):
#                 nonlocal i
#                 if j < h:
#                     self.draw_bars(compare=[j, h])
#                     if self.array[j] <= pivot:
#                         i += 1
#                         self.array[i], self.array[j] = self.array[j], self.array[i]
#                         self.draw_bars(swap=[i, j])
#                     self.root.after(self.speed, lambda: partition_step(j + 1))
#                 else:
#                     self.array[i + 1], self.array[h] = self.array[h], self.array[i + 1]
#                     self.draw_bars(swap=[i + 1, h])
#                     callback(i + 1)

#             partition_step(l)

#         def quicksort_step(l, h):
#             if l < h:
#                 def after_partition(pi):
#                     self.draw_bars(sorted_indices=[pi])
#                     quicksort_step(l, pi - 1)
#                     quicksort_step(pi + 1, h)
#                 partition(l, h, after_partition)

#         quicksort_step(low, high)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SortingVisualizer(root)
#     root.mainloop()























import tkinter as tk
from tkinter import ttk
import random

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.array = []
        self.canvas_width = 820
        self.canvas_height = 400
        self.bar_width = 0
        self.speed = 50  # Animation speed in ms
        self.is_sorting = False
        
        # Setup GUI
        self.setup_gui()
        self.generate_array()

    def setup_gui(self):
        # Control Frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        # Algorithm Selection
        ttk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
        self.algo_var = tk.StringVar(value="Bubble Sort")
        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
        algo_menu = ttk.Combobox(control_frame, textvariable=self.algo_var, values=algorithms, state="readonly")
        algo_menu.pack(side=tk.LEFT, padx=5)

        # Buttons
        ttk.Button(control_frame, text="Generate New Array", command=self.generate_array).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Start Sorting", command=self.start_sorting).pack(side=tk.LEFT, padx=5)

        # Speed Scale
        ttk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=5)
        self.speed_scale = ttk.Scale(control_frame, from_=10, to=200, orient=tk.HORIZONTAL, command=self.update_speed)
        self.speed_scale.set(self.speed)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(pady=10)

        # Label to display array values
        self.array_label = ttk.Label(self.root, text="", font=("Arial", 10))
        self.array_label.pack(pady=5)

    def update_speed(self, value):
        self.speed = int(float(value))

    def generate_array(self):
        if not self.is_sorting:
            self.array = [random.randint(10, 300) for _ in range(20)]
            self.draw_bars()
            self.update_array_label()

    def update_array_label(self):
        # Update the label with current array values
        array_str = "Arr: " + ", ".join(map(str, self.array))
        self.array_label.config(text=array_str)

    def draw_bars(self, compare=None, swap=None, sorted_indices=None):
        self.canvas.delete("all")
        self.bar_width = self.canvas_width // len(self.array)
        sorted_indices = sorted_indices or []

        for i, height in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = self.canvas_height
            x1 = (i + 1) * self.bar_width
            y1 = self.canvas_height - height

            color = "blue"  # Default color
            if i in sorted_indices:
                color = "green"  # Sorted
            elif compare and i in compare:
                color = "red"  # Comparing
            elif swap and i in swap:
                color = "yellow"  # Swapping

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        
        # Update array label after drawing bars
        self.update_array_label()

    def start_sorting(self):
        if not self.is_sorting:
            self.is_sorting = True
            algo = self.algo_var.get()
            if algo == "Bubble Sort":
                self.bubble_sort()
            elif algo == "Selection Sort":
                self.selection_sort()
            elif algo == "Insertion Sort":
                self.insertion_sort()
            elif algo == "Merge Sort":
                self.merge_sort(0, len(self.array) - 1)
            elif algo == "Quick Sort":
                self.quick_sort(0, len(self.array) - 1)
            self.root.after(self.speed * 10, self.stop_sorting)

    def stop_sorting(self):
        self.is_sorting = False
        self.draw_bars(sorted_indices=list(range(len(self.array))))

    def bubble_sort(self):
        def step(i, j):
            if i < len(self.array) - 1:
                if j < len(self.array) - i - 1:
                    self.draw_bars(compare=[j, j + 1])
                    if self.array[j] > self.array[j + 1]:
                        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                        self.draw_bars(swap=[j, j + 1])
                    self.root.after(self.speed, lambda: step(i, j + 1))
                else:
                    self.draw_bars(sorted_indices=[len(self.array) - i - 1])
                    self.root.after(self.speed, lambda: step(i + 1, 0))
        step(0, 0)

    def selection_sort(self):
        def step(i, j, min_idx):
            if i < len(self.array) - 1:
                if j < len(self.array):
                    self.draw_bars(compare=[j, min_idx])
                    if self.array[j] < self.array[min_idx]:
                        min_idx = j
                    self.root.after(self.speed, lambda: step(i, j + 1, min_idx))
                else:
                    self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
                    self.draw_bars(swap=[i, min_idx], sorted_indices=[i])
                    self.root.after(self.speed, lambda: step(i + 1, i + 2, i + 1))
        step(0, 1, 0)

    def insertion_sort(self):
        def step(i, j, key):
            if i < len(self.array):
                if j >= 0 and self.array[j] > key:
                    self.draw_bars(compare=[j, j + 1])
                    self.array[j + 1] = self.array[j]
                    self.draw_bars(swap=[j, j + 1])
                    self.root.after(self.speed, lambda: step(i, j - 1, key))
                else:
                    self.array[j + 1] = key
                    self.draw_bars(sorted_indices=[k for k in range(i + 1)])
                    self.root.after(self.speed, lambda: step(i + 1, i, self.array[i + 1] if i + 1 < len(self.array) else None))
        if len(self.array) > 1:
            step(1, 0, self.array[1])

    def merge_sort(self, left, right):
        def merge(l, m, r):
            left_arr = self.array[l:m + 1]
            right_arr = self.array[m + 1:r + 1]
            i = j = 0
            k = l

            def merge_step():
                nonlocal i, j, k
                if i < len(left_arr) and j < len(right_arr):
                    self.draw_bars(compare=[l + i, m + 1 + j])
                    if left_arr[i] <= right_arr[j]:
                        self.array[k] = left_arr[i]
                        i += 1
                    else:
                        self.array[k] = right_arr[j]
                        j += 1
                    self.draw_bars(swap=[k])
                    k += 1
                    self.root.after(self.speed, merge_step)
                elif i < len(left_arr):
                    self.array[k] = left_arr[i]
                    self.draw_bars(swap=[k])
                    i += 1
                    k += 1
                    self.root.after(self.speed, merge_step)
                elif j < len(right_arr):
                    self.array[k] = right_arr[j]
                    self.draw_bars(swap=[k])
                    j += 1
                    k += 1
                    self.root.after(self.speed, merge_step)

            merge_step()

        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            merge(left, mid, right)

    def quick_sort(self, low, high):
        def partition(l, h, callback):
            pivot = self.array[h]
            i = l - 1

            def partition_step(j):
                nonlocal i
                if j < h:
                    self.draw_bars(compare=[j, h])
                    if self.array[j] <= pivot:
                        i += 1
                        self.array[i], self.array[j] = self.array[j], self.array[i]
                        self.draw_bars(swap=[i, j])
                    self.root.after(self.speed, lambda: partition_step(j + 1))
                else:
                    self.array[i + 1], self.array[h] = self.array[h], self.array[i + 1]
                    self.draw_bars(swap=[i + 1, h])
                    callback(i + 1)

            partition_step(l)

        def quicksort_step(l, h):
            if l < h:
                def after_partition(pi):
                    self.draw_bars(sorted_indices=[pi])
                    quicksort_step(l, pi - 1)
                    quicksort_step(pi + 1, h)
                partition(l, h, after_partition)

        quicksort_step(low, high)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()













# import tkinter as tk
# from tkinter import ttk
# import random

# class SortingVisualizer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sorting Algorithm Visualizer")
#         self.array = []
#         self.canvas_width = 800
#         self.canvas_height = 400
#         self.bar_width = 0
#         self.speed = 50  # Animation speed in ms
#         self.is_sorting = False
        
#         # Setup GUI
#         self.setup_gui()
#         self.generate_array()

#     def setup_gui(self):
#         # Control Frame
#         control_frame = ttk.Frame(self.root)
#         control_frame.pack(pady=10)

#         # Algorithm Selection
#         ttk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
#         self.algo_var = tk.StringVar(value="Bubble Sort")
#         algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
#         algo_menu = ttk.Combobox(control_frame, textvariable=self.algo_var, values=algorithms, state="readonly")
#         algo_menu.pack(side=tk.LEFT, padx=5)

#         # Buttons
#         ttk.Button(control_frame, text="Generate New Array", command=self.generate_array).pack(side=tk.LEFT, padx=5)
#         ttk.Button(control_frame, text="Start Sorting", command=self.start_sorting).pack(side=tk.LEFT, padx=5)

#         # Speed Scale
#         ttk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=5)
#         self.speed_scale = ttk.Scale(control_frame, from_=10, to=200, orient=tk.HORIZONTAL, command=self.update_speed)
#         self.speed_scale.set(self.speed)
#         self.speed_scale.pack(side=tk.LEFT, padx=5)

#         # Canvas for visualization
#         self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
#         self.canvas.pack(pady=10)

#     def update_speed(self, value):
#         self.speed = int(float(value))

#     def generate_array(self):
#         if not self.is_sorting:
#             self.array = [random.randint(10, 300) for _ in range(30)]
#             self.draw_bars()

#     def draw_bars(self, compare=None, swap=None, sorted_indices=None):
#         self.canvas.delete("all")
#         self.bar_width = self.canvas_width // len(self.array)
#         sorted_indices = sorted_indices or []

#         for i, height in enumerate(self.array):
#             x0 = i * self.bar_width
#             y0 = self.canvas_height
#             x1 = (i + 1) * self.bar_width
#             y1 = self.canvas_height - height

#             color = "blue"  # Default color
#             if i in sorted_indices:
#                 color = "green"  # Sorted
#             elif compare and i in compare:
#                 color = "red"  # Comparing
#             elif swap and i in swap:
#                 color = "yellow"  # Swapping

#             self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
#             # Add text label below each bar
#             text_x = (x0 + x1) / 2  # Center the text under the bar
#             text_y = self.canvas_height + 10  # Position below the bar
#             self.canvas.create_text(text_x, text_y, text=str(height), font=("Arial", 8), fill="black")

#     def start_sorting(self):
#         if not self.is_sorting:
#             self.is_sorting = True
#             algo = self.algo_var.get()
#             if algo == "Bubble Sort":
#                 self.bubble_sort()
#             elif algo == "Selection Sort":
#                 self.selection_sort()
#             elif algo == "Insertion Sort":
#                 self.insertion_sort()
#             elif algo == "Merge Sort":
#                 self.merge_sort(0, len(self.array) - 1)
#             elif algo == "Quick Sort":
#                 self.quick_sort(0, len(self.array) - 1)
#             self.root.after(self.speed * 10, self.stop_sorting)

#     def stop_sorting(self):
#         self.is_sorting = False
#         self.draw_bars(sorted_indices=list(range(len(self.array))))

#     def bubble_sort(self):
#         def step(i, j):
#             if i < len(self.array) - 1:
#                 if j < len(self.array) - i - 1:
#                     self.draw_bars(compare=[j, j + 1])
#                     if self.array[j] > self.array[j + 1]:
#                         self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
#                         self.draw_bars(swap=[j, j + 1])
#                     self.root.after(self.speed, lambda: step(i, j + 1))
#                 else:
#                     self.draw_bars(sorted_indices=[len(self.array) - i - 1])
#                     self.root.after(self.speed, lambda: step(i + 1, 0))
#         step(0, 0)

#     def selection_sort(self):
#         def step(i, j, min_idx):
#             if i < len(self.array) - 1:
#                 if j < len(self.array):
#                     self.draw_bars(compare=[j, min_idx])
#                     if self.array[j] < self.array[min_idx]:
#                         min_idx = j
#                     self.root.after(self.speed, lambda: step(i, j + 1, min_idx))
#                 else:
#                     self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
#                     self.draw_bars(swap=[i, min_idx], sorted_indices=[i])
#                     self.root.after(self.speed, lambda: step(i + 1, i + 2, i + 1))
#         step(0, 1, 0)

#     def insertion_sort(self):
#         def step(i, j, key):
#             if i < len(self.array):
#                 if j >= 0 and self.array[j] > key:
#                     self.draw_bars(compare=[j, j + 1])
#                     self.array[j + 1] = self.array[j]
#                     self.draw_bars(swap=[j, j + 1])
#                     self.root.after(self.speed, lambda: step(i, j - 1, key))
#                 else:
#                     self.array[j + 1] = key
#                     self.draw_bars(sorted_indices=[k for k in range(i + 1)])
#                     self.root.after(self.speed, lambda: step(i + 1, i, self.array[i + 1] if i + 1 < len(self.array) else None))
#         if len(self.array) > 1:
#             step(1, 0, self.array[1])

#     def merge_sort(self, left, right):
#         def merge(l, m, r):
#             left_arr = self.array[l:m + 1]
#             right_arr = self.array[m + 1:r + 1]
#             i = j = 0
#             k = l

#             def merge_step():
#                 nonlocal i, j, k
#                 if i < len(left_arr) and j < len(right_arr):
#                     self.draw_bars(compare=[l + i, m + 1 + j])
#                     if left_arr[i] <= right_arr[j]:
#                         self.array[k] = left_arr[i]
#                         i += 1
#                     else:
#                         self.array[k] = right_arr[j]
#                         j += 1
#                     self.draw_bars(swap=[k])
#                     k += 1
#                     self.root.after(self.speed, merge_step)
#                 elif i < len(left_arr):
#                     self.array[k] = left_arr[i]
#                     self.draw_bars(swap=[k])
#                     i += 1
#                     k += 1
#                     self.root.after(self.speed, merge_step)
#                 elif j < len(right_arr):
#                     self.array[k] = right_arr[j]
#                     self.draw_bars(swap=[k])
#                     j += 1
#                     k += 1
#                     self.root.after(self.speed, merge_step)

#             merge_step()

#         if left < right:
#             mid = (left + right) // 2
#             self.merge_sort(left, mid)
#             self.merge_sort(mid + 1, right)
#             merge(left, mid, right)

#     def quick_sort(self, low, high):
#         def partition(l, h, callback):
#             pivot = self.array[h]
#             i = l - 1

#             def partition_step(j):
#                 nonlocal i
#                 if j < h:
#                     self.draw_bars(compare=[j, h])
#                     if self.array[j] <= pivot:
#                         i += 1
#                         self.array[i], self.array[j] = self.array[j], self.array[i]
#                         self.draw_bars(swap=[i, j])
#                     self.root.after(self.speed, lambda: partition_step(j + 1))
#                 else:
#                     self.array[i + 1], self.array[h] = self.array[h], self.array[i + 1]
#                     self.draw_bars(swap=[i + 1, h])
#                     callback(i + 1)

#             partition_step(l)

#         def quicksort_step(l, h):
#             if l < h:
#                 def after_partition(pi):
#                     self.draw_bars(sorted_indices=[pi])
#                     quicksort_step(l, pi - 1)
#                     quicksort_step(pi + 1, h)
#                 partition(l, h, after_partition)

#         quicksort_step(low, high)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SortingVisualizer(root)
#     root.mainloop()