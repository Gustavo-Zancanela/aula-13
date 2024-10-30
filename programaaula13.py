x = input('Digite "m" para sistema métrico (kg e metros) ou "i" para sistema imperial (libras e pés): ')
def librastokilos(x):
    kilos = x*0.453592
    return kilos
def pestometros(y):
    metros = y*0.3048
    return metros
def imc(peso,altura):
    imc = round(peso/altura**2,2)
    if imc < 18.5:
        print('Seu IMC é', imc,'- Classificação: magreza')
    elif imc >= 18.5 and imc <= 24.9:
        print('Seu IMC é', imc,'- Classificação: normal')
    elif imc >= 25 and imc <= 29.9:
        print('Seu IMC é', imc,'- Classificação: sobrepeso')
    elif imc >= 30 and imc <= 39.9:
        print('Seu IMC é', imc,'- Classificação: obesidade')
    else:
        print('Seu IMC é', imc,'- Classificação: obesidade grave')
if x == 'i':
    peso = librastokilos(float(input('Digite seu peso em libras: ')))
    altura = pestometros(float(input('Digite sua altura em pés: ')))
    imc(peso, altura)
else:
    peso = float(input('Digite seu peso em kilos: '))
    altura = float(input('Digite sua altura em metros: '))
    imc(peso, altura)