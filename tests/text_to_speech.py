from gtts import gTTS

#making the text-to-speech audio file
text = gTTS(text='Kanye West jest moim bogiem', lang='pl')

#saving the text-to-speech audio file
text.save("text_to_speech_output.wav")
