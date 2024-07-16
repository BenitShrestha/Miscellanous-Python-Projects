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

        audio_reader.save_to_file(content, f'Audio_Book_TTS/Audio_Files/{bookname}_page{page.page_number}.mp3')
        # full_text += content # Saves all contents to one variable, might cause issues

        # audio_reader.say(content)
        audio_reader.runAndWait()
    ''' To save whole book as one, for smaller PDFs '''
    # audio_reader.save_to_file(full_text, f'Audio_Book_TTS/Audio_Files/{bookname}_Audio/{bookname}.mp3')
    print(f'{bookname} PDF file converted to audio file and saved')
    # audio_reader.runAndWait()
