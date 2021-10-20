import random
porta = []
lista = []

for g in range(1,31):
    n = int(input("""
bem-vindo ao jogo das portas!
Veremos se você ganhará um carro ou não!
escolha uma porta (1) / (2) / (3):::: """))
    if n ==1 or n==2 or n==3:
        for h in range(1,4):
            lista.append(h)
            porta.append(h)
            random.choice(lista)

            print("""você escolheu a porta %i, mas eu lhe informo
                  que na porta %i há um bode."""%(n,random.choice(porta)))
            trocar = int(input("deseja trocar de porta [(1)- sim / (0) - não]: "))
            if trocar == 1:
                n2 = int(input("digite o numero da porta. 1/2/3"))
                if n2 == random.choice(lista):
                    print("você ganhouu um carro zero.. ")
                    

                else:
                    print("você ganhou um cabrito . kkkk")
                    
                break    
            if trocar == 0:
                
                if n == random.choice(lista):
                    print("você ganhouu ... um carro zero")

                else:
                    print("você ganhou um camelo .. kkkk")
                    
                break    

                    
                 
        
