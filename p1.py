plays = {
    "Anthony and Cleopatra": "Anthony is there brutus is with Ceaser is with Cleopatra mercy worser",
    "Julius Ceaser":"Anthony is there, Brutus is Caeser is but Calpurnia is.",
    "The Tempest":"mercy worser",
    "Hamlet": "I did enact Julius Caeser Brutus killed me"
}
words = ["Anthony", "Brutus", "Caeser", "Philippi"]

# 1. Build Bit Vectors Directly (No 2D Matrix needed!)
vector_dict = {}
for w in words:
    bit_str = ""
    for text in plays.values():
        if w.lower() in text.lower():
            bit_str += "1"
        else:
            bit_str += "0"
            
    vector_dict[w] = int(bit_str, 2) # Instantly convert "10" to base-2 integer

print("Bit Vectors:", vector_dict)

# 2. Take Query and Swap Words for Numbers
query = input("\nEnter condition ")
eval_query = query
for w in words:
    eval_query = eval_query.replace(w, str(vector_dict[w]))

# 3. Calculate and Decode Result
res_int = eval(eval_query)

# Convert integer back to binary, remove '0b', and pad with zeros
res_bin = bin(res_int)[2:].zfill(len(plays)) 

print(f"Binary Result: {res_bin}")

# 4. Print the matching plays
play_names = list(plays.keys())
for i in range(len(res_bin)):
    if res_bin[i] == '1':
        print("→ Match found in:", play_names[i])

# & | ~
