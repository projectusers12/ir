def editdist(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
        
    if str1[m-1] == str2[n-1]:
        return editdist(str1, str2, m-1, n-1)
        
    return 1 + min(
        editdist(str1, str2, m, n-1),    # Insert
        editdist(str1, str2, m-1, n),    # Remove
        editdist(str1, str2, m-1, n-1)   # Replace
    )

# --- Execution ---
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print("Edit Distance is:", editdist(str1, str2, len(str1), len(str2)))
