import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# 1. Read the raw text from the first file
with open('pre.txt', 'r') as file1:
    words = file1.read().split() # .split() chops it into words using spaces

# 2. Filter the words and write them to the new file
with open('to_write_data.txt', 'w') as file2:
    for w in words:
        if w.casefold() not in stop_words:
            file2.write(w + " ") # Write the word and add a space after it
            
print("Stop words removed and saved to new file successfully!")
