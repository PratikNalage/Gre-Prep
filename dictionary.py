#https://en.oxforddictionaries.com/definition/
import urllib.request
import urllib.parse
import re

def site(url):
    resp = urllib.request.urlopen(url)
    respData = resp.read()
    return str (respData)

print('''
+++++++++++++++++++++++++++Powered by Oxford Dictionaries+++++++++++++++++++++++
''')

word = input('Enter a word to search: ').strip().lower()

import pyttsx3;     #text to speech library
engine = pyttsx3.init();  #tts init
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

print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')



'''comments
<div class="ex"> <em>&lsquo; ... &rsquo;  for examples

'''
