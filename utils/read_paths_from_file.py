def read_paths_from_file(txt_file):
    """
    Lê um arquivo .txt contendo paths de arquivos e retorna os paths encontrados.

    :param arquivo_txt: Caminho do arquivo .txt que contém os paths.
    :return: Lista de paths encontrados no arquivo.
    """

    with open("data/playlists/" + txt_file + ".txt", "r") as file:
        paths = [line.strip() for line in file if line.strip()]
        return paths
