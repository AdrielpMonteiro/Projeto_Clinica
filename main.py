import tkinter as tk
import customtkinter as ctk
from ui.tela_login import tela_login
from ui.tela_cadastro import tela_cadastro


def main():
    root = ctk.CTk()
    root.title("Sistema de Agendamentos")
    root.geometry("800x600")
    ctk.set_appearance_mode("dark")  # Modos: "light", "dark", "system"
    ctk.set_default_color_theme("blue")

    tela_login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
