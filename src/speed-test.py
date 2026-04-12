"""Lecture Demonstration: Why we use NumPy instead of Python lists."""

import time
import numpy as np

def python_lists(size):
    """Multiplies two arrays using standard Python lists and loops."""
    list_a = list(range(size))
    list_b = list(range(size))
    result = []
    
    start_time = time.time()
    for i in range(size):
        result.append(list_a[i] * list_b[i])
    end_time = time.time()
    
    print(f"Python Native Time: {end_time - start_time:.5f} seconds")

def numpy_arrays(size):
    """Multiplies two arrays using vectorized NumPy C-bindings."""
    arr_a = np.arange(size)
    arr_b = np.arange(size)
    
    start_time = time.time()
    result = arr_a * arr_b  # Vectorized operation
    end_time = time.time()
    
    print(f"NumPy Vectorized Time: {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    SIZE = 10_000_000
    print(f"Testing element-wise multiplication of {SIZE} items...")
    python_lists(SIZE)
    numpy_arrays(SIZE)
