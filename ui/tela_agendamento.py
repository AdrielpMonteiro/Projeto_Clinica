import customtkinter as ctk
import tkinter as tk
from ui.tela_login import verificar_login
import tkinter.ttk as ttk
from banco_dados import listar_usuario


def tela_agendamento(root,nome):
    root.configure(bg="black")

    frame = ctk.CTkFrame(root,fg_color="transparent")
    frame.pack(expand=True,fill="both",padx=20,pady=20)

    label = ctk.CTkLabel(frame,text="Agendamentos",font=("Arial",20,"bold"),text_color="white")
    label.pack(pady=20)

    BoasVindas = f"Bem vindo a tela de agendamentos {nome} !!!"
    label = ctk.CTkLabel(frame,text=BoasVindas,font=("Arial",20,"bold"),text_color="white")
    label.pack(pady=20)


    # Frame da tabela
    tabela_frame = tk.Frame(frame, bg="black")
    tabela_frame.pack(pady=10)


    ### Nova tabela para mostrar os usuários cadastrados
    label_usuarios = ctk.CTkLabel(frame, text="Usuários Cadastrados", font=("Arial", 16, "bold"), text_color="white")
    label_usuarios.pack(pady=10)

    tabela_usuarios = ttk.Treeview(frame, columns=("id", "nome", "email", "nascimento"), show="headings")
    tabela_usuarios.heading("id", text="ID")
    tabela_usuarios.heading("nome", text="Nome")
    tabela_usuarios.heading("email", text="Email")
    tabela_usuarios.heading("nascimento", text="Nascimento")
    tabela_usuarios.pack(pady=5)
    ## centralizando os dados
    tabela_usuarios.column("id",width=50,anchor="center")
    tabela_usuarios.column("nome",width=150,anchor="center")
    tabela_usuarios.column("email",width=200,anchor="center")
    tabela_usuarios.column("nascimento",width=100,anchor="center")

    # Inserir os dados dos usuários na tabela
    usuarios = listar_usuario()
    print("usuarios retornados",usuarios)
    for usuario in usuarios:
        tabela_usuarios.insert("", "end", values=usuario)

    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)
    button_Delete = ctk.CTkButton(frame,text="Delete usuário",width=200,height=40)
    button_Delete.pack(pady=10)


def tela_login(root):
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.attributes("-fullscreen",True)
    nova_janela.title("Login")
    tela_login(nova_janela)
    root.destroy()
    nova_janela.mainloop()