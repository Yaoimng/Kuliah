def abjad(n,m):
    result = ""
    for char in n:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset+m) % 26 + offset)
        else:
            result += char
    return result

n = input()
m = int(input())

result = abjad(n,m)

print (result)