import urllib.request
import urllib.parse
import re
import random
import pyttsx3;     #text to speech library
engine = pyttsx3.init();  #tts init

print("1)Search a word\n2)Play quiz")
ch = int(input("Enter your choice: ").strip())
if ch not in [1,2]:
    print("You can't even enter a number properly. Just rethink of doing GRE!")
    engine.say("You can't even enter a number properly. Just rethink of doing GRE!");
    engine.runAndWait()
else:
    if ch == 1:

        #https://en.oxforddictionaries.com/definition/
        def site(url):
            resp = urllib.request.urlopen(url)
            respData = resp.read()
            return str (respData)

        print('''+++++++++++++++++++++++++++Powered by Oxford Dictionaries+++++++++++++++++++++++''')
        while(1):
            word = input('Enter a word: ').strip().lower()
            
            engine.say(word);          #tts word to speak 


            #word = str.lower(word)
            url = 'https://en.oxforddictionaries.com/definition/'
            url = url + word
            respData = site(url)

            meanings = re.findall(r'"ind">(.*?)</span>',respData)
            examples = re.findall(r'<div class="ex"> <em>&lsquo;(.*?)&rsquo;',respData)

            if meanings:
                engine.runAndWait()  #tts speak the word
                try:
                    file = open('MyDictionary.txt','a')
                    file.write('\n')
                    file.write(word.capitalize())     #write the word
                    file.write('\n')

                    print('Definition:')
                    
                    for x in range(len(meanings)):
                        print('--- ',meanings[x])             #print the meaning of word
                        #file.write('--- '+meanings[x]+'\n')   #write the word to the file         

                    file.close()

                    print('Examples:')

                    if examples:
                        for x in range(len(examples)):
                            print('--- ',examples[x])
                            
                except Exception as e:
                    print('OPPS! Some exception occured: ',e)

            if not meanings:
                url = 'https://en.oxforddictionaries.com/search?filter=dictionary&query='
                url = url + word
                respData = site(url)
                similarmeaningsChunk = re.findall(r'unpadded">(.*?)</ul>',respData)
                similarmeanings = re.findall(r'/definition/(.*?)">',str(similarmeaningsChunk))
                try:
                    print('Did you mean?')
                    for x in similarmeanings:
                        print('--> ',x)
                except:
                    print('Word not found')

            print('''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
            print()

    elif ch == 2:

        file = open('magoosh.txt','r')
        data = file.read()
        data = str(data)

        print("1)Enable options (I'am a noob)\n2)Disable options(I'am a pro)")
        opt = int(input("Enter your choice: ").strip())
        if opt not in [1,2]:
            print("I knew that you are an asshole!")
            engine.say("I knew it");
            engine.runAndWait()
            
        else:
            words = re.findall(r'>>>(.*?)---',data)
            meaning = re.findall(r'---(.*?)>>>',data)

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

        

        
    
