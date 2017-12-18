import re
import random

file = open('magoosh.txt','r')
data = file.read()
data = str(data)

words = re.findall(r'>>>(.*?)---',data)
meaning = re.findall(r'---(.*?)>>>',data)


import pyttsx3;     #text to speech library
engine = pyttsx3.init();  #tts init

while(1):
    r = random.randint(0, len(words) -1)
    print('Guess the word:', meaning[r])
    print ('Hint: ',end=' ')
    for i in range(len(words[r])-1):     #display the hint
        if i == 0:
            print(words[r][i],end='')
        elif i == int(len(words[r])/2):
            print(words[r][i],end='')
        elif i == len(words[r])-2:
            print(words[r][i],end='')
        else:
            print('_',end=' ')
    print('')

    engine.say(words[r]);          #tts word to speak
    
    ans = input('Input your answer: ')
    ans = ans.upper()
    if ans == words[r]:
        print('Hurrah! You got it correct')
    else:
        print('OPPS! Incorrect answer. The correct answer is',words[r])

    print()

    engine.runAndWait()  #tts speak the word
