def restore_string(formatted_text):
    """
    Restaura uma string formatada ao seu estado original (substitui '_' por espaços
    e coloca em maiúscula apenas a primeira letra da string).
    """
    restored_text = formatted_text.replace("_", " ")
    return restored_text.capitalize()
