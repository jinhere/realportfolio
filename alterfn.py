import os, fnmatch
'''
file_path = 'C:\\Users\\user\\Desktop\\새 폴더\\'

files_to_rename = fnmatch.filter(os.listdir(file_path), '*.doc')
print(files_to_rename)
####
from docx import Document 
for x in files_to_rename:
    document = Document(x)
    if "November" in x.text: # 문단에 "{C001}"이 있으면 날짜로 문자열 변경 
        x.text = x.text.replace("November","December")


###3
for file_name in files_to_rename:    
    os.rename(file_path + file_name, 
          file_path + file_name.replace('9', '10'))
'''
from random import choice
place=[1,2,3,4,5]
def whichnum():
    return choice(place)
