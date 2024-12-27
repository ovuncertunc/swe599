from flask import Flask, request, jsonify
import numpy as np
import time
import multiprocessing

app = Flask(__name__)

def heavy_computation(input_data):
    # Simulate a computationally heavy task
    for _ in range(1000000):
        input_data = np.sqrt(input_data ** 2 + 1)
    return input_data

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse input JSON for data
        data = request.json
        if not data or "input" not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Simulate inference workload
        input_data = np.array(data["input"]).astype(np.float32)
        pool = multiprocessing.Pool(processes=4)  # Use multiple processes
        results = pool.map(heavy_computation, [input_data for _ in range(4)])
        pool.close()
        pool.join()

        # Generate dummy predictions
        predictions = [np.sum(result) for result in results]

        return jsonify({"predictions": predictions}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
