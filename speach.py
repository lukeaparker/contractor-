import speech_recognition as sr

class Speach():
    def __init__(self):
        # Creates an instance of Recognizer(), detects voice input
        self.r = sr.Recognizer()
        # TODO: allows users to choose input devices
        # receives audio from users first mic
        self.mic = sr.Microphone()

    def toggle(self, toggle_str, output):
        with mic as source:
            # checks for commands
            while True:
                self.r.adjust_for_ambient_noise(source)
                print("Say Something")
                try:
                    audio = self.r.listen(source)
                    audio_str = self.r.recognize_google(audio)

                    # start command is yo
                    if toggle_str in audio_str:
                        self.r.adjust_for_ambient_noise(source)
                        print(output)
                except sr.UnknownValueError:
                    print("Say that again?")

def test_toggle():
    toggle_str = "home axis"
    output = "homing axis"
    speach = Speach()
    Speach.toggle(toggle_str, output)

test_toggle() 



