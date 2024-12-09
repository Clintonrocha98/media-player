def generate_playlist_filename(text):
    """
    Substitui espaços por '_' e converte todas as letras para minúsculas.
    """
    return text.replace(" ", "_").lower()