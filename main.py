import speech_recognition as sr
import webbrowser


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def play_youtube(query):
    if query:
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(search_url, new=2)

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if command == "exit":
            break
        elif command and command.startswith("play"):
            query = command[5:].strip()
            play_youtube(query)
        else:
            print("Command not recognized. Try again or say 'exit' to quit.")