Put your TP1 solution here
# Documents
D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."

# Dictionary for number conversion
number_map = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

def normalize(text):
    # Step 1: Lowercasing
    text = text.lower()
    
    # Step 2: Convert numbers to words
    words = text.split()
    new_words = []
    
    for word in words:
        # نحي العلامات من الرقم باش نعرفو
        clean_word = word.strip(".,!?")
        
        if clean_word in number_map:
            word = word.replace(clean_word, number_map[clean_word])
        
        new_words.append(word)
    
    return " ".join(new_words)

# Apply normalization
print("D1:", normalize(D1))
print("D2:", normalize(D2))
print("D3:", normalize(D3))
print("D4:", normalize(D4))
