import os


def delete_playlist_file(playlist):
    if os.path.exists("data/playlists/" + playlist + ".txt"):
      os.remove("data/playlists/" + playlist + ".txt")
      print("Arquivo / Playlist apagada")
    else:
      print("Arquivo / Playlist não existe :(...)") 
