# Função para adicionar tarefa
def adicionar_tarefa(lista_tarefas, nova_tarefa):
    lista_tarefas.append({"tarefa": nova_tarefa, "concluida": False})

# Função para visualizar lista de tarefas
def visualizar_tarefas(lista_tarefas):
    print("### Lista de Tarefas ###")
    for idx, tarefa in enumerate(lista_tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['tarefa']} - Status: {status}")
    print("#########################")

# Função para marcar tarefa como concluída
def marcar_concluida(lista_tarefas, indice):
    if 1 <= indice <= len(lista_tarefas):
        lista_tarefas[indice - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")

# Função para editar tarefa
def editar_tarefa(lista_tarefas, indice, nova_descricao):
    if 1 <= indice <= len(lista_tarefas):
        lista_tarefas[indice - 1]["tarefa"] = nova_descricao
        print("Tarefa editada com sucesso!")
    else:
        print("Índice inválido.")

# Função para excluir tarefa
def excluir_tarefa(lista_tarefas, indice):
    if 1 <= indice <= len(lista_tarefas):
        tarefa_removida = lista_tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
    else:
        print("Índice inválido.")

# Lista para armazenar as tarefas
tarefas = []

# Exemplo de utilização
# Sistema de Gerenciamento de Tarefas

# Lista para armazenar as tarefas
tarefas = []
while True:
    # Exibição do menu
    print("\n=== Sistema de Gerenciamento de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Editar Tarefa")
    print("4. Marcar Tarefa como Concluída")
    print("5. Excluir Tarefa")
    print("6. Sair")

    # Leitura da escolha do usuário
    escolha = input("Escolha uma opção (1-6): ")

    # Adicionar Tarefa
    if escolha == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append({"tarefa": nova_tarefa, "concluida": False})
        print("Tarefa adicionada com sucesso!")

    # Visualizar Tarefas
    elif escolha == "2":
        print("\n=== Lista de Tarefas ===")
        for idx, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{idx}. {tarefa['tarefa']} - Status: {status}")

    # Editar Tarefa
    elif escolha == "3":
        idx_edicao = int(input("Digite o número da tarefa que deseja editar: "))
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        tarefas[idx_edicao - 1]["tarefa"] = nova_descricao
        print("Tarefa editada com sucesso!")

    # Marcar Tarefa como Concluída
    elif escolha == "4":
        idx_conclusao = int(input("Digite o número da tarefa concluída: "))
        tarefas[idx_conclusao - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")

    # Excluir Tarefa
    elif escolha == "5":
        idx_exclusao = int(input("Digite o número da tarefa que deseja excluir: "))
        tarefa_excluida = tarefas.pop(idx_exclusao - 1)
        print(f"Tarefa '{tarefa_excluida['tarefa']}' excluída com sucesso!")

    # Sair do Programa
    elif escolha == "6":
        print("Saindo do Sistema de Gerenciamento de Tarefas. Até logo!")
        break

    # Opção Inválida
    else:
        print("Opção inválida. Digite um número de 1 a 6.")