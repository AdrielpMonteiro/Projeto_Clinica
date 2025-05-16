import customtkinter as ctk
from banco_dados import cadastrar_usuario
import datetime
import re
from PIL import Image
import os




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



    ##Funçao nova para "Flag" de exibição de senha !!
    mostrar_senha = ctk.BooleanVar(value=False)


    label_preview = ctk.CTkLabel(frame, text="", text_color="white")
    label_preview.pack()

    ##Def para controlar o label da senha sendo digitada !!
    def atualizar_preview_senha(*args):
        senha = entry_senha.get()
        if mostrar_senha.get():
            label_preview.configure(text=senha)
        else:
            label_preview.configure(text="*" * len(senha))

    ##atualiza ao vivo instaneamente a senha !!
    entry_senha.bind("<KeyRelease>", atualizar_preview_senha)

    ##LOGICA Para opção do usuario ! mostrar ou não mostrar  a senha!
    def toggle_senha():
        if mostrar_senha.get():
            entry_senha.configure(show="*")
            mostrar_senha.set(False)
        else:
            entry_senha.configure(show="")
            mostrar_senha.set(True)
        atualizar_preview_senha()  # Atualiza a visualização também

    # Botão de mostrar/ocultar senha
    button_mostraSenha = ctk.CTkButton(frame, text="Ocultar/Mostrar senha", command=toggle_senha)
    button_mostraSenha.pack(pady=5)

    entry_nascimento = ctk.CTkEntry(frame, placeholder_text="Data de nascimento (DD/MM/AAAA)", width=300, height=40)
    entry_nascimento.pack(pady=10)

    entry_email = ctk.CTkEntry(frame, placeholder_text="Digite seu email", width=300, height=40)
    entry_email.pack(pady=10)

    label_mensagem = ctk.CTkLabel(frame,text="",text_color="white")
    label_mensagem.pack(pady=10)

    def validacao_data(data):
        try:
            datetime.datetime.strptime(data,"%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validacao_senha(senha):
        return(
            len(senha) >= 6 and
            re.search(r'[A-Z]',senha) and
            re.search(r'[@#$!$&*]',senha)
        )





    # Função para cadastrar usuário
    def cadastrar():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        nascimento = entry_nascimento.get()
        email = entry_email.get()

        # Validação simples dos campos
        if not nome or not senha or not nascimento or not email:
            label_mensagem.configure(frame,text="Preencha todos os campos!", text_color="red").pack(pady=10)
            label_mensagem.update()
            return

        if not validacao_data(nascimento):
            label_mensagem.configure(text="Data inválida !! Use o formato AAAA/MM/DD",text_color="red")
            return

        if not validacao_senha(senha):
            label_mensagem.configure(text="Senha Fraca !! Digite mais de 6 caracteres, Use Pelo menos 1 letra Maiscula ,E  1 simbolo entre( @#$)",text_color="red")
            return


        # Tenta cadastrar o usuário
        if cadastrar_usuario(nome, senha, nascimento,email):
            label_mensagem.configure(text="Cadastro realizado com sucesso!", text_color="green").pack(pady=10)
        else:
            label_mensagem.configure(text="Erro ao cadastrar", text_color="red").pack(pady=10)

    # Botões
    button_cadastrar = ctk.CTkButton(frame, text="Cadastrar", width=200, height=40, command=cadastrar)
    button_cadastrar.pack(pady=10)
    button_voltar = ctk.CTkButton(frame, text="Voltar", width=200, height=40, command=lambda: tela_login(root))
    button_voltar.pack(pady=10)
    button_profissional = ctk.CTkButton(frame, text="Cadastro de Profissionais", width=200, height=40, command=lambda: tela_medico(root))
    button_profissional.pack(pady=10)

def tela_login(root):
    from ui.tela_login import tela_login
    nova_janela = ctk.CTk()
    nova_janela.attributes("-fullscreen",True)
    nova_janela.title("Login")
    tela_login(nova_janela)
    root.destroy()
    nova_janela.mainloop()


def tela_medico(root):
    from ui.tela_medico import tela_medico
    nova_janela = ctk.CTk()
    nova_janela.attributes("-fullscreen",True)
    nova_janela.title("Cadastro de Profissionais")
    tela_medico(nova_janela)
    root.destroy()
    nova_janela.mainloop()
    root.destroy()