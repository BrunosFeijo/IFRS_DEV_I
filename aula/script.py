from random import random

from exemplo.models.example import Example
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
    print("Opção 1 selecionada: Guardar dados")
    times = ["Grêmio", "Internacional", "Flamengo", "Palmeiras", "São Paulo",
             "Corinthians", "Fluminense", "Vasco", "Botafogo", "Atlético Mineiro",
             "Cruzeiro", "Santos", "Athletico Paranaense", "Bahia", "Ceará", "São Caetano"]

    for nome_time in times:
        novo_time = Example(nome=nome_time)
        novo_time.torcedores = random.randint(100, 100000)
        novo_time.save()
    print("Dados salvos com sucesso!")


def criar_superuser():
    print("Opção 2 selecionada: Criar SuperUsuário")
    User = get_user_model()
    User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs2023')
    print("Superuser criado: user=ifrs, password=ifrs2023")


def atualizar_consultar():
    print("Opção 3 selecionada: Atualizar / Consultar")
    times = Example.objects.all()
    for time in times:
        print(f"Id: {time.id} - {time.nome}: {time.torcedores}")

    id_time = int(input("Deseja informar a quantidade de torcedores para qual time? {id}"))
    torcedores = int(input("Quantos torcedores? "))

    time = Example.objects.get(id=id_time)
    time.torcedores = torcedores
    time.save()
    print("Alterado com sucesso!")
    print(f"Id: {time.id} - {time.nome}: {time.torcedores}")


def deletar():
    print("Opção 4 selecionada: Deletar")
    times = Example.objects.all()
    for time in times:
        print(f"Id: {time.id} - {time.nome}: {time.torcedores}")

    id_time = int(input("Digite o id do time que deseja deletar: "))
    time = Example.objects.get(id=id_time)
    time.delete()
    print("Deletado com sucesso!")


def consultar_registro():
    print("Opção 5 selecionada: Consultar 1 registro")
    times = Example.objects.all()
    for time in times:
        print(f"Id: {time.id} - {time.nome}: {time.torcedores}")

    id_time = int(input("Digite um id? {id}"))
    time = Example.objects.get(id=id_time)

    print(f"Id: {time.id} - {time.nome}: {time.torcedores}")


def consultar_5_elementos():
    print("Opção 6 selecionada: Consultar (5 elementos)")
    # Coloque aqui a lógica para consultar 5 elementos
    times = Example.objects.all()
    for time in times[:5]:
        print(f"Id: {time.id} - {time.nome}: {time.torcedores}")


def deletar_todos():
    times = Example.objects.all()
    for time in times:
        time.delete()
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
