import numpy as np


try:
    # In-memory storage with a fixed size
    MAX_STORAGE_SIZE = 100
    
    matrix_storage = []
    
    while True:
        a = np.random.rand(500, 500)
        b = np.random.rand(500, 500)

        # Perform matrix multiplication
        result = np.dot(a, b)

        # Manage memory: Remove oldest matrix if limit is reached
        if len(matrix_storage) >= MAX_STORAGE_SIZE:
            matrix_storage.pop(0)  # Remove the oldest entry

        # Store the new result
        matrix_storage.append(result)

        # Calculate a summary of the result
        result_summary = {
            "sum": float(result.sum()),
            "mean": float(result.mean()),
            "max": float(result.max()),
            "min": float(result.min())
        }

        print(result_summary)

except MemoryError:
    print("Memory limit reached! Free up resources.")