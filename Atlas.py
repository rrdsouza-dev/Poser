def veri_idade(idade):
 return idade >= 18

idade = int(input("Qual sua idade?: "))

if veri_idade(idade):
    print("Maior de idade")
    
else:
    print("Menor de idade")