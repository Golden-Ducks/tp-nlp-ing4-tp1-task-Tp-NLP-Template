import re

from matplotlib import text

def Text_cleaning():
    print("Text Cleaning : ")
    print("Task 1 : ")
    with open("task1.txt", "r",encoding="utf-8") as f:
        text = f.read()

    text = text.lower()

    text = re.sub(r'\d+', '', text)

    text = re.sub(r'[^\w\s]', '', text)

    symbols_list = ['@', '#', '$', '%', '&', '*', '_', '–', '—']

    for symbol in symbols_list:
        text = text.replace(symbol, '')


    text = re.sub(r'\s+', ' ', text).strip()

    print(text)
    print("Question  : ")
    sentence = "He scored 88% and %% won the 1%st and 2nd game"


    sentence = re.sub(r'(?<!\d)%', '', sentence)

    sentence = re.sub(r'(\d+)%([a-zA-Z]+)', r'\1\2', sentence)

    sentence = re.sub(r'%{2,}', '', sentence)

    sentence = re.sub(r'\s+', ' ', sentence).strip()

    print(sentence)

    
def text_normalization():

    print("Text Normalization : ")
    print("Task 1 : ")
    text = "Wow!! This cow ran fast & ate 3 apples."

    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    number_map = {
    "0": "zero", "1": "one", "2": "two", "3": "three",
    "4": "four", "5": "five", "6": "six",
    "7": "seven", "8": "eight", "9": "nine"
    }

    for digit, word in number_map.items():
        text = re.sub(r'\b' + digit + r'\b', word, text)

    print(text)
   
    text = "I'm sure the cow will stop the ducks from fighting soon!!."

    contractions = {
        "I'm": "I am",
    }

    for short, full in contractions.items():
        text = text.replace(short, full)

    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    print(text)
    
    print("Task 2 : ")
    
    with open("task2.txt", "r", encoding="utf-8") as f:
        text = f.read()

    number_map = {
    "0": "zero", "1": "one", "2": "two", "3": "three",
    "4": "four", "5": "five", "6": "six",
    "7": "seven", "8": "eight", "9": "nine"
    }

    for digit, word in number_map.items():
        text = re.sub(r'\b' + digit + r'\b', word, text)

    contractions = {
    "I'm": "I am",
    "I'm": "I am",
    "I'll": "I will",
    "I've": "I have",
    "don't": "do not",
    "didn't": "did not",
    "wasn't": "was not",
    "isn't": "is not",
    "can't": "cannot",
    "won't": "will not",
    "it's": "it is",
    "It's": "It is",
    "that's": "that is",
    "let's": "let us",
    "she's": "she is",
    "he's": "he is"
    }

    for short, full in contractions.items():
        text = text.replace(short, full)


    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    print(text[:1000]) 


def text_tokenization():
        print("Text Tokenization : ")
        text = "I love luna !"
        tokens = text.split()
        print(tokens)


Text_cleaning()
text_normalization()
text_tokenization()
