s = 'y2b2'
res = ''
for i in range(0, len(s), 2):
    char = s[i]
    times = int(s[i + 1])
    
    # Calculate the new character, wrapping around within 'a' to 'z'
    new_char = chr((ord(char) - ord('a') + times) % 26 + ord('a'))
    res += new_char
print(res)
