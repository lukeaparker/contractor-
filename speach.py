import speech_recognition as sr

class Speach():
    def __init__(self):
        # Creates an instance of Recognizer(), detects voice input
        self.r = sr.Recognizer()
        # TODO: allows users to choose input devices
        # receives audio from users first mic
        self.mic = sr.Microphone()

    def get_command(self, toggle_str, output):
        with self.mic as source:
            while True:
                # checks for commands
                if "home" in toggle_str:
                    self.r.adjust_for_ambient_noise(source)
                    print("Say Something")
                    try:
                        audio = self.r.listen(source)
                        audio_str = self.r.recognize_google(audio)
                        words = audio_str.split()
                        if toggle_str == words[0]:
                            del words[0]
                        print(words)
                        return words
                    except sr.UnknownValueError:
                        print("Say that again?")
                        return False 
                        
                

def test_toggle():
    toggle_str = "home"
    output = "homing axis"
    speach = Speach()
    # speach.get_command(toggle_str, output)

test_toggle() 



