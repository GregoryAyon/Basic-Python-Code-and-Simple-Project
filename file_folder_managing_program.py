import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
files.remove("main.py")

# print(files)

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Medias')
createIfNotExist('Others')

imgExts = [".jpg",".png",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docsExts = [".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]
mediaExts = [".mp4",".mp3",".mov"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in mediaExts) and (ext not in docsExts) and os.path.isfile(file):
        others.append(file)

# print(others)

for image in images:
    os.replace(image, f"Images/{image}")
for item in media:
    os.replace(item, f"Medias/{item}")
for doc in docs:
    os.replace(doc, f"Docs/{doc}")
for other in others:
    os.replace(other, f"Others/{other}")
