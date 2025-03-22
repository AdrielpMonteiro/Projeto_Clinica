import customtkinter as ctk
from banco_dados import cadastrar_profissional




def tela_medico(root):
    root.configure(bg="black")

    frame = ctk.CTkFrame(root, fg_color="transparent")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = ctk.CTkLabel(frame, text="Cadastro Profissional", font=("Arial", 24, "bold"), text_color="white")
    label.pack(pady=20)



    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Usuário Medico", width=300, height=40)
    entry_usuario.pack(pady=10)
    entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*", width=300, height=40)
    entry_senha.pack(pady=10)
    entry_crf = ctk.CTkEntry(frame, placeholder_text="Digite seu CRF", width=300, height=40)
    entry_crf.pack(pady=10)
    entrt_email = ctk.CTkEntry(frame, placeholder_text="Digite seu email", width=300 , height=40)
    entrt_email.pack(pady=10)
    entry_especialidade = ctk.CTkEntry(frame,placeholder_text="digite sua especialidade",width=300 , height=40)
    entry_especialidade.pack(pady=10)

    def cadastrar():
        nome =entry_usuario.get()
        senha = entry_senha.get()
        email = entrt_email.get()
        crf = entry_crf.get()
        especialidade = entry_especialidade.get()

        if not nome or not senha or not crf or not email or not especialidade:
            ctk.CTkLabel(frame,text="Preencha todos os campos!",text_color="red").pack(pady=10)
            return

        if cadastrar_profissional(nome,senha,crf,email,especialidade):
            ctk.CTkLabel(frame,text="Cadastro Realizado com sucesso",text_color="green").pack(pady=10)
        else:
            ctk.CTkLabel(frame,text="Erro ao cadastrar Proffisional",text_color="red").pack(pady=10)



    button_cadastrar = ctk.CTkButton(frame, text="Cadastrar Profissional", width=200, height=40 ,command=cadastrar)
    button_cadastrar.pack(pady=10)

    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)




def tela_login(root):
    root.destroy()
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.geometry("800x600")  # Garante que a tela de cadastro tenha o mesmo tamanho
    nova_janela.title("Cadastro")
    tela_login(nova_janela)
    nova_janela.mainloop()