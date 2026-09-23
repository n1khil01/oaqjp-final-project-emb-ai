import requests
import json

def emotion_detector(text_to_analyze):
    request_body = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        json=request_body
    )

    response_data = json.loads(response.text)

    emotion = response_data["emotionPredictions"][0]["emotion"]

    emotion_scores = {
        "anger": emotion["anger"],
        "disgust": emotion["disgust"],
        "fear": emotion["fear"],
        "joy": emotion["joy"],
        "sadness": emotion["sadness"],
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores

if __name__ == "__main__":
    result = emotion_detector("I am so glad this happened today")
    for key, value in result.items():
        print(f"{key}: {value}")
