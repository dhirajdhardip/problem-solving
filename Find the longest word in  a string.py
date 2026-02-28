def longest_Words(str):

    words = str.split()

    longest =""

    for word in words:
       if len(word) > len(longest):
           longest = word

    return longest

print(longest_Words("I love python programing"))
