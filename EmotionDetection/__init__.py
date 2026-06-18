import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.text

    if response=status_code==200:
        formatted_responde=json.loads(response.text)
        emotion_predictions=formatted_responde['emotionPredictions'][0]['emotion']
        anger_score= emotion_predictions['anger']
        disgust_score= emotion_predictions['disgust']
        fear_score= emotion_predictions['fear']
        joy_score= emotion_predictions['joy']
        sadness_score= emotion_predictions['sadness']

        dictionary={
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': '<name of the dominant emotion>'
            }
            dominant_emotion=max(dictionary,key=dictionary.get)
            out={
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': '<name of the dominant emotion>'
                }
         return out 
    else:
        return "error"

