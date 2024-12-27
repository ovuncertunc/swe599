from flask import Flask, jsonify
import numpy as np

# Create Flask app
app = Flask(__name__)

# In-memory storage with a fixed size
MAX_STORAGE_SIZE = 100  # Limit to 100 matrices
matrix_storage = []

@app.route('/matrix-multiply', methods=['GET'])
def matrix_multiply():
    """Endpoint to perform matrix multiplication and manage memory usage."""
    try:
        # Generate two random 10000x10000 matrices
        a = np.random.rand(10000, 10000)
        b = np.random.rand(10000, 10000)

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

        # Return the response
        return jsonify({
            "status": "success",
            "result_summary": result_summary,
            "stored_matrices": len(matrix_storage)
        }), 200

    except MemoryError:
        return jsonify({
            "status": "error",
            "message": "Memory limit reached! Free up resources."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)