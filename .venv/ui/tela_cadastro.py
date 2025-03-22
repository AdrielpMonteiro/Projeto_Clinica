import customtkinter as ctk
from banco_dados import cadastrar_usuario

def tela_cadastro(root):
    root.configure(bg="black")

    frame = ctk.CTkFrame(root, fg_color="transparent")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = ctk.CTkLabel(frame, text="Cadastro", font=("Arial", 24, "bold"), text_color="white")
    label.pack(pady=20)


    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Usuário", width=300, height=40)
    entry_usuario.pack(pady=10)

    entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*", width=300, height=40)
    entry_senha.pack(pady=10)

    entry_nascimento = ctk.CTkEntry(frame, placeholder_text="Data de nascimento (AAAA-MM-DD)", width=300, height=40)
    entry_nascimento.pack(pady=10)

    entry_email = ctk.CTkEntry(frame, placeholder_text="Digite seu email", width=300, height=40)
    entry_email.pack(pady=10)

    # Função para cadastrar usuário
    def cadastrar():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        nascimento = entry_nascimento.get()
        email = entry_email.get()

        # Validação simples dos campos
        if not nome or not senha or not nascimento or not email:
            ctk.CTkLabel(frame, text="Preencha todos os campos!", text_color="red").pack(pady=10)
            return

        # Tenta cadastrar o usuário
        if cadastrar_usuario(nome, senha, nascimento,email):
            ctk.CTkLabel(frame, text="Cadastro realizado com sucesso!", text_color="green").pack(pady=10)
        else:
            ctk.CTkLabel(frame, text="Erro ao cadastrar", text_color="red").pack(pady=10)

    # Botões
    button_cadastrar = ctk.CTkButton(frame, text="Cadastrar", width=200, height=40, command=cadastrar())
    button_cadastrar.pack(pady=10)
    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)
    button_profissional = ctk.CTkButton(frame, text="Cadastro de Profissionais", width=200, height=40, command=lambda: tela_medico(root))
    button_profissional.pack(pady=10)

def tela_login(root):
    root.destroy()
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.geometry("800x600")
    nova_janela.title("Login")
    tela_login(nova_janela)
    nova_janela.mainloop()

def tela_medico(root):
    root.destroy()
    from ui.tela_medico import tela_medico
    nova_janela = ctk.CTk()
    nova_janela.geometry("800x600")
    nova_janela.title("Cadastro de Profissionais")
    tela_medico(nova_janela)
    nova_janela.mainloop()