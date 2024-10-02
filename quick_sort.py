import random
import time
import matplotlib.pyplot as plt
import sys


# Random pivot quicksort
def quicksort_randomchoice(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr.remove(pivot)
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_randomchoice(left) + [pivot] + quicksort_randomchoice(right)

# Non-random pivot quicksort with median-of-three pivot selection
def quicksort_nonrandomchoice(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    pivot = sorted([arr[0], arr[mid], arr[-1]])[1]  # Median of first, middle, and last elements

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    return quicksort_nonrandomchoice(left) + equal + quicksort_nonrandomchoice(right)




def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time


def generate_best_case(n):
    return list(range(n))


def generate_worst_case(n):
    return list(range(n, 0, -1))


def generate_average_case(n):
    return [random.randint(1, 10000) for _ in range(n)]


def benchmark_quicksort(sort_func, sizes):
    best_times, worst_times, avg_times = [], [], []

    for n in sizes:
        # Best case
        best_case = generate_best_case(n)
        best_times.append(measure_time(sort_func, best_case))

        # Worst case
        worst_case = generate_worst_case(n)
        worst_times.append(measure_time(sort_func, worst_case))

        # Average case
        avg_case = generate_average_case(n)
        avg_times.append(measure_time(sort_func, avg_case))

    return best_times, worst_times, avg_times



def plot_results(sizes, best_times, worst_times, avg_times):
    plt.plot(sizes, best_times, label='Best Case')
    plt.plot(sizes, worst_times, label='Worst Case')
    plt.plot(sizes, avg_times, label='Average Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Non-Random Pivot Performance')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    best_times, worst_times, avg_times = benchmark_quicksort(quicksort_nonrandomchoice, sizes)
    plot_results(sizes, best_times, worst_times, avg_times)