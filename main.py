import os
from PyPDF2 import PdfReader
from gtts import gTTS

language = "ru"
dir_path = os.getcwd()+"/files"
files = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append(os.path.join(dir_path, path))
print(files)

for x in files[1:]:
    reader = PdfReader(x)
    f = open(x[:-3] + "txt", "a")
    for page in reader.pages:
        text = page.extract_text()
        myobj = gTTS(text=text, lang=language, slow=False)
        f.write(text)
        myobj.save(x[:-3] + "mp3")
    f.close()