import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    # Send the POST request
    response = requests.post(url, headers=headers, json=payload)
    
        # Check the status code
    if response.status_code == 400:
        # Return dictionary with all values None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert the response text into a dictionary
    data = json.loads(response.text)
    
    # Extract the emotion scores
    overall_emotion = data["emotionPredictions"][0]["emotion"]
    
    # Find the dominant emotion
    dominant_emotion = max(overall_emotion, key=overall_emotion.get)
    
    # Prepare the output format
    result = {
        'anger': overall_emotion['anger'],
        'disgust': overall_emotion['disgust'],
        'fear': overall_emotion['fear'],
        'joy': overall_emotion['joy'],
        'sadness': overall_emotion['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result
