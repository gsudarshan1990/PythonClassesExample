class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def open(self):
        print('Opening the generic file')

class PDFFile(File):
    def __init__(self,name):
        super().__init__(name,".pdf")

    def open(self):
        print('Opening the pdf file')

class TextFile(File):
    def __init__(self,name):
        super().__init__(name,".txt")

    def open(self):
        print('Opening the text file')

pdf1=PDFFile("Broucher")
txt1=TextFile("TextFile1")
pdf2=PDFFile("Broucher1")

def file_open(files):
    for file in files:
        file.open()

total_files=[pdf1,txt1,pdf2]

file_open(total_files)