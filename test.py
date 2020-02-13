from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
input_path = "sample.pdf"
output_path = "result.txt"
rsrcmgr = PDFResourceManager()
# codec = 'utf-8'
codec = 'cp932'
params = LAParams()
text = ""
with StringIO() as output:
    device = TextConverter(rsrcmgr, output, codec=codec, laparams=params)
    with open(input_path, 'rb') as input:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(input):
            interpreter.process_page(page)
            text += output.getvalue()
    device.close()
text = text.strip()
print(f'output: {text}')

with open(output_path, "wb") as f:
    f.write(text.encode('utf-8', "ignore"))
