def weighted_editdist(str1, str2, m, n):
    # If one string is empty, cost is length * insert/remove weight (assuming 1)
    if m == 0: return n * 1  
    if n == 0: return m * 1  

    if str1[m-1] == str2[n-1]:
        return weighted_editdist(str1, str2, m-1, n-1)

   
    insert_cost = 1
    remove_cost = 1
    replace_cost = 2  # Making replace more expensive

    return min(
        weighted_editdist(str1, str2, m, n-1) + insert_cost,   # Insert
        weighted_editdist(str1, str2, m-1, n) + remove_cost,   # Remove
        weighted_editdist(str1, str2, m-1, n-1) + replace_cost # Replace
    )


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print("Weighted Edit Distance is:", weighted_editdist(str1, str2, len(str1), len(str2)))
