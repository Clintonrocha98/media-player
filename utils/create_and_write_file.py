def create_and_write_file(file_name, text):
    """
    Cria um arquivo .txt e grava nele o texto especificado.

    :param file_name: O nome do arquivo .txt a ser criado.
    :param text: O texto a ser escrito no arquivo.
    """
    with open("data/playlists/" + file_name, "w") as file:
        file.write(text)
