from datetime import datetime

from trabalho.models.genero import Genero
from trabalho.models.producao import Producao
from django.contrib.auth import get_user_model


# menu
# 1 Guardar dados
# 2 Criar SuperUsuario
# 3 Atualizar / Consultar
# 4 Deletar
# 5 Consultar 1 registro
# 6 Consultar (5 elementos)
# 0 Sair

def gerar_dados():
    i = 1
    filmes = []
    while i <= 15:
        filme = {
            'titulo': 'Filme ' + str(i),
            'sinopse': 'Sinopse do Filme ' + str(i),
            'genero': Genero.ACTION,
            'classificacao': 'Livre',
            'quantidade_avaliacoes': i,
            'nota': i if i <= 10 else i - 6,
            'duracao': datetime.strptime('02:00:00', '%H:%M:%S').time(),
            'popularidade': 50 + i,
            'especificacoes': 'Especificação do Filme ' + str(i),
            'data_lancamento': datetime.now().date()
        }

        filmes.append(filme)
        i += 1

    # Instanciando e salvando os exemplos de filmes no banco de dados
    for filme in filmes:
        novo_filme = Producao.objects.create(
            titulo=filme['titulo'],
            sinopse=filme['sinopse'],
            genero=filme['genero'].value,  # Acessa o valor do enum
            classificacao=filme['classificacao'],
            quantidade_avaliacoes=filme['quantidade_avaliacoes'],
            nota=filme['nota'],
            duracao=filme['duracao'],
            popularidade=filme['popularidade'],
            especificacoes=filme['especificacoes'],
            data_lancamento=filme['data_lancamento']
        )
        novo_filme.save()
    print("Dados salvos com sucesso!")


def criar_superuser():
    print("Opção 2 selecionada: Criar SuperUsuário")
    User = get_user_model()
    User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs2023')
    print("Superuser criado: user=ifrs, password=ifrs2023")


def atualizar_consultar():
    print("Opção 3 selecionada: Atualizar / Consultar")
    filmes = Producao.objects.all()
    for filme in filmes:
        print(f"Id: {filme.id} - {filme.titulo}")

    id_filme = int(input("Deseja modificar o nome de qual filme? {id}"))
    titulo = int(input("Qual o novo nome? "))

    filme = Producao.objects.get(id=id_filme)
    filme.titulo = titulo
    filme.save()
    print("Alterado com sucesso!")
    print(f"Id: {filme.id} - {filme.titulo}")


def deletar():
    print("Opção 4 selecionada: Deletar")
    filmes = Producao.objects.all()
    for filme in filmes:
        print(f"Id: {filme.id} - {filme.titulo}")

    id_filme = int(input("Digite o id do filme que deseja deletar: "))
    filme = Producao.objects.get(id=id_filme)
    filme.delete()
    print("Deletado com sucesso!")


def consultar_registro():
    print("Opção 5 selecionada: Consultar 1 registro")
    filme = Producao.objects.all()
    for filme in filme:
        print(f"Id: {filme.id} - {filme.titulo}")

    id_filme = int(input("Digite um id? {id}"))
    filme = Producao.objects.get(id=id_filme)

    print(f"Id: {filme.id} - {filme.titulo}")


def consultar_5_elementos():
    print("Opção 6 selecionada: Consultar (5 elementos)")
    # Coloque aqui a lógica para consultar 5 elementos
    filme = Producao.objects.all()
    for filme in filme[:5]:
        print(f"Id: {filme.id} - {filme.titulo}")


def deletar_todos():
    filmes = Producao.objects.all()
    for filme in filmes:
        filme.delete()
    print("Deletados com sucesso!")


def __main__():
    while True:
        print("\n=== MENU ===")
        print("1. Guardar dados")
        print("2. Criar SuperUsuário")
        print("3. Atualizar / Consultar")
        print("4. Deletar")
        print("5. Consultar 1 registro")
        print("6. Consultar (5 elementos)")
        print("7. Deletar todos os elementos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerar_dados()
        elif opcao == "2":
            criar_superuser()
        elif opcao == "3":
            atualizar_consultar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            consultar_registro()
        elif opcao == "6":
            consultar_5_elementos()
        elif opcao == "7":
            deletar_todos()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

    print("Fim do programa.")


if __name__ == "__main__":
    __main__()
