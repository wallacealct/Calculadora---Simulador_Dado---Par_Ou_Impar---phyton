from logging import exception
import random

class SimuladoDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'voce gostaria de gerar um  valor para o dado?'

    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não') 
        except:
            print('Ocorreu um erro ao receber sua resposta')              

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))        

simulador = SimuladoDeDado()
simulador.iniciar()        
