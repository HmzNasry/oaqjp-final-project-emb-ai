from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  

app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    result = emotion_detector(text_to_analyze)  
    dominant_emotion = result.pop("dominant_emotion") 
    
    response_text = f"For the given statement, the system response is {result}. The dominant emotion is {dominant_emotion}."
    
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
