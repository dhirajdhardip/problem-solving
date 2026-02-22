def to_LowerString(str):
    result =""

    for char in str :

        if 'A'<= char <= 'Z' :
            result += chr(ord (char)+ 32) 

        else:
            result += char

    return result

str = input("Enter the name or sentance: ")

print(to_LowerString(str))
