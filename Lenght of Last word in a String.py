def lengthOfLastWord(s: str) -> int:
    array = s.split()
    wordsAmount = len(array)
    lastWord = (array[wordsAmount - 1])
    return len(lastWord)

phrase = input('Please give a phrase: ')
print(lengthOfLastWord(phrase))