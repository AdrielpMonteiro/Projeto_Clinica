import customtkinter as ctk
import tkinter as tk
from ui.tela_login import verificar_login
import tkinter.ttk as ttk
from banco_dados import listar_usuario, deletar_usuario, atualizar_usuario


def tela_agendamento(root, nome):
    root.configure(bg="black")

    frame = ctk.CTkFrame(root, fg_color="transparent")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = ctk.CTkLabel(frame, text="Agendamentos", font=("Arial", 20, "bold"), text_color="white")
    label.pack(pady=20)

    BoasVindas = f"Bem vindo à tela de agendamentos {nome} !!!"
    label = ctk.CTkLabel(frame, text=BoasVindas, font=("Arial", 20, "bold"), text_color="white")
    label.pack(pady=20)

    # Frame da tabela
    tabela_frame = tk.Frame(frame, bg="black")
    tabela_frame.pack(pady=10)

    # Título
    label_usuarios = ctk.CTkLabel(frame, text="Usuários Cadastrados", font=("Arial", 16, "bold"), text_color="white")
    label_usuarios.pack(pady=10)

    # Tabela
    tabela_usuarios = ttk.Treeview(frame, columns=("id", "nome", "email", "nascimento"), show="headings")
    tabela_usuarios.heading("id", text="ID")
    tabela_usuarios.heading("nome", text="Nome")
    tabela_usuarios.heading("email", text="Email")
    tabela_usuarios.heading("nascimento", text="Nascimento")
    tabela_usuarios.pack(pady=5)

    tabela_usuarios.column("id", width=50, anchor="center")
    tabela_usuarios.column("nome", width=150, anchor="center")
    tabela_usuarios.column("email", width=200, anchor="center")
    tabela_usuarios.column("nascimento", width=100, anchor="center")

    # Inserir dados dos usuários
    usuarios = listar_usuario()
    print("usuarios retornados", usuarios)
    for usuario in usuarios:
        tabela_usuarios.insert("", "end", values=usuario)

    # Botão voltar
    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)

    # Função deletar
    def deletar_usuario_selecionado():
        item_selecionado = tabela_usuarios.selection()
        if not item_selecionado:
            ctk.messagebox.showwarning("Aviso", "Selecione um usuário para deletar!")
            return

        id_usuario = tabela_usuarios.item(item_selecionado[0])['values'][0]
        if deletar_usuario(id_usuario):
            tabela_usuarios.delete(item_selecionado[0])
            ctk.messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
        else:
            ctk.messagebox.showerror("Erro", "Erro ao deletar usuário!")

    # Função editar
    def editar_usuario_selecionado():
        item_selecionado = tabela_usuarios.selection()
        if not item_selecionado:
            ctk.messagebox.showwarning("Aviso", "Selecione um usuário para editar!")
            return

        dados = tabela_usuarios.item(item_selecionado[0])['values']
        id_usuario, nome, email, nascimento = dados

        janela_editar = tk.Toplevel(root)
        janela_editar.title("Editar Usuário")
        janela_editar.geometry("400x300")

        tk.Label(janela_editar, text="Nome").pack()
        entry_nome = tk.Entry(janela_editar)
        entry_nome.insert(0, nome)
        entry_nome.pack()

        tk.Label(janela_editar, text="Email").pack()
        entry_email = tk.Entry(janela_editar)
        entry_email.insert(0, email)
        entry_email.pack()

        tk.Label(janela_editar, text="Nascimento").pack()
        entry_nascimento = tk.Entry(janela_editar)
        entry_nascimento.insert(0, nascimento)
        entry_nascimento.pack()

        def salvar_alteracoes():
            novo_nome = entry_nome.get()
            novo_email = entry_email.get()
            novo_nascimento = entry_nascimento.get()

            from banco_dados import atualizar_usuario  # Ou mova para o topo
            if atualizar_usuario(id_usuario, novo_nome, novo_email, novo_nascimento):
                ctk.messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
                tabela_usuarios.item(item_selecionado[0], values=(id_usuario, novo_nome, novo_email, novo_nascimento))
                janela_editar.destroy()
            else:
                ctk.messagebox.showerror("Erro", "Erro ao atualizar usuário!")

        tk.Button(janela_editar, text="Salvar", command=salvar_alteracoes).pack(pady=10)

    # Botões de ação
    button_Delete = ctk.CTkButton(frame, text="Deletar Usuário", width=200, height=40, command=deletar_usuario_selecionado)
    button_Delete.pack(pady=10)

    button_Editar = ctk.CTkButton(frame, text="Editar Usuário", width=200, height=40, command=editar_usuario_selecionado)
    button_Editar.pack(pady=10)
    ## telas - abertura de nova e encerramento de velhas.



def tela_login(root):
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.attributes("-fullscreen", True)
    nova_janela.title("Login")
    tela_login(nova_janela)
    root.destroy()
    nova_janela.mainloop()
