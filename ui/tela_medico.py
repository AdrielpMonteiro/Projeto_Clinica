import customtkinter as ctk



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

    button_cadastrar = ctk.CTkButton(frame, text="Cadastrar Profissional", width=200, height=40)
    button_cadastrar.pack(pady=10)
    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)
    button_profissional =ctk.CTkButton(frame , text="Cadastro de Profissionais" , width=200, height=40 ,command=lambda:tela_medico(root))
    button_profissional.pack(pady=10)



def tela_login(root):
    root.destroy()
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.geometry("800x600")  # Garante que a tela de cadastro tenha o mesmo tamanho
    nova_janela.title("Cadastro")
    tela_login(nova_janela)
    nova_janela.mainloop()