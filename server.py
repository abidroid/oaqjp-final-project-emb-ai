"""
This module defines a Flask web server for emotion detection.
It provides endpoints to analyze text for emotions and returns the
dominant emotion and associated emotion scores.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page of the web application.

    Returns:
        str: The rendered index.html template.
    """
    # This will serve the provided index.html file from the templates folder
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """
    Handle POST requests to detect emotions in the provided text.

    Returns:
        str: A formatted response string indicating the detected emotions 
        or an error message if the input is invalid.
    """
    # Retrieve the user input from the form

    # If GET, retrieve text from query params
    if request.method == 'GET':
        text = request.args.get('textToAnalyze')
    else:
        # For POST requests, retrieve text from form data
        text = request.form.get('statement')
    #text = request.form.get('statement')

    # Analyze the text using the emotion_detector function
    result = emotion_detector(text)

    # Check if dominant_emotion is None, which indicates an invalid input scenario
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores
    anger_score = result['anger']
    disgust_score = result['disgust']
    fear_score = result['fear']
    joy_score = result['joy']
    sadness_score = result['sadness']
    dominant_emotion = result['dominant_emotion']

    # Format the response as requested
    response_str = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

    return response_str

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
