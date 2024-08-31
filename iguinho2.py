import random

class Questao:
    def __init__(self, texto, alternativas, resposta_correta):
        self.texto = texto
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta

    def exibir_questao(self):
        print(self.texto)
        for i, alternativa in enumerate(self.alternativas, 1):
            print(f"{i}. {alternativa}")

    def verificar_resposta(self, resposta):
        return self.alternativas[resposta - 1] == self.resposta_correta

questao1 = Questao("Qual a cor do céu?", ["Azul", "Verde", "Vermelho", "Amarelo"], "Azul")
questao2 = Questao("Quanto é 2 + 2?", ["1", "2", "3", "4"], "4")
questao3 = Questao("Qual o nome do planeta?", ["Marte", "Terra", "Vênus", "Júpiter"], "Terra")
questao4 = Questao("Qual o maior oceano?", ["Atlântico", "Pacífico", "Índico", "Ártico"], "Pacífico")
questao5 = Questao("Qual o animal mais rápido?", ["Leão", "Tigre", "Guepardo", "Elefante"], "Guepardo")
questao6 = Questao("Qual o maior país?", ["China", "EUA", "Brasil", "Rússia"], "Rússia")
questao7 = Questao("Qual a capital do Brasil?", ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"], "Brasília")
questao8 = Questao("Quem escreveu 'Dom Quixote'?", ["Miguel de Cervantes", "William Shakespeare", "Camões", "Machado de Assis"], "Miguel de Cervantes")
questao9 = Questao("Qual o menor planeta?", ["Marte", "Terra", "Mercúrio", "Netuno"], "Mercúrio")
questao10 = Questao("Qual o maior mamífero?", ["Elefante", "Baleia Azul", "Girafa", "Rinoceronte"], "Baleia Azul")

todas_questoes = [questao1, questao2, questao3, questao4, questao5, questao6, questao7, questao8, questao9, questao10]

questoes_sorteadas = random.sample(todas_questoes, 5)

pontuacao = 0

for questao in questoes_sorteadas:
    questao.exibir_questao()
    
    while True:
        try:
            resposta = int(input("Escolha a alternativa correta (1, 2, 3 ou 4): "))
            if resposta not in [1, 2, 3, 4]:
                print("Só é permitido escolher as opções digitando 1, 2, 3 ou 4.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")
    
    if questao.verificar_resposta(resposta):
        print("Resposta correta!\n")
        pontuacao += 1
    else:
        print(f"Resposta errada! A resposta correta é: {questao.resposta_correta}\n")

print(f"Você acertou {pontuacao} de {len(questoes_sorteadas)} questões.")
