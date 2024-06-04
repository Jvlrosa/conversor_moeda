from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
# dolar 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("dolar hj" + Keys.RETURN)
dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto1 = dolar.text
print(f'o dolar hoje é de: {texto1}')

# Euro
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Euro hj" + Keys.RETURN)
euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto2 = euro.text
print(f'o Euro hoje é de: {texto2}')

# Libra esterlina 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Libra esterlina hj" + Keys.RETURN)
Libra_esterlina = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto3 = Libra_esterlina.text
print(f'A Libra esterlina hoje está à: {texto3}')

# Iene 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Iene hj" + Keys.RETURN)
Iene = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto4 = Iene.text
print(f'o Iene hoje é de: {texto4}')

# Dólar Australiano
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Dólar Australiano hj" + Keys.RETURN)
Dolar_Australiano = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto5 = Dolar_Australiano.text
print(f'o Dólar Australiano hoje é de: {texto5}')

# Franco Suíço 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Franco Suíço hj" + Keys.RETURN)
Franco_Suico = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto6 = Franco_Suico.text
print(f'o Franco Suíço hoje é de: {texto6}')

# Dólar Canadense 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Dólar Canadense hj" + Keys.RETURN)
Dolar_Canadense = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto7 = Dolar_Canadense.text
print(f'o Dólar Canadense hoje é de: {texto7}')

# Yuan 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Yuan hj" + Keys.RETURN)
Yuan = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto8 = Yuan.text
print(f'o Yuan hoje é de: {texto8}')

# Peso Argentino 
navegador.get('https://www.google.com')
navegador.find_element('xpath', "//*[@id='APjFqb']").send_keys("Peso Argentino hj" + Keys.RETURN)
Peso_Argentino = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
texto8 = Peso_Argentino.text
print(f'o Peso Argentino hoje é de: {texto8}')

input()