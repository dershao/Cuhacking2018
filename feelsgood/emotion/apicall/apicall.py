import indicoio
import apikey

# api key
indicoio.config.api_key = apikey.api_key

# calling the api and return the result as a string
def getEmotion(image):
    return getMax(indicoio.fer(image))

# get the emotion
def getMax(emotions):
    max = 0
    emotion = ''

    for key, value in emotions.items():
        if value >= max:
            max = value
            emotion = key

    return emotion
