from bs4 import BeautifulSoup 


link=input('사이트 주소: ')
linkname=input('바로가기 이름: ')
with open('../../SHORTCUT.html',encoding='cp949') as f:
    text=f.read()
    soup=BeautifulSoup(text,'html.parser')

new_line=soup.new_tag("a",href=link)
new_line.string=linkname

soup.body.append(new_line)
br = soup.new_tag('br')
br2 = soup.new_tag('br')

soup.body.insert(-1,br)
soup.body.insert(-1,br2)

with open("../../SHORTCUT.html", "w") as editf:
    editf.write(str(soup))
