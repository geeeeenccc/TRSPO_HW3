import time
import itertools
import concurrent.futures


# Function to calculate the Collatz step for a given number
def collatz_func(num):
    new_num = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        new_num += 1
    return new_num


def main(n, num_threads):
    """ n - number of numbers to calculate the gradient for
        num_threads - number of threads to use for parallelization"""

    start_time = time.time()

    # List of numbers to calculate gradients for
    numbers = list(range(1, n + 1))

    # Calculate the gradient for each number
    def worker(start, end):
        total_steps = 0
        for number in itertools.islice(numbers, start, end):
            total_steps += collatz_func(number)
        return total_steps

    chunk_size = n // num_threads
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads)]

    # Calculate the gradient for each chunk in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(lambda chunk: worker(*chunk), chunks))

    # Calculate the mean gradient from the results
    mean_gradient = sum(results) / n

    print("Середня кількість кроків:", mean_gradient)
    print("Час виконання:", time.time() - start_time)


if __name__ == "__main__":
    n_nums = 10000
    num_threads = 10
    main(n_nums, num_threads)
