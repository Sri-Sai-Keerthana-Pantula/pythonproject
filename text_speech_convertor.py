from gtts import gTTS
import os
text = "Hello user! You are currently explorig the outcome of the library developed by Google India team..To customize our voice to your text enter the text here"
language = 'en'
speech = gTTS(text=text, lang=language,slow=False)
speech.save("sample.mp3")
os.system("start sample.mp3")

t_input=input("Enter input for text to speech conversion")
speech1 = gTTS(text=t_input, lang=language,slow=False)
speech1.save("speech.mp3")
os.system("start speech.mp3")
