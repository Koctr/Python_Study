# -*- coding: utf-8 -*-
# author = 'K0ctr'


from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

with open("D:/客户1-价格通知.pdf", 'rb') as pdf_file:
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)
    process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    print(content)
