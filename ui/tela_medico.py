import customtkinter as ctk
from banco_dados import cadastrar_profissional
import re





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


    mostrar_senha = ctk.BooleanVar(value=False)


    label_preview = ctk.CTkLabel(frame, text="", text_color="white")
    label_preview.pack()


    def atualizar_preview_senha(*args):
        senha = entry_senha.get()
        if mostrar_senha.get():
            label_preview.configure(text=senha)
        else:
            label_preview.configure(text="*" * len(senha))

    entry_senha.bind("<KeyRelease>", atualizar_preview_senha)


    def toggle_senha():
        if mostrar_senha.get():
            entry_senha.configure(show="*")
            mostrar_senha.set(False)
        else:
            entry_senha.configure(show="")
            mostrar_senha.set(True)
        atualizar_preview_senha()


    button_mostraSenha = ctk.CTkButton(frame, text="Ocultar/Mostrar senha", command=toggle_senha)
    button_mostraSenha.pack(pady=5)

    entry_crf = ctk.CTkEntry(frame, placeholder_text="Digite seu CRF", width=300, height=40)
    entry_crf.pack(pady=10)
    entrt_email = ctk.CTkEntry(frame, placeholder_text="Digite seu email", width=300 , height=40)
    entrt_email.pack(pady=10)
    entry_especialidade = ctk.CTkEntry(frame,placeholder_text="digite sua especialidade",width=300 , height=40)
    entry_especialidade.pack(pady=10)

    label_mensagem = ctk.CTkLabel(frame,text="",text_color="white")
    label_mensagem.pack(pady=10)

    def validacao_crf(crf):
        try:
            int(crf)
            return True
        except ValueError:
            return False


    def validacao_senha(senha):
        return(
            len(senha) >= 6 and
            re.search(r'[A-Z]',senha) and
            re.search(r'[@#$!&%*]',senha)
        )

    def cadastrar():
        nome =entry_usuario.get()
        senha = entry_senha.get()
        crf = entry_crf.get()
        email = entrt_email.get()
        especialidade = entry_especialidade.get()


        if not nome or not senha or not crf or not email or not especialidade:
            label_mensagem.configure(text="Preencha todos os campos!",text_color="red").pack(pady=10)
            label_mensagem.update()
            return

        if not validacao_crf(crf):
            label_mensagem.configure(text="CRF Inválidos , Digite somente numeros!",text_color="red")
            return


        if not validacao_senha(senha):
            label_mensagem.configure(text="senha fraca, digite 6 caracteres ,use 1 letra maiscula , 1 simbolo entre( @#$)",text_color="red")
            return



        if cadastrar_profissional(nome,senha,crf,email,especialidade):
            label_mensagem.configure(text="Cadastro Realizado com sucesso",text_color="green").pack(pady=10)
        else:
            label_mensagem.configure(text="Erro ao cadastrar Proffisional",text_color="red").pack(pady=10)



    button_cadastrar = ctk.CTkButton(frame, text="Cadastrar Profissional", width=200, height=40 ,command=cadastrar)
    button_cadastrar.pack(pady=10)

    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)




def tela_login(root):
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.attributes("-fullscreen",True)
    nova_janela.title("Cadastro")
    tela_login(nova_janela)
    root.destroy()
    nova_janela.mainloop()
