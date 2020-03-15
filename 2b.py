def rev(str1):
    str2=""
    i = len(str1)
    while i > 0:
        str2 +=str1[i - 1]
        i = i -1;
    return str2

word = input("\nEnter a String:")
print("\nThe mirror image of the gievn string is:",rev(word))