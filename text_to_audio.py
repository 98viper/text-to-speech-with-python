from gtts import gTTS 
import os 
language = 'en'

my_file  = open('myfile.txt','r')
#print (my_file.read())
myobj = gTTS(text=my_file.read(), lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 


#we need to work on not saying apostrophy blah blah blaH