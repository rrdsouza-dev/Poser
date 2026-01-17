
#Código base para treino de função

def verificação_de_entrada(idade, permissao_especial, cadastro_ativo, tentou_burlar):
    
    if tentou_burlar == True:
        return False

    if not cadastro_ativo:
     return False   
 
    if idade >= 18 or permissao_especial:
      return True
  
    return False

idade = int(input("Quantos anos tem? "))
    
permissao = input("Vc tem permissão especial? ").lower().strip() == "s"
    
cadastro = input("Tem castro ativo? ").lower().strip() == "s"
    
burlar = input("Tentou Burlar?") == "s"
    
if verificação_de_entrada (idade, permissao, cadastro, burlar):
        print("Pode entrar")
        
else:
     print("Acesso negado")
        
