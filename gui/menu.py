import tkinter as tk


class MediaPlayerMenu:
    def __init__(self, root):
        self.option_selected = tk.StringVar(value="Opções")
        self.menu = tk.OptionMenu(root, self.option_selected, "Opções")
        self.menu.pack(pady=10)
        self.options = {}
        
    def add_option(self, option_name, function):
        """
        Adiciona uma nova opção ao menu com uma função associada.\n
        :param option_name: Nome da opção que aparecerá no menu.\n
        :param function: Função a ser executada quando a opção for selecionada.
        """
        self.options[option_name] = function
        self.menu["menu"].add_command(label=option_name, command=lambda: self.execute_option(option_name))
    
    def execute_option(self, option_name):
        """
        Executa a função associada a uma opção específica.\n
        :param option_name: Nome da opção selecionada.
        """
        if option_name in self.options:
            self.options[option_name]()  
        else:
            print("Opção inválida!")