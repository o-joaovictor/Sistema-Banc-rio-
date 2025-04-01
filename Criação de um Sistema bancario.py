menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha uma opção: """


saldo = 0
limite = 500
extrato = ""
numeros_de_saques = 0
limite_de_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":  
        
         valor = float(input("Digite o valor do depósito:"))
      
            
         if valor > 0: 
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
                
                
         else:print("Valor inválido. O depósito deve ser maior que zero.")
    
    
    
    
    
    elif opcao == "s": 
    
        valor = float(input("Digite o valor do saque:"))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numeros_de_saques >= limite_de_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_de_saques += 1
            print("Saque realizado com sucesso!")
        
        else: print("Valor informado é inválido. Operação falhou!")

    elif opcao == "e":
       print("====== EXTRATO ======")
       print("Não foram realizadas transações no período." if not extrato else extrato)
       print(f"saldo: R$ {saldo:.2f}")
       print("===========================")
    
    
    elif opcao == "q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
