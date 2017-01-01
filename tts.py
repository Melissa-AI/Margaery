import os
import sys

if not os.path.exists('words'):
    print('Please generate the words/ directory by running main.py')
    quit()


def tts(text, choice='p'):
    words_list = []
    for root, dirs, files in os.walk('words/'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".wav":
                words_list.append(os.path.join(root, filename.lower()))

    if sys.platform == 'darwin':
        player = "afplay '"
    else:
        player = "mpg123 '"

    if choice == 'p':
        text_words = text
        word_loc = 'words/' + text_words + '.wav'
        if word_loc in words_list:
            command = player + word_loc + "'"
            os.system(command)
        else:
            print("Don't have the requisite phrase for your request.")
            quit()

    elif choice == 'w':
        text_words = text.split()
        for word in text_words:
            word_loc = 'words/' + word + '.wav'
            if word_loc in words_list:
                command = player + word_loc + "'"
                os.system(command)
            else:
                print("Don't have the requisite words for your request.")
                quit()
