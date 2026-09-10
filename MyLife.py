tarefas = []
print("===============================")
print("            MyLife")
print("===============================")

while True:
    print("\n1-Adicionar Tarefa") #Interface do usuário
    print("2-Listar Tarefas")  #Interface do usuário
    print("3-Concluir Tarefa")  #Interface do usuário
    print("4-Sair")  #Interface do usuário
    opcao = int(input("Escolha uma opção: "))
    if opcao == 4: 
        print("Encerrando o MyLife...")
        break
    if opcao == 1:
        tarefa = input("Digite a Tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")    
    if opcao == 2:
        print("Lista de Tarefas:")
        for  indice,tarefa in enumerate(tarefas, start=1):
            print(indice,"-",tarefa)
         
    if opcao == 3:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")

        else:
            numero = int(input("Digite o numero da tarefa que deseja concluir: "))

            tarefa_concluida = tarefas.pop(numero - 1)

            print("Tarefa concluída com sucesso:", tarefa_concluida)
        
      
       


