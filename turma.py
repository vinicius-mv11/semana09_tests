class Turma:
    def __init__(self):
        self.turma = []
        self.menorNota = None
        self.maiorNota = None

    def cadastrarAlunos(self, alunos):
        for i in alunos:
            self.turma.append(i)
            if (self.menorNota == None):
                self.menorNota = i

            if (self.maiorNota == None):
                self.maiorNota = i

            if (self.menorNota.nota > i.nota):
                self.menorNota = i
            elif (self.maiorNota.nota < i.nota):
                self.maiorNota = i

    def mostrarAlunos(self):
        print('Quantidade de alunos:', len(self.turma))
        for x in self.turma:
            print(x.mostrarAluno())
