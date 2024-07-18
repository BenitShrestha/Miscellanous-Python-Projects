import os
from pydub import AudioSegment
from pydub.utils import which

# AudioSegment.converter = which('ffmepg')
# AudioSegment.ffprobe = which('ffprobe')

bookname = input("Insert bookname, so audio files can be merged: ")

audio_files_path = f'Audio_Book_TTS/Audio_Files/{bookname}/'

audio_files_list = [os.path.join(audio_files_path, name) for name in os.listdir(audio_files_path)]
# print(audio_files_list)    

first_file = AudioSegment.from_file(audio_files_list[0])
for audio_file in audio_files_list[1:]:
    merged = AudioSegment.from_file(audio_file)
    first_file += merged

first_file.export(f"Audio_Book_TTS/Merged_Files/{bookname}.mp3", format="mp3")
