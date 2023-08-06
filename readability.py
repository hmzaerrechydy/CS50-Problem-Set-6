text = input("Text: ")

words = 0 
letters = 0 
sentences = 0 

for word in text.split(): 
    words += 1
    for letter in word:  
        if letter.isalpha(): 
            letters += 1
        if letter in [".", "?", "!"]: 
            sentences += 1

L = letters / words * 100
S = sentences / words * 100 

index = 0.0588 * L - 0.296 * S - 15.8

if index > 16: 
    print("Grade 16+")
elif index < 1: 
    print("Before Grade 1")
else: 
    print("Grade: ", round(index))