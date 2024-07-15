import pyttsx3
import pdfplumber

# Open PDF in read binary mode
with pdfplumber.open(r'Audio_Book_TTS\Text_Files\EnglishSpeaking.pdf') as book:  # Use raw string (r'') or escape backslashes (\\)
    full_text = ""
    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 150)  # Adjust speech rate if needed

    for page in book.pages:
        content = page.extract_text()

        audio_reader.say(content)
        audio_reader.runAndWait()
