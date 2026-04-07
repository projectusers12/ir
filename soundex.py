def soundex(word):
    if not word:
        return ""
        
    word = word.upper()
    code = word[0]
    
    
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
        
        
        for group, val in mappings.items():
            if char in group:
                digit = val
                break
                
        
        if digit != "":
            if digit != prev_digit:
                code += digit
            prev_digit = digit
        elif char in "AEIOUYHW":
            prev_digit = "" 
            
        
        if len(code) == 4:
            break
            
    
    return (code + "000")[:4]


print(soundex("Robert"))  

