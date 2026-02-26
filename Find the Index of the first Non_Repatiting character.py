def first_non_repeating_char(str):

    char_count ={}

    for char in str :

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char]=1

    for i in range(len(str)):
        if char_count[str[i]]==1:
            return i
    return -1

print(first_non_repeating_char("swiss"))
