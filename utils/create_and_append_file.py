def create_and_append_file(file_name, text=""):
    """
    Cria um arquivo .txt (se não existir) ou adiciona texto a um existente.

    :param file_name: O nome do arquivo .txt a ser criado ou editado.
    :param text: O texto a ser adicionado ao arquivo.
    """
    with open("data/playlists/" + file_name + ".txt", "a") as file:
        file.write(text + "\n")