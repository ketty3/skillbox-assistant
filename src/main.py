import random
import playsound
from gtts import gTTS
import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду: ")
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: ", speech)
        return speech
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
        return 'error'


def say(text):
    voice = gTTS(text, lang="ru")
    unique_filename = "audio_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(unique_filename)

    playsound.playsound(unique_filename)

    print("Ассистент:", text)


def handle_message(message):
    message = message.lower()

    if "привет" in message:
        say("Привет привет")
    elif "прощай" in message:
        finish()
    else:
        say("Я такой команду не знаю")


def finish():
    say("Пока")
    exit()


if __name__ == '__main__':
    print("Test")

    while True:
        command = listen()
        handle_message(command)
