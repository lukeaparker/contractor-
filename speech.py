import speech_recognition as sr
start_prompt = 'Active Listening Begun:'
# Creates an instance of Recognizer(), detects voice input
r = sr.Recognizer()
# TODO: allows users to choose input devices
# receives audio from users first mic
mic = sr.Microphone()
with mic as source:
    # checks for commands
    while True:
        r.adjust_for_ambient_noise(source)
        print(start_prompt)
        try:
            audio = r.listen(source)
            audio_str = r.recognize_google(audio)
            print(audio_str)
            if "home" in audio_str:
                print("homing all axis")
            if "prepare" in audio_str:
                print("BedTemp:60  NozTemp: 210")
            if "extrude" in audio_str:
                print("extruding 10mm")
        except sr.UnknownValueError:
            print("Say that again?")