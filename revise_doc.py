import os, fnmatch

# 1) return names of all files in certain folder
file_path = 'C:\\Users\\user\\Desktop\\새 폴더\\'

files_to_rename = fnmatch.filter(os.listdir(file_path), '*.doc')
print(files_to_rename)
# end of 1)

# 2) 모든 학생들의 지난달 성적표 날짜를 전부 이번달로 바꾸기
# change the date section['November' -> 'December'] in all students' reports(.doc)
from docx import Document 
for x in files_to_rename:
    document = Document(x)
    if "November" in x.text: # 문단에 "{C001}"이 있으면 날짜로 문자열 변경 
        x.text = x.text.replace("November","December")
# end of 2)

# 3) 2번과 같은 결로, 모든 학생들의 성적표 파일 이름[예)kate_9을 kate_10으로] 바꾸기
for file_name in files_to_rename:    
    os.rename(file_path + file_name, 
          file_path + file_name.replace('9', '10'))
# end of 3)
