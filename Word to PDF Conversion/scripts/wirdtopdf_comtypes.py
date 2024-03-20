# use comtypes if docx2pdf doesn't work
import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = os.path.abspath(sys.argv[1])
out_file = os.path.abspath(sys.argv[2])

in_file = '/content/Ayush Bhattacharya - Updated Resume.docx'
out_file = '/content/Ayush Bhattacharya - Updated Resume.pdf'



word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()