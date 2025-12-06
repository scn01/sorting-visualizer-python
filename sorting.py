import time
import os
import random

# Clear screen based on OS
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Visualise array as bars
def visualize(arr, highlight_indices=[]):
    clear()
    for i, val in enumerate(arr):
        bar = "█" * val
        if i in highlight_indices:
            print(f"\033[92m{bar}\033[0m")  # Green highlighted
        else:
            print(bar)
    time.sleep(0.1)

# Bubble Sort Visualizer
def bubble_sort_visualize(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            visualize(arr, [j, j + 1])

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(arr, [j, j + 1])

    visualize(arr)

# Insertion Sort Visualizer
def insertion_sort_visualize(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            visualize(arr, [j, j + 1])
            j -= 1

        arr[j + 1] = key
        visualize(arr, [j + 1])

# Main Program
if __name__ == "__main__":
    size = 15
    arr = [random.randint(1, 30) for _ in range(size)]

    print("Choose Algorithm:\n1. Bubble Sort\n2. Insertion Sort")
    choice = input("Enter choice: ")

    if choice == "1":
        bubble_sort_visualize(arr)
    elif choice == "2":
        insertion_sort_visualize(arr)
    else:
        print("Invalid choice!")