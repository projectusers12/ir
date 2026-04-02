def soundex(word):
    if not word:
        return ""
        
    word = word.upper()
    code = word[0]
    
    # Dictionaries are great for IDLE - clean and easy to read
    mappings = {
        'BFPV': '1', 
        'CGJKQSXZ': '2', 
        'DT': '3',
        'L': '4', 
        'MN': '5', 
        'R': '6'
    }
    
    prev_digit = ""
    
    for char in word[1:]:
        digit = ""
        
        # Look up the character in the dictionary
        for group, val in mappings.items():
            if char in group:
                digit = val
                break
                
        # Apply the Soundex rules
        if digit != "":
            if digit != prev_digit:
                code += digit
            prev_digit = digit
        elif char in "AEIOUYHW":
            prev_digit = ""  # Reset memory if a vowel separates sounds
            
        # Stop processing early if we already have 4 characters
        if len(code) == 4:
            break
            
    # Pad with zeros and slice to exactly 4 characters
    return (code + "000")[:4]

# Example usage
print(soundex("Robert"))   # R163
print(soundex("Rupert"))   # R163
print(soundex("Ruia"))     # R000
print(soundex("Herman"))   # H655
print(soundex("Hermann"))  # H655
