import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
#its function
video = moviepy.editor.VideoFileClip(video)

audio=video.audio
#path of file where it is located
audio.write_audiofile("sample.mp3")
print("completed!")
