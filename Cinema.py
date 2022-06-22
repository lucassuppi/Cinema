import os
import csv
from time import sleep

# código escrito por Arthur Maron, Lucas Suppi, Theodoro Salazar, Kalleu Queirolo
# Cinema #

os.system('cls' if os.name == 'nt' else 'clear')

# inicializado
initialized = False

#desenha a progressbar do relatório
def ProgressBar(percentage):


  progressbar = "[--------------------]"
# tamanho da string desconsiderando os colchetes
  value = len(progressbar)-2

#se o valor que chegar for 0 simplesmente retorna ela vazia
  if percentage == 0:

    return progressbar


#se o valor que chegar for entre 1 e 99 roda o código pra mostrar pro valor especifico 
  elif percentage > 0 or percentage <= 99:
#pega a porcentagem recebida
    perhundred = percentage / 100
    #calcula a porcentagem recebida do tamanho da string da progressbar
    x = value * perhundred
    #transforma em inteiro pra usar no .replace()
    x = int(x)
    #substitui a quantidade especifica na string
    showprog = progressbar.replace("-","=",x)   
    return showprog

  elif percentage == 100:
#se o valor que chegar for 100 desenha ela cheia e mostra
    progressbar = "[====================]"
    return progressbar

#carrega a informação salva em arquivo
def load_data():
  global load

#pergunta o nome do arquivo que o usuario quer carregar
  load = str(input("Digite o nome do arquivo para realizar o loading: "))
#fala o arquivo que foi escolhido
  print("Arquivo escolhido:", load+".csv")

#testa se o arquivo existe
  try:
#abre o arquivo    
    cinema = open(load+".csv")
#se o arquivo não esistir cai nessa exceção e roda novamente a função
  except:
    print("Este anime não existe!")
    return load_data()
# se não continua o a leitura do arquivo
  else:
    leitor = csv.reader(cinema)
    info = list(leitor)
    cinema.close()
    linha=len(info)

#aqui passa pela matriz que ja tem 
    for i in range(rows):
      for j in range(columns):
#aqui passa pelas linhas da matriz do arquivo
        for k in range (linha):
# ignora as linhas vazias do arquivo .csv
          if info[k] != []:
#separa o assento das informaçoes
            assento = info[k][0]         
            if assento[1:].isnumeric() == True:
              if int(ord(assento[0]))-65 > rows:
                print("O cinema carregado tem mais fileiras que o atual")
                window2()
                break
              elif int(assento[1:])-1 > columns:
                print("O cinema carregado tem mais colunas que o atual")
                break
  #testa se o o numero do assento é realmente um numero no arquivo
              else:

    #testa onde na matriz é igual ao valores no arquivo
                if i == int(ord(assento[0]))-65 and j == int(assento[1:])-1:
    #adiciona os valores do arquivo na matriz do programa
                      cstructure[i][j] = info[k][1]              
            else:
              continue
    input("Pressione enter para continuar")



 
def verifyseats():
  global verify
#recebe o assento para ser verificado
  verify = input("Digite a localização de uma cadeira para realizar a verificação: ")
#testa se ta no tamanho certo a entrada

  if len(verify) > 3 or len(verify) <2 :
    print("Por favor informe a fileira e o assento")
  
    return verifyseats()
#testa se a pessoa informou o numero do assento e acaba testando se esta na ordem correta
  elif verify[1:].isnumeric() == False:

    print("Por favor, informe o número do assento")
    return verifyseats()
#testa se o valor recebido no input é uma letra

  elif verify[0].isnumeric() == True:
    print("Por favor, informe a fileira como letra")
    return verifyseats()
  else:
  #testa se o valor recebido no input é uma letra

      upperx = verify[0].upper()

      #transforma os dois em valor numerico para o indice conseguir entender
      fileira = (int(ord(upperx))-65)
      assento = int(verify[1:])-1
      #testa se os valores informados são posiveis de usar na matriz
      if fileira > rows-1:
        print ("Essa fileira não existe!")
        input('Precione enter para continuar') 
        os.system('cls' if os.name == 'nt' else 'clear')
        return verifyseats() 
      if assento > columns-1:
        print ("Esse assento não existe!")  
        input('Precione enter para continuar') 
        os.system('cls' if os.name == 'nt' else 'clear')
        return verifyseats()     
      
#se na posição da matriz tiver um ponto então o assento não foi reservado...
      if cstructure[fileira][assento] == ".":

          print("O assento está liberado")       
              
#se não ele pega os valores e separa 
      else:

          mostraidadeEsexo = cstructure[fileira][assento]

          mostrasplit = mostraidadeEsexo.split()

#testa se é masculino...
          if mostrasplit[1].isnumeric() == True:
            idade = int(mostrasplit[1])
            if idade >= 60 or idade < 18:
              if mostrasplit[0] == "M":
                print ("A pessoa que esta nesse assento é um homem de",mostrasplit[1]," anos e pagou R${:.2f}".format(price/2))
              elif mostrasplit[0] == "F":
                print ("A pessoa que esta nesse assento é uma mulher de",mostrasplit[1]," anos e pagou R${:.2f}".format(price/2))

            else:
              if mostrasplit[0] == "M":
          
                print ("A pessoa que esta nesse assento é um homem de",mostrasplit[1]," anos e pagou R${:.2f}".format(price))
    #ou feminino e mostra
              elif mostrasplit[0] == "F":
          
                print ("A pessoa que esta nesse assento é uma mulher de",mostrasplit[1]," anos e pagou R${:.2f}".format(price))

def chooseseats():
  global choose
#pergunta aquantidade de assentos a serem reservados
  quantassentos = input("Quantos assentos deseja reservar: ")
#testa se é um numero se não for chama a funçao de volta
  if quantassentos.isnumeric() == False:
    print("Por favor, informe um número")
    print()
    input('Precione enter para continuar')
    os.system('cls' if os.name == 'nt' else 'clear') 
    return chooseseats()
#se não ele continua
  else:
    quantassentos = int(quantassentos)
    if quantassentos > columns:
        print('A sequência de assentos não coincide com a quantidade de assentos suportado')
        input('Precione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear') 
        return chooseseats()
    else:

    #pede a partir de qual assento reservar
        choose = input("Apartir de qual assento:  ")
      
    #testa se esta no tamanho certo
        if len(choose) > 3 or len(choose) <2 :
          print("Por favor informe a fileira e o assento")
        
          return chooseseats()
    #testa se a pessoa informou o numero do assento e acaba testando se esta na ordem correta
        elif choose[1:].isnumeric() == False:

          print("Por favor, informe o número do assento")
          return chooseseats()
        elif choose[0].isnumeric() == True:
          print("Por favor, informe a fileira como letra")
          return chooseseats()
        else:
      #testa se o valor recebido no input é uma letra
          try:
            upperx = choose[0].upper()
          except:
            print("Por favor, informe uma letra")
          else:
          #transforma os dois em valor numerico para o indice conseguir entender
            fileira = (int(ord(upperx))-65)
            assento = int(choose[1:])-1
          #testa se os valores informados são posiveis de usar na matriz
            if fileira > rows-1:
              print ("Essa fileira não existe!")
              input('Precione enter para continuar') #botei isso
              os.system('cls' if os.name == 'nt' else 'clear') #botei isso 
              return chooseseats()
            if assento > columns-1:
              print ("Esse assento não existe!")
              input('Precione enter para continuar') #botei isso
              os.system('cls' if os.name == 'nt' else 'clear') #botei isso 
              return chooseseats()     

    #passa pela matriz pra ver se o assento não esta ocupado ou se os assentos pedidos existem
            if quantassentos > 1:
              for j in range(quantassentos):
                  #serve para testar se os assentos existem
                  if assento+j > rows-1:
                    print ("Não temos esse assento nesse fileira"+" (",chr(fileira+65),assento+j+1,")")
                    input('Precione enter para continuar') 
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    return chooseseats() 

                  if cstructure[fileira][assento+j] == ".":
                    teste = True

                  else:
                      teste = False
                      break
            if quantassentos == 1:

                  if cstructure[fileira][assento] == ".":
                    teste = True

                  else:
                      teste = False


            if quantassentos < 1:
              print("Por favor informe um número valido!") 
              input('Precione enter para continuar') 
              os.system('cls' if os.name == 'nt' else 'clear') 
              return chooseseats()


    #se o teste for verdade
            if teste == True:
    #começa a perguntar o genero e a idade         
              for i in range(quantassentos):
                MorF = input("Voce é do sexo masculino ou feminino?(M ou F): ")
                age = input("Informe sua idade: ")
                print()
                agen = age.isnumeric()
    #testa se a pessoa colocou M ou F tanto maiusculo quanto minusculo
                if MorF!= "M" and MorF!= "F" and MorF!= "m" and MorF!= "f":
                  print("Erro, porfavor informe com M ou F")
                  input('Pressione enter para continuar')
                  os.system('cls' if os.name == 'nt' else 'clear')
                  
                  for k in range(quantassentos-1):
                    #se a pessoa não colocou nem M nem F volta as posiçoes para ponto e chama afunção denovo
                    cstructure[fileira][assento+k] = "."

                  return chooseseats()
    #basicamente a mesma coisa do anterior mas testando se a idade é realmente um numero
                if agen == False:
                  print("Erro, você digitou a idade incorretamente")
                  input('Pressione enter para continuar')
                  os.system('cls' if os.name == 'nt' else 'clear')
                  for k in range(quantassentos-1):
                    cstructure[fileira][assento+k] = "."
                  return chooseseats()
    #se não entrar em nenhum if adiciona o genero e a idade na posição exata da matriz 
                else:
                  cstructure[fileira][assento+i] = MorF.upper()+" "+age

              
              print("Você reservou o assento",upperx,assento+1,"e mais", quantassentos-1,"assentos") 
              input('Pressione enter para continuar')
            else:

              print ("Um dos assentos esta ocupado")

      
#libera a reserva de n cadeiras
def releaseseat():
  global release
#pergunta aquantidade de assentos a serem liberado
  quantassentos = input("Quantos assentos deseja liberar: ")
#testa se é um numero se não for chama a funçao de volta
  if quantassentos.isnumeric() == False:
    print("Por favor, informe um número")
    releaseseat()
 #se não ele continua
  else:
    quantassentos = int(quantassentos)

    print(quantassentos)
#pede a partir de qual assento reservar
    release = input("Apartir de qual assentos: ")

#testa se esta no tamanho certo
    if len(release) > 3 or len(release) <2 :
        print("por favor informe a fileira e o assento")
      
        releaseseat()
#testa se a pessoa informou o numero do assento e acaba testando se esta na ordem correta
    elif release[1:].isnumeric() == False:

        print("Por favor, informe o número do assento")
        releaseseat()

    elif release[0].isnumeric() == True:
        print("Por favor, informe a fileira como letra")
        return releaseseat()
    else:
  #testa se o valor recebido no input é uma letra    
      try:
        upperx = release[0].upper()
      except:
        print("por favor informe uma letra")
      else:
      #transforma os dois em valor numerico para o indice conseguir entender
        fileira = (int(ord(upperx))-65)
        assento = int(release[1:])-1
      #testa se os valores informados são posiveis de usar na matriz
        if fileira > rows-1:
          print ("Essa fileira não existe!")
        if assento > columns-1:
          print ("Esse assento não existe!")      
      #serve para testar se os assentos existem
        for j in range(quantassentos):
            if assento+j > rows-1:
              print ("Não temmos esse assento nesse fileira"+" (",chr(fileira+65),assento+j+1,")")
              input('Precione enter para continuar') 
              os.system('cls' if os.name == 'nt' else 'clear')
              return releaseseat() 


        for i in range(quantassentos):
#volta as posiçoes de volta para um ponto 

              cstructure[fileira][assento+i] = "."
          
        print("Você liberou os Assentos solicitados") 

#desenha o mapa do cinema
def cinemamap():
  print('''Mapa do cinema
  
  
  ''')
#cria uma lista
  cmap = []
#adiciona as informaçoes na matriz
  for x in range(rows):
        cmap.append([0] * columns)

  for x in range(rows):
        for y in range(columns):
            cmap[x][y] = ('.')
 
#passa pela matriz
  for c in range(rows):
    for d in range (columns):
#testa se o assento ja foi reservado
      if cstructure[c][d] != ".":
#marca com um x os assentos ja reservados
        cmap[c][d] = "X"

#se se o assento não tiver sido reservado
      elif cstructure[c][d] == ".":  
        continue
#mostra o mapa
  print(" ",end='  ')
  for i in range(columns):
    print(i+1,end='  ')
  print()
  for x in range(rows):
        print(chr(x+65),end = '  ')
        for y in range(columns):
            print(cmap[x][y], end='  ')
        print()
  print()
  input('Pressione enter para continuar')


def report():
  global report

#criando variaveis que serão usadas no relatório

  quantreserved = 0
  quantfree = 0
  quantman = 0
  quantwomen= 0
  vendatotal = 0
  quantelderly= 0
  quantteen= 0
  quantfull= 0
  valorteen = 0
  valorelderly = 0
  print("Relatório:")

  print("assento | sexo | idade | valor")
  print('''                    ''')


#passa por toda a matriz
  for c in range(rows):
    for d in range (columns):
# testa os assentos vendidos
      if cstructure[c][d] != ".":
#conta as vendas totais
        vendatotal = vendatotal+1

#pega a informação do genero e a idade e cria duas strings separadas
        tabelare = cstructure[c][d]
        mostratab = tabelare.split()

        ager = int(mostratab[1])
        genderr = mostratab[0]
        filr = chr(c + 65)
#testa se a pessoa é de menor e adiciona no contador
        if ager < 18 :

          valorr = price/2
          quantteen = quantteen+1
#testa se a pesso tem mais de 60 e adiciona no contador
        elif ager >= 60:
          valorr = price/2
          quantelderly = quantelderly+1
#se não  é inteiro, adiciona no contador
        else:
          valorr = price
          quantfull =quantfull+1
#testa se é homen ou mulher e adiciona no contador
        if genderr == "m" or genderr == "M":
    
          genderr = "Masculino"
          quantman = quantman+1        

        elif genderr == "f" or genderr == "F":
    
          genderr = "Feminino "
          quantwomen= quantwomen+1
#adiciona no contador a quantidade de locais reservados
        quantreserved = quantreserved+1
        print(("{}-{} | {} | {} | R${:.2f}").format(filr,d+1,genderr,ager,valorr))
      elif cstructure[c][d] == ".":

        quantfree= quantfree+1

  print('''                    
  
      ''')


#mostra o total de lugares , os reservados e os liberados


  print("Total de lugares:", rows*columns)
  print("Reservados: ",  quantreserved )
  print("Liberados: ", quantfree )
  print('''                    
 
      ''')
#mostra o total de reservas e quantos são homens e quantas são mulheres
  print("Total de Reservas:", quantreserved)
  print("Homens: ",  quantman )
  print("Mulheres: ", quantwomen )
  print('''                    
        ''')

#faz o calculo da porcentagem

  percentageelderly = (quantelderly/vendatotal)*100 
  percentageteen = (quantteen/vendatotal)*100 
  percentagefully = (quantfull/vendatotal)*100 
  if quantteen != 0 or quantelderly != 0:
    valorteen = quantteen*(price/2)
    valorelderly = quantelderly*(price/2)

  valorfull = quantfull*price

#mostra todas as informaçoes nessa forma

  print(f'Meia menor:   {quantteen} - {percentageteen:.2f}%  {ProgressBar(percentageteen)} R$ {valorteen:.2f}\nInteira   :   {quantfull} - {percentagefully:.2f}%  {ProgressBar(percentagefully)} R$ {valorfull:.2f}\nMeia idoso:   {quantelderly} - {percentageelderly:.2f}%  {ProgressBar(percentageelderly)} R$ {valorelderly:.2f}\nTotal     :   {vendatotal} - {100:.2f}%  {ProgressBar(100)} R$ {valorfull + valorteen + valorelderly:.2f}')
  input("Pressione enter para continuar")


def savedata():
  global save

#pede o nome do arquivo
  save = str(input("Digite o nome do arquivo para realizar o save: "))
  print("Local escolhido:", save)
#adiciona uma row de cabechalho
  data = [['Assento','Sexo', 'Idade']]
#abr o arquivo ou cria um novo
  arq = open(save+'.csv', 'w')
  writer2 = csv.writer(arq)
#escreve o cabeçalho no arquivo
  writer2.writerows(data)
#passa pela matriz
  for i in range(rows):
    for j in range(columns):
#testa os indices reservados e adiciona no arquivo
      if cstructure[i][j] != ".":
  
        writer2.writerow([chr(i+65)+str(j+1),cstructure[i][j]])
#se não continua
      else:
        continue

  arq.close()
  print("Informações salvas!")



#cria o menu
def window2():
  print("1. Carregar dados\n2. Consultar situação de assento\n3. Reservar assentos\n4. Liberar assentos\n5. Visualizar mapa do cinema\n6. Relatório\n7. Salvar dados\n9. Sair")
  response2 = input("Selecione uma opção: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"Opção escolhida: {response2}\n")
  if response2 == "1":
    load_data()
  elif response2 == "2":
    verifyseats()
  elif response2 == "3":
    chooseseats()
  elif response2 == "4":
    releaseseat()
  elif response2 == "5":
    cinemamap() 
  elif response2 == "6":
    report() 
  elif response2 == "7":
    savedata() 
  elif response2 == "9":
    exit()
  else:
    print("Opção não existente!")
  sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
#primeiro janela que abre no programa e pede o tamanho da sala de cinema e o valor do ingresso    

def window1():
  global price, rows, columns, initialized, dados
  os.system('cls' if os.name == 'nt' else 'clear')
  print("1. Inicializar cinema\n9. Sair")
  response1 = input("Selecione uma opção: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"Opção escolhida: {response1}\n")
  if response1 == "1":
    print('Capacidade mínima e máxima do cinema ↓\nDe 5 a 15 fileiras e assentos')
    print()
    try:
      price = float(input("Informe o valor do ingresso: "))
    except:
        print("Por favor informe um número")
        input("Pressione enter para continuar")
    else:
      try:
        rows = int(input("Informe a quantidade de fileiras: "))
      except:
        print("Por favor informe um número")
        input("Pressione enter para continuar")        
      else:
        if rows < 5:
          print("Por favor informe um ou mais fileiras")
          input("Pressione enter para continuar")
          return window1()
        if rows > 15:
          print("Por favor informe menos fileiras")
          input("Pressione enter para continuar")
          return window1()
        else:
          try:
            columns = int(input("Informe a quantidade de assentos por fileira: "))
          except:
            print("Por favor, informe um número")
            input("Pressione enter para continuar")
          else:
            if columns < 5:
              print("Por favor informe um ou mais assentos")
              input("Pressione enter para continuar")
              return window1()
            if columns > 15:
              print("Por favor informe menos assentos")   
              input("Pressione enter para continuar")
              return window1()
            else:
              print(f"Valores informados:\nR${price}\nLinhas: {rows}\nColunas: {columns}")
              print()
              

              for x in range(rows):
                  cstructure.append([0] * columns)

              for x in range(rows):
                  for y in range(columns):
                      cstructure[x][y] = ('.')

              print('Minimapa do Cinema')
              for x in range(rows):
                  for y in range(columns):
                      print(cstructure[x][y], end='   ')
                  print()
                  
              input("Pressione enter para continuar")
              os.system('cls' if os.name == 'nt' else 'clear')
              initialized = True
    
  elif response1 == "9":
    exit()
  else:
    print("Opção não existente!")
    input("Pressione enter para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')
    
# main
def main():
  global cstructure

  cstructure =[]
  while True:
    if not initialized:
      window1()
    else:
      window2()

if __name__ == "__main__":
  main()