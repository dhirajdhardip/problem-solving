text =input("Enter the string do you want: ")
words =[]
i = 0

while i < len(text):

    while i<len(text) and text[i] == ' ':
        i += 1

    if i == len(text):
            break
    j = i
    while j < len(text) and text[j] != ' ':
     j += 1
    words.append(text[i:j])
    i = j

left, right = 0, len(words)-1
while left < right :
    words[left], words[right] = words[right], words[left]
    left += 1
    right -= 1

result= " "
for char in range(len(words)):
    if char > 0:
       result+= " "
    result += words[char]

print(result)
