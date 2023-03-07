from englisttohindi.englisttohindi import EngtoHindi
from bs4 import BeautifulSoup
import os
import re
import nltk
import fileinput

with open('zzz__www.classcentral.com_report_free-certificates_ - Copy.html', "r", encoding="utf-8", errors='ignore') as html_file:
               soup = BeautifulSoup(html_file, "html.parser")
               for text in soup.stripped_strings:
                    translator= EngtoHindi(text)
                    with fileinput.FileInput('zzz__www.classcentral.com_report_free-certificates_.html', inplace = True,encoding='utf-8') as f:
                            for line in f:                  
                                            if translator is not None:
                                                if re.search(fr'\s{text}\s',line):
                                                    print(line.replace(text,(translator.convert)), end ='')
                                                else:
                                                    print(line, end ='')
                                            else:
                                                print(line, end ='')
