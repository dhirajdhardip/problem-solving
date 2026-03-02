def compressed_string(s):

    result =[]

    count = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1

        else:
            result.append(s[i-1] + str(count))
            count = 1

    result.append(s[-1] + str(count))

    compressed_string =''.join(result)


    if len(compressed_string) < len(s):
        return compressed_string
    
    else:
        return s
    

s = input("Enter the string name: ")
print(compressed_string(s))
