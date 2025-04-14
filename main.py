import tkinter as tk
import customtkinter as ctk
from ui.tela_login import tela_login
from ui.tela_cadastro import tela_cadastro
import pytest

def main():
    root = ctk.CTk()
    root.title("Sistema de Agendamentos")
    ##root.geometry("1300x760")
    root.attributes("-fullscreen",True) ## colocando modo fullScreee tela cheia

    ctk.set_appearance_mode("dark") ## conf para deixar tema de aparencia dark (escuro)
    ctk.set_default_color_theme("blue")##conf da personalização dos botões .


    tela_login(root)
    root.mainloop()


if __name__ == "__main__":
    main()