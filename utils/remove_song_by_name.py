def remove_song_by_name(file_path, song_name):
    """
    Remova uma linha de um arquivo de texto contendo caminhos de músicas, usando o nome da música.

    :param file_path: Caminho para o arquivo de texto.
    :param song_name: Nome da música a ser removida (sem distinção entre maiúsculas e minúsculas).
    """
    file_path = "data/playlists/" + file_path + ".txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            for line in lines:
                if song_name.lower() not in line.lower():
                    file.write(line)

        print(f'Song "{song_name}" removed successfully (if it existed).')
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
