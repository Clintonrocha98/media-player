import os


def rename_file(current_name, new_name):
    """
    Renomeia um arquivo.

    Parâmetros:
        nome_atual (str): O nome atual do arquivo, incluindo o caminho, se necessário.
        novo_nome (str): O novo nome do arquivo, incluindo o caminho, se necessário.

    Retorna:
        bool: True se a operação foi bem-sucedida, False caso contrário.
    """
    try:
        os.rename("data/playlists" + current_name, "data/playlists" + new_name)
        print(f"File renamed from '{current_name}' to '{new_name}' successfully.")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{current_name}' was not found.")
