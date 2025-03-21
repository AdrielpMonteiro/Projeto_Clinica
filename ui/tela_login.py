import customtkinter as ctk
from ui.tela_cadastro import tela_cadastro

def tela_login(root):
    root.configure(bg="black")

    frame = ctk.CTkFrame(root, fg_color="transparent")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = ctk.CTkLabel(frame, text="Login", font=("Arial", 24, "bold"), text_color="white")
    label.pack(pady=20)

    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Usuário", width=300, height=40)
    entry_usuario.pack(pady=10)

    entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*", width=300, height=40)
    entry_senha.pack(pady=10)

    button_login = ctk.CTkButton(frame, text="Entrar", width=200, height=40)
    button_login.pack(pady=10)

    button_cadastro = ctk.CTkButton(frame, text="Cadastre-se", width=200, height=40, command=lambda: abrir_tela_cadastro(root))
    button_cadastro.pack(pady=10)


def abrir_tela_cadastro(root):
    root.destroy()
    nova_janela = ctk.CTk()
    nova_janela.geometry("800x600")  # Garante que a tela de cadastro tenha o mesmo tamanho
    nova_janela.title("Cadastro")
    tela_cadastro(nova_janela)
    nova_janela.mainloop()
