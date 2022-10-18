import requests
import pandas as pd
import collections

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
#url = sys.argv[1]#O link sera fornecido como parametro no momento de execucao do script via terminal Ex: python main_resolucao.py 'https://ser.....' - sys.argv[1] = parametro  e sys.argv[0] = script

respota = requests.get(url, verify=False) #verify=False para não validar o SSL
r_text = respota.text 

#removendo caracteres nao necessarias
r_text = r_text.replace('\\r\\n', '')
r_text = r_text.replace('"\r\n}', '')
r_text = r_text.replace('{\r\n} "html": "', '')


#Atravez do codigo HTML, ira analisar e reconhecer automaticamente as tabelas com tag <tr>
df = pd.read_html(r_text, encoding='utf-8')[0] #'[0]' =  transforma as informacoes do formato de lista para o formato de dataframe
#df = df[0].copy

#Corrgindo nome de todas as colunas
new_columns = df.columns
new_columns = list(i.replace('\\r\\n','') for i in new_columns)
df.columns = new_columns

#removendo linhas nulas
#compara os valores da coluna "Bola1" com elas mesma "Bola1", quando comparamos "Bola1" = null, o resultado nunca será veradeiro(true)
df = df[df["Bola1"] == df["Bola1"]]

#-------------------------------------------------------------#
nr_pop = list(range(1, 26))
lista_colunas = ['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']
lista_primos = [2, 3, 5, 7,  11, 13, 17, 19, 23]

dict_valores = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0} #Quantidade de cada numero sorteado

lista_quantidades = []
for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for coluna in lista_colunas:
      if row[coluna] % 2 == 0:
        v_pares +=1
      else:
        v_impares +=1

      if row[coluna] in lista_primos:
        v_primos +=1

      dict_valores[row[coluna]] = dict_valores[row[coluna]] + 1 #Quantidade de vezes que um numero apareceu

    lista_quantidades.append(f'{v_pares}p,{v_impares}i,{v_primos}np')#combinacoes de pares, impares e primos linha a linha
    
    
#transforma dicionario em lista ordenada
lista_orderm_values = []
for i in sorted(dict_valores, key = dict_valores.get): #ordena o dicionario
    #print(i,dict_valores[i])
    lista_orderm_values.append([i,dict_valores[i]]) #transforma dicionario em lista
print('----- Lista ordenada de numeros mais sorteados -----')
print(lista_orderm_values)


#Frequencia/Quantidade de vezes que uma combinacao apareceu
counter = collections.Counter(lista_quantidades) #forma um dicionario com a frequencia | em sql seria um group by com sum
resultado = pd.DataFrame(counter.items(), columns=['Combinacao','Frequencia'])  #Transforma dicionario em data frame, quebra a chave e valor dele em 'Cominacao','Frequencia'
resultado['d_freq'] =  (resultado['Frequencia']/resultado['Frequencia'].sum())*100 #Coluna de Percentual de frequencia
resultado = resultado.sort_values(by='d_freq') #ordenando DF
print('----- Frequencia de combinacoes -----')
print(resultado)


#Apresentacao dos resultado
print(f'''
O Numero mais frequente é o {lista_orderm_values[-1][0]} com {lista_orderm_values[-1][1]} Aparicoes\n
O Numero menos frequente é o {lista_orderm_values[0][0]} com {lista_orderm_values[0][1]} Aparicoes\n
A Combinacao de numeros pares, impares e primos mais frequentes é '{resultado['Combinacao'].values[-1]}' com a % de frequencia igual a {resultado["d_freq"].values[-1]:.2f}
''')