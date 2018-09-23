import speech_recognition as sr
r=sr.Recognizer()


harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    print("Say Something!")
    audio=r.record(source)
    
type(audio)    
   
try:
    text=r.recognize_google(audio)
    print("Google thinks you said:\n".format(text) )    
    
except:
    print("Failed to Recognise")    
