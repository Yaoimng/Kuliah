def abjad():
    abjad = "abcdefghijklmnopqrstuvwxyz"
    kacau = str(input())
    n = int(input())
    kata = input()
    result = ""
    for char in kata:
        if char == " ":
            result += " "
        else:
            index = abjad.index(char)
            if index >= len(abjad):
                index -= len(abjad)
            result += kacau[index]
    print(result)
        
abjad()
# textcase
#   bcdefghijklmnopqrstuvwxyza 
#   cdbefghijklmnopqrstuvwxyza