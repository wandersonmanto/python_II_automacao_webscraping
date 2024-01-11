from bs4 import BeautifulSoup

# Importando página html
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
  content = file_html.read()
  # print(content)
  soup = BeautifulSoup(content, 'lxml')
  # print(soup.prettify())
  
# Recuperar titulos das vagas
vagas = soup.find('h5')
# print(vagas)
cursos = soup.find_all('h5')
for curso in cursos:
  print(curso.text)  
