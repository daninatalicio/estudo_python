from typing import Counter


class Aluno(object):

    def __init__(self, RA, nome, genero, disciplina, nota):
        self.RA = RA
        self.nome = nome
        self.genero = genero
        self.disciplina = disciplina
        self.nota = nota

class AlunoReprovado(object):

    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class Escola(object):

    def __init__(self):
        self.alunos = []

    def adiciona_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def maior_nota(self, disciplina: str):
        maior_nota = 0
        aluno_maior_nota = None
        for aluno in self.alunos:
            if disciplina == aluno.disciplina:
                if aluno.nota > maior_nota:
                    maior_nota = aluno.nota
                    aluno_maior_nota = aluno.nome
        return aluno_maior_nota
                    
    def alunos_reprovados(self):    
        alunos_reprovados = []
        for aluno in self.alunos:
            if aluno.nota < 5:
                aluno_reprovado = AlunoReprovado(aluno.nome, aluno.disciplina)
                alunos_reprovados.append(aluno_reprovado)
        return alunos_reprovados

    def genero_maior_nota(self, disciplina: str):
        maior_nota = 0
        genero_aluno_nota_mais_alta = None
        for aluno in self.alunos:
            if disciplina == aluno.disciplina:
                if aluno.nota > maior_nota:
                    maior_nota = aluno.nota
                    genero_aluno_nota_mais_alta = aluno.genero
        return genero_aluno_nota_mais_alta

    def percentual_genero(self, disciplina: str):
        count_fem = 0
        count_masc = 0
        count = 0
        percentual_fem = 0
        percentual_masc = 0
        percentual_genero = {}
        for aluno in self.alunos:
            if disciplina == aluno.disciplina:
                if aluno.genero == 'feminino':
                    count_fem = count_fem + 1
                else:
                    count_masc = count_masc + 1
        count = count_masc + count_fem
        percentual_fem = count_fem/count
        percentual_masc = count_masc/count
        percentual_genero['feminino'] = percentual_fem
        percentual_genero['masculino'] = percentual_masc   
        return percentual_genero