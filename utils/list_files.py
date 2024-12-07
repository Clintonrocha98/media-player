import os

def list_files(directory="data/playlists"):
    """
    Retorna uma lista com os caminhos completos de todos os arquivos em uma determinada pasta.

    :param pasta: Caminho da pasta a ser lida.
    :return: Lista com os caminhos completos dos arquivos.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths