import requests
import json

def emotion_detector(text_to_analyse):  
    if not text_to_analyse: 
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    extracted_emotions = {key: emotions[key] for key in emotions}
    dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
    extracted_emotions["dominant_emotion"] = dominant_emotion
    
    return extracted_emotions
