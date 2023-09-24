import threading
import time


# func to calculate the Collatz gradient for a given number
def gradient(num):
    new_num = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        new_num += 1
    return new_num


def main(n, num_threads):
    start_time = time.time()

    # list of numbers to calculate gradients for
    numbers = list(range(1, n + 1))

    threads = []  # List to hold thread objects
    results = []  # List to store results from each thread

    for i in range(num_threads):
        # Divide the work among threads
        start_idx = i * (n // num_threads)
        end_idx = (i + 1) * (n // num_threads)
        thread_numbers = numbers[start_idx:end_idx]

        # Create a thread for each range of numbers
        thread = threading.Thread(target=lambda nums: results.extend([gradient(num) for num in nums]),
                                  args=(thread_numbers,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Calculate the mean gradient from the results
    mean_gradient = sum(results) / len(results)

    print("Середня кількість кроків:", mean_gradient)
    print("Час виконання:", time.time() - start_time)


if __name__ == "__main__":
    n_nums = 600000
    num_threads = 4
    main(n_nums, num_threads)
