#My take on a A1Z26 or numeric substituion cipher

#Menu
print("1. Decode from numbers to text\n2. Encode text to numbers\n")

selection = int(input())

if (selection==1):
    numbers = input("Type the numbers you want to decode. Example: 8 5 12 12 15. \n")
    numberList = numbers.split()
    for number in numberList:
        result = chr(int(number) + 64)
        print(result, end='')
elif (selection==2):
    word = input("Type the word you want to encode. Example: hello \n").upper()
    for letter in word:
        result = ord(letter) - 64
        print(result, end=' ')
else: print("Not a valid selection.")