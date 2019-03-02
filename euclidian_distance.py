import math

def get_vector(word):
    """using ord()"""
    text=[]
    for char in word:
        text.append(ord(char))
    return text

def euclidean_distance(x, y):
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

word1="Male"
word2="Male"
word3="Female"
v1=get_vector(word1)
v2=get_vector(word2)
v3=get_vector(word3)
print("euclidean distance: "+str(euclidean_distance(v1,v2)))
print("euclidean distance: "+str(euclidean_distance(v1,v3)))
