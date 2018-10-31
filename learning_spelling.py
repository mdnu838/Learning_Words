
import random
from PyDictionary import PyDictionary
import time
from gtts import gTTS
import os

#### install this library
# sudo apt-get update
# sudo apt-get install mpg321

dictionary = PyDictionary()

WORDLIST_FILENAME = "words.txt"

# inFile: file
inFile = open(WORDLIST_FILENAME, 'r')
# line: string
line = inFile.readline()
# wordlist: list of strings
wordlist = line.split()
dictionary.meaning('words')
n = int(input('Enter The Number of words : '))
s = int(input('Enter The Number of second you want to wait for next word : '))
for i in range (n):
    secret_word = random.choice(wordlist)
    print('\n\n','Words : ',secret_word)
    try:
        tts = gTTS(text=secret_word, lang='en')
        tts.save("word.mp3")
        os.system("mpg321 word.mp3")
    except:
        pass
    meaning = dictionary.meaning(secret_word)
    print ('Meaning : ',meaning)
    try:
        k = list(meaning.keys())
        tts = gTTS(text=meaning[k[0]][0], lang='en')
        tts.save("meaning.mp3")
        os.system("mpg321 meaning.mp3")
    except:
        pass
    print('Synonym : ',dictionary.synonym(secret_word))
    print('Antonym : ',dictionary.antonym(secret_word))
    time.sleep(s)

