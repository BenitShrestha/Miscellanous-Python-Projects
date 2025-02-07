import os
import pyttsx3
import pdfplumber
from audioMerge import audio_merge

# Specify directory paths
folder_path_text = "Audio_Book_TTS/Text_Files"
folder_path_audio = "Audio_Book_TTS/Audio_Files"

# Iterate over PDF files in directory
file_names = [filename for filename in os.listdir(folder_path_text) if filename.endswith('.pdf')]
just_names = [os.path.splitext(filename)[0] for filename in file_names] # Removes file extension
print(f'List of available books: {', '.join(just_names)}')
# Create new folders based on PDF filenames
for name in file_names:
    # Construct full path for each new folder
    new_folder_path = os.path.join(folder_path_audio, os.path.splitext(name)[0])
    ''' os.path.splitext - Splits the path into root(filename) and extension (pdf) as a tuple '''
    os.makedirs(new_folder_path, exist_ok=True)

# Open PDF in read binary mode
bookname = input('Enter name of book (without .pdf extension): ')
count_page = 0
# Ensure the specified PDF file exists
if f'{bookname}.pdf' not in file_names:
    print(f"Error: '{bookname}.pdf' not found in '{folder_path_text}' directory.")
else:
    with pdfplumber.open(os.path.join(folder_path_text, f'{bookname}.pdf')) as book:
        count_page = len(book.pages)
        audio_reader = pyttsx3.init()
        audio_reader.setProperty('rate', 200)  # Adjust speech rate if needed
        
        if count_page >= 100:
            print('Over 100 pages, might take a long time to convert to audio')

        for i, page in enumerate(book.pages): # Enumerate to limit no. of pages, conditionally
            content = page.extract_text()
            audio_file_path = os.path.join(folder_path_audio, os.path.splitext(bookname)[0], f'{bookname}_page{page.page_number}.mp3')
            audio_reader.save_to_file(content, audio_file_path)
            audio_reader.runAndWait()  # Wait for each page's text-to-speech conversion to complete
    print(f"Total pages in {bookname}.pdf : {count_page} pages")
    print(f'{bookname}.pdf file converted to audio files and saved')
    audio_merge(bookname)
