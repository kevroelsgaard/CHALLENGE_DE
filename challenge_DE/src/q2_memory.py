import json
from collections import Counter
import emoji

#extraigo emojis para hacer una lista de todos los diferentes emojis presentes 
def extract_emojis(text: str):
    return [char for char in text if char in emoji.EMOJI_DATA]

def q2_memory(file_path: str):
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as archivo:
        #por cada content me fijo que emoji esta presente e incremento su count en 1
        for linea in archivo:
            tweet = json.loads(linea)
            emojis = extract_emojis(tweet['content'])
            emoji_counter.update(emojis)

    #devuelvo los 10 emojis con mas apariciones
    return emoji_counter.most_common(10) 