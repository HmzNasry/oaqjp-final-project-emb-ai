"""
Flask server for Emotion Detection application.

This module sets up a web server using Flask to analyze text for emotional content.
It provides an endpoint for users to submit text and receive detected emotions.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotional_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home() -> str:
    """
    Renders the home page of the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Handles emotion detection requests.

    Retrieves user input text from query parameters, calls the `emotion_detector` function,
    and returns the detected emotions or an error message.

    Returns:
        flask.Response: JSON response containing the detected emotions or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)
    dominant_emotion = result.pop("dominant_emotion")

    if dominant_emotion is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = {
        "message": f"For the given statement, the system response is {result}.",
        "dominant_emotion": dominant_emotion
    }

    return jsonify(response_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
