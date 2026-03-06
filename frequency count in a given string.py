
def frequency_string(s):

    frequency_count ={}

    for ch in s:
        if s in frequency_count:
            frequency_count[ch] += 1

        else:
            frequency_count[ch] = 1

    return frequency_count

s = input("Enterr the string")

print(frequency_string(s))
