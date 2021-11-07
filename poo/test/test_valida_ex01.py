from poo.ex_01 import Aluno, Escola, AlunoReprovado

def test_valida_maior_nota():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',7.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',5))
    disciplina = 'Matemática'
    validar_maior_nota = escola.maior_nota(disciplina = disciplina)
    assert validar_maior_nota == 'Júlia'

def test_valida_maior_nota_1():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',7.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',5))
    disciplina = 'Física'
    validar_maior_nota = escola.maior_nota(disciplina = disciplina)
    assert validar_maior_nota == 'Júlia'

def test_valida_maior_nota_2():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',7.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',5))
    disciplina = 'Português'
    validar_maior_nota = escola.maior_nota(disciplina = disciplina)
    assert validar_maior_nota == 'Lucas'


def test_valida_alunos_reprovados():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    alunos_reprovados = escola.alunos_reprovados()
    primeiro_aluno_reprovado = alunos_reprovados[0]
    segundo_aluno_reprovado = alunos_reprovados[1]
    terceiro_aluno_reprovado = alunos_reprovados[2]
    assert primeiro_aluno_reprovado.nome == 'Lucas'
    assert primeiro_aluno_reprovado.disciplina == 'Matemática'
    assert segundo_aluno_reprovado.nome == 'Júlia'
    assert segundo_aluno_reprovado.disciplina == 'Português'
    assert terceiro_aluno_reprovado.nome == 'Lucas'
    assert terceiro_aluno_reprovado.disciplina == 'Física'

    # alunos_reprovados_esperados = [AlunoReprovado('Lucas','Matemática'),AlunoReprovado('Júlia','Português'),AlunoReprovado('Lucas','Física')]
    # for idx, aluno in enumerate(alunos_reprovados):
    #     assert aluno.nome == alunos_reprovados_esperados[idx].nome
    #     assert aluno.disciplina == alunos_reprovados_esperados[idx].disciplina


        
def test_genero_maior_nota():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    disciplina = 'Português'
    validar_genero_maior_nota = escola.genero_maior_nota(disciplina = disciplina)
    assert validar_genero_maior_nota == 'masculino'

def test_genero_maior_nota_2():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    disciplina = 'Matemática'
    validar_genero_maior_nota = escola.genero_maior_nota(disciplina = disciplina)
    assert validar_genero_maior_nota == 'feminino'

def test_genero_maior_nota_3():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    disciplina = 'Português'
    validar_genero_maior_nota = escola.genero_maior_nota(disciplina = disciplina)
    assert validar_genero_maior_nota == 'feminino'

def test_percentual_genero():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    disciplina = 'Matemática'
    validar_percentual_genero = escola.percentual_genero(disciplina = disciplina)
    assert validar_percentual_genero == {'feminino': 0.5 , 'masculino': 0.5}

def test_percentual_genero_2():
    escola = Escola()
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Matemática',4.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Física',9.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Português',4.5))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Português',6.5))
    escola.adiciona_aluno(Aluno('Ra222','Júlia','feminino','Matemática',10))
    escola.adiciona_aluno(Aluno('Ra111','Lucas','masculino','Física',2))
    escola.adiciona_aluno(Aluno('Ra111','Pedro','masculino','Física',2))
    escola.adiciona_aluno(Aluno('Ra111','Lou','masculino','Física',2))
    disciplina = 'Física'
    validar_percentual_genero = escola.percentual_genero(disciplina = disciplina)
    assert validar_percentual_genero == {'feminino': 0.25 , 'masculino': 0.75}