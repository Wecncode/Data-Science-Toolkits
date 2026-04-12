import time
import random
import numpy as np

def generate_python_matrix(size):
    """Generates a 2D matrix using nested Python lists."""
    return [[random.random() for _ in range(size)] for _ in range(size)]

def multiply_python_lists(mat_a, mat_b, size):
    """Multiplies two matrices using pure Python O(N^3) logic."""
    # Create an empty matrix for the result
    result = [[0.0 for _ in range(size)] for _ in range(size)]
    
    start_time = time.time()
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    end_time = time.time()
    
    return end_time - start_time

def multiply_numpy_arrays(mat_a, mat_b):
    """Multiplies two matrices using NumPy's optimized C-backend."""
    start_time = time.time()
    # The @ operator performs matrix multiplication in NumPy
    result = mat_a @ mat_b 
    end_time = time.time()
    
    return end_time - start_time

if __name__ == "__main__":
    # 500x500 is large enough to make Python crawl, but fast enough to not crash.
    MATRIX_SIZE = 500 
    
    print(f"Generating {MATRIX_SIZE}x{MATRIX_SIZE} matrices...")
    py_matrix_a = generate_python_matrix(MATRIX_SIZE)
    py_matrix_b = generate_python_matrix(MATRIX_SIZE)
    
    np_matrix_a = np.array(py_matrix_a)
    np_matrix_b = np.array(py_matrix_b)
    
    print("\nRunning Native Python Multiplication (This will take a few seconds)...")
    py_time = multiply_python_lists(py_matrix_a, py_matrix_b, MATRIX_SIZE)
    print(f"Python Time: {py_time:.4f} seconds")
    
    print("\nRunning NumPy Vectorized Multiplication...")
    np_time = multiply_numpy_arrays(np_matrix_a, np_matrix_b)
    print(f"NumPy Time: {np_time:.6f} seconds")
    
    print(f"\n🚀 NumPy was {py_time / np_time:.0f}x faster.")
