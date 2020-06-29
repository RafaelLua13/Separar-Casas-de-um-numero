# Separar um número inteiro independente de seu tamanho

# Nome do projeto: Separar Casas de um número
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Vetores
# Autor: Rafael Lua - rafaellua13




# Usuário deve escolher o numero inteiro positivo de qualquer tamanho

num = int(input("Digite o número: ")) 




aux = num
cont = 0

while (aux >= 1): # Contar numero de casas do número
  aux = aux/10
  cont += 1
  
var = 0
var2 = 0
cont2 = 1

varHelp = 0

# Definir vetores das casas, seus valores significativos e seus valores reais

casas = [0]*cont    
valores = [0]*cont
reais = [0]*cont

print("\n\n\nValor Original: ",num)
print()

helpOficial = cont

for x in range(cont):
  
  var = num%(10**(cont2))
  
  var2 = (var - varHelp)/10**(cont2-1)
  #print(int(var2), end = " ")

  valores[helpOficial-1] = var - varHelp;
  reais[helpOficial-1] = var;
  varHelp = var

  casas[helpOficial-1] = int(var2)
  helpOficial -= 1


  cont2 += 1
  
  


print()
print()
print("Casas: ",casas)
print("Valores das casas: ",valores)
print("Valores Reais: ", reais)
print()
print()

