## Margaery

Margaery is an experimental attempt to build an open source Text to Speech (TTS) engine generator. If successful, Margaery will allow you to construct a customized and personalized TTS engine which will speak in your voice.

### Installation of Margaery

You will need to install [PortAudio](http://www.portaudio.com/download.html), [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/), [SoX](http://sox.sourceforge.net) and [mpg123](https://www.mpg123.de/download.shtml). You will then need to issue the following commands on your terminal:

```
git clone https://github.com/Melissa-AI/Margaery.git
cd Margaery
pip install -r requirements.txt
```

### Working with Margaery

First of all, run the `main.py` file and start recording your voice. If you want to record phrases like 'how are you', you are good to go with one phrase at a time. The recording will be saved with the name `how are you.wav` inside the `words` directory. For recording individual words separately, try speaking with a one second gap between your words. In that case, your words would be saved in the form of individual audio recordings.

Now, for executing the TTS, run the `tts.py` file and choose if you want to read out a phrase or want to sew individual recorded words together to create a new phrase (doesn't work that well currently). Type in the text that you want to hear in your voice in the `tts()` function in the `tts.py` file. Please note that Margaery is very young and highly experimental (not suitable for usage yet).

### Discussion and Support

If you face an issue or require support, please take a look through the GitHub Issues, as you may find some useful advice there. If you are still facing issues, feel free to create a post at our [Google Group Forum](https://groups.google.com/forum/#!forum/melissa-support--discussion-forum/) describing the issue and the steps you have taken to debug it.

### Licence

[The MIT License (MIT)](https://github.com/Melissa-AI/Margaery/blob/master/LICENSE.md)
