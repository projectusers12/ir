import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


with open('pre.txt', 'r') as file1:
    words = file1.read().split() 

# 2. Filter the words and write them to the new file
with open('to_write_data.txt', 'w') as file2:
    for w in words:
        if w.casefold() not in stop_words:
            file2.write(w + " ")
            
print("Stop words removed and saved to new file successfully!")
