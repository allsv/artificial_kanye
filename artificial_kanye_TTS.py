from gtts import gTTS
import os.path


def kanye_text_to_speech(text_string, filename, language = 'pl'):
    text_to_speech_output = gTTS(text = str(text_string), lang=language)
    directory = os.path.join('res','sound', filename + '.wav')
    text_to_speech_output.save(directory)
