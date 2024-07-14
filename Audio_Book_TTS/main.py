import pyttsx3
import PyPDF2 

# PDF read in bytes
with open('Audio_Book_TTS\Text_Files\GOT_BOOK_ONE.pdf', 'rb') as book:
    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()

    audio_reader.setProperty('rate', 100) # 50 is slow, 300 is fast, we can test it out

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()

        audio_reader.say(content)
        audio_reader.runAndWait()