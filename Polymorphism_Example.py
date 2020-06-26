class File:
    def __init__(self,name,extension):
        self.name = name
        self.extension = extension

    def open(self):
        print('Opening a generic file')

class PDFFile(File):
    def __init__(self,name):
        File.__init__(self,name,".pdf")

    def open(self):
        print('Opening a PDF File')

class TextFile(File):
    def __init__(self,name):
        File.__init__(self,name,".txt")

    def open(self):
        print('Opening a text file')

def fileopen(files):
    for file in files:
        file.open()

PDF1=PDFFile("Brochure")
TXT1=TextFile("Notepad1")
PDF2=PDFFile("Brochure2")

files1=[PDF1,TXT1,PDF2]
fileopen(files1)