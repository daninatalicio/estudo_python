def media_notas(disciplinas, notas):
  
  nota_por_disciplina = list(zip(disciplinas,notas)) #transforma duas listas em uma lista de tuplas
  dict_medias = {}
  count_disciplinas = {}
  

  for chave, valor in nota_por_disciplina:
    dict_medias.setdefault(chave, []).append(valor) #coloca as chaves com os valores em lista

  for chave, valor in dict_medias.items():
    dict_medias[chave] = sum(valor) #soma os valores de cada chave

#vendo quantas vezes a disciplina se repete para poder dividir 
  for item in disciplinas:
      count = count_disciplinas.get(item,None)
      nao_existe = count == None
      if nao_existe:
        count_disciplinas[item] = 1
      else:
        count = count + 1
        count_disciplinas[item] = count

  for chave, somatorio_notas in dict_medias.items():
    ocorrencias_disciplinas = count_disciplinas[chave]
    media = somatorio_notas / ocorrencias_disciplinas
    dict_medias[chave] = media
 
 

  return dict_medias
  
def media_notas2(disciplinas, notas):

  nota_por_disciplina = list(zip(disciplinas,notas))
  disciplina_to_nota = {}

  for tupla in nota_por_disciplina:
    # disciplina = tupla[0]
    # nota = tupla[1]
    disciplina,nota = tupla
    notas = disciplina_to_nota.get(disciplina,None)
    if notas is None:
      notas = []
    notas.append(nota)
    disciplina_to_nota[disciplina] = notas

  disciplinas_to_media = {}
  
  for disciplina, notas in disciplina_to_nota.items():
    somatorio_notas = sum(notas)
    ocorrencia_disciplinas = len(notas)
    disciplinas_to_media[disciplina] = somatorio_notas / ocorrencia_disciplinas

  return disciplinas_to_media
  





 







  
  







  #{'Matematica': [7.5, 10, 3.5], 'Fisica': [9.5, 5.0], 'Portugues': [4.5, 6.5]}
  #{'Matematica': 21.0, 'Fisica': 14.5, 'Portugues': 11.0} 
  # {'Matematica': 3, 'Fisica': 2, 'Portugues': 2}

# def media_notas(disciplinas, notas):
#     count_disciplinas = {}    
#             
#     for item in disciplinas:
#       count = count_disciplinas.get(item,None)
#       nao_existe = count == None
#       if nao_existe:
#         count_disciplinas[item] = 1
#       else:
#         count = count + 1
#         count_disciplinas[item] = count
    
#     print(count_disciplinas, notas_por_disciplinas)
    