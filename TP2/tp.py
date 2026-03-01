D1 = "feel good."
D2 = "feel better thank"
D3 = "happened good"

def clean(text):
    text = text.lower()
    
    ponctuation = "!?.,'"
    for c in ponctuation:
        text = text.replace(c, "")
    
    mots = text.split()
    
    return mots

D1_c = clean(D1)
D2_c = clean(D2)
D3_c = clean(D3)

print("D1 =", D1_c)  
print("D2 =", D2_c)  
print("D3 =", D3_c) 
print()

vocab = []
for doc in [D1_c, D2_c, D3_c]:
    for mot in doc:
        if mot not in vocab:
            vocab.append(mot)

print("Vocabulaire =", vocab)
print()

def vect(doc, vocab):
    v = []
    for mot in vocab:
        if mot in doc:
            v.append(1)
        else:
            v.append(0)
    return v

print("D1 →", vect(D1_c, vocab))
print("D2 →", vect(D2_c, vocab))
print("D3 →", vect(D3_c, vocab))