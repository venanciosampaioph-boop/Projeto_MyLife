# Projeto MyLife - Gerenciador de Tarefas


tarefas = []
print("===============================")
print("            MyLife")
print("===============================")

while True:

    print("\n1-Adicionar Tarefa") #Interface do usuário
    print("2-Listar Tarefas")  #Interface do usuário
    print("3-Concluir Tarefa")  #Interface do usuário
    print("4-Excluir Tarefa")  #Interface do usuário
    print("5-Sair")  #Interface do usuário
    try:

        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas numeros!!")
    if opcao == 5: 
        print("Encerrando o MyLife...")
        break
    if opcao == 1:
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    if opcao == 2:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
         print("Lista de Tarefas:")
         for  indice,tarefa in enumerate(tarefas, start=1):
            print(indice,"-",tarefa)
         
    if opcao == 3:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")

        else:
         try:
            
             numero = int(input("Digite o numero da tarefa que deseja concluir: "))
         except ValueError:
                print("Digite apenas numeros!!")
                continue   

         tarefa_concluida = tarefas.pop(numero - 1)

         print("Tarefa concluída com sucesso:", tarefa_concluida)

    if opcao == 4:
        if not tarefas:
            print("nenhuma tarefa cadastrada.")
        else:
         try:
            numero = int(input("Digite o numero da tarefa que deseja remover:"))
         except ValueError:
                    print("Digite apenas numeros!!")
                    continue
         tarefa_removida = tarefas.pop(numero - 1)
        print("Tarefa Removida.")

              

       


