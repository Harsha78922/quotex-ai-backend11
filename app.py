
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import json

model = tf.keras.models.load_model("quotex_signal_model.h5")

app = Flask(__name__)

@app.route("/")
def home():
    return "Quotex AI Backend is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_data = np.array(data["input"]).reshape(1, 50, 5)
        prediction = model.predict(input_data)[0]
        signal = "buy" if prediction[0] > 0.5 else "sell"
        return jsonify({
            "signal": signal,
            "confidence": float(prediction[0] if signal == "buy" else 1 - prediction[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
