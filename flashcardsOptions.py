import re
import random

file = open('magoosh.txt','r')
data = file.read()
data = str(data)

print("1)Enable options (I'am a noob)\n2)Disable options(I'am a pro)")
opt = int(input("Enter your choice: ").strip())
if opt not in [1,2]:
    print("I knew that you are an asshole!")
    
else:
    words = re.findall(r'>>>(.*?)---',data)
    meaning = re.findall(r'---(.*?)>>>',data)


    import pyttsx3;     #text to speech library
    engine = pyttsx3.init();  #tts init

    while(1):
        r = random.randint(0, len(words) -1)
        print('Guess the word:', meaning[r])
        
        if opt == 1:
            print ('Hint: ',end=' ')
            options = []
            options.append(words[r])   #opt1 ans
            rr = random.randint(0, len(words) -1)
            options.append(words[rr])  #opt2
            rr = random.randint(0, len(words) -1)
            options.append(words[rr])  #opt3
            rr = random.randint(0, len(words) -1)
            options.append(words[rr])  #opt4
            random.shuffle(options, random=None)
            print(options[0],options[1],options[2],options[3])
        

        engine.say(words[r]);          #tts word to speak
        
        ans = str(input('Input your answer: ').strip())
        print("The answer is ",words[r])
        
        


        print()

        engine.runAndWait()  #tts speak the word
