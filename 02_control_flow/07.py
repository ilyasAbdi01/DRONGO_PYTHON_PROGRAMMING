def find_anagram(word, anagram):
    if sorted (word) == sorted(anagram):
        print ('True')
    else:
        print('False') 

if __name__ == '__main__':
    find_anagram("Drongo", "ognorde")           

    