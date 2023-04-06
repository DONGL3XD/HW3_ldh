def wordReverse(input):
    input = input.split()
    reversed = [word[ : : -1] for word in input]

    return " ".join(reversed)

if __name__ == '__main__':
    str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"

    print(wordReverse(str1))
    print(wordReverse(str2))