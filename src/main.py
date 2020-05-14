from model.Game import Game

def main():
    print("Teste de Primeiro Print")
    g = Game(["ABC","Carro"],"Primeira Partida")
    print("Palavra 1: {}".format(g.palavras[0]))
    print("{}".format(g.partida))
    return None


main()
