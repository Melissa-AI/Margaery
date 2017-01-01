import os
import shutil

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

with open("results.wav", "wb") as f:
    f.write(audio.get_wav_data())

os.system('sox -V3 results.wav output.wav silence 1 0.50 0.1% 1 0.1 0.1% : newfile : restart')

words_list = []
files = os.listdir('.')
for filename in files:
    if os.path.splitext(filename)[1] == ".wav":
        words_list.append(filename.lower())

words_list.remove('results.wav')

if not os.path.exists('words'):
    os.makedirs('words')

for output_file in words_list:
    with sr.WavFile(output_file) as source:
        audio = r.record(source)
    try:
        print("Melissa thinks you said " + r.recognize_google(audio))
        new_name = 'words/' + r.recognize_google(audio) + '.wav'
        shutil.move(output_file, new_name)
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
        os.remove(output_file)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

os.remove('results.wav')
