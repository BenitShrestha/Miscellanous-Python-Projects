import pyttsx3
import pdfplumber

# Open PDF in read binary mode
bookname = input('Enter name of book: ')
with pdfplumber.open(f'Audio_Book_TTS/Text_Files/{bookname}.pdf') as book:  # Use raw string (r'') or escape backslashes (\\)
    full_text = ""
    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 150)  # Adjust speech rate if needed

    for page in book.pages:
        content = page.extract_text()
        full_text += content
        # audio_reader.say(content)
    
    audio_reader.save_to_file(full_text, f'Audio_Book_TTS/Audio_Files/{bookname}.mp3')
    print(f'{bookname} PDF file convertd to audio file and saved')
    audio_reader.runAndWait()
