def decrypt(text, shift):
    result = ""
    for i in text:
        shiftedCode = ord(i) - shift
        if shiftedCode < 65:
            shiftedCode += 26
        result += chr(shiftedCode)
    return result

for i in range(26):
    print("Shift " + str(i).ljust(2) +  " :" + decrypt("BSUOFODSBUVOGWZAWBMOY", i))