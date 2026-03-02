def find_permutations(s):

    if len(s) == 1:
        return [s]
    
    permutations =[]

    for i in range(len(s)):
        current_char =s[i]
        remaining_char =s[:i] + s[i+1:]
        remaining_permutations = find_permutations(remaining_char)

        for p in remaining_permutations:
            permutations.append(current_char + p)


    return permutations

print(find_permutations('abc'))
