'''função para calcular se um número é primo'''
def eprimo(n):
    
    #para os menores números, apenas isso basta
    if n == 2 or n == 3 or n == 5:    
        return True
    if n == 4:
        return False
    
    #para números maiores, foi implementado os eguinte algoritmo de verificação
    else: 
        h = 2
        for j in range(2,round(n**(1/2))+1): #a lógica é simples, o range irá até raiz quadrada do número mais 1,
                                             #se o número não divisível por nenhum desses, é primo.

            if n%j == 0:
                #não é primo
                return False
                break

            if h == round(n**(1/2)):

                #é primo
                return True
            


            h = h + 1

'''função para calcular a lista com 4 primos consecutivos'''
def listaprimos(lista_anterior): #a primeira entrada será sempre uma entrada dos primos primos sequenciais [2,3,5,7]
    
    lista_anterior.pop(0)
    n = lista_anterior[2]
    n = n+1
    
    while eprimo(n)==False: #enquanto o número não for primo, continua gerando um número
        
        eprimo(n)
        n= n+1
    
    '''após descobrir o próximo primo, este é adicionado ao final da lista'''
    lista_anterior.append(n)


    return lista_anterior


'''Função para calcular o modo 2'''
def modo2(n):
    
    
    lista = [2,3,5,7]                                             #inicia com a primeira sequeência de primos.
    while lista[0]**2+lista[1]**2+lista[2]**2+lista[3]**2 <= n:   #loop onde, enquanto a somatória dos quadrados
                                                                  #for menor ou igual ao valor de n, ele continua.
        

        if lista[0]**2+lista[1]**2+lista[2]**2+lista[3]**2 == n:  #se a soma for n, finaliza e termina o loop.
            
            return True #O segundo retorno foi retirado pois a lista de primos será utilizada
            break       #para descobrir se está funcionando
        lista = listaprimos(lista)
    if lista[0]**2+lista[1]**2+lista[2]**2+lista[3]**2 > n:       # se o loop acabar, quer dizer que não exite 
                                                                  #soma do quadrado dos primos igual a n, logo
        return False                                              #retorna falso.



print(modo2(569))
print(modo2(2020))
print(modo2(15))
print(modo2(100))




























































































































































