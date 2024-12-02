from tkinter import ttk

class ProgressBar:
  def __init__(self, root):
    self.__root = root
    self.__progress = 0
    self.__duration = 0
    self.__is_paused = False
    self.__progress_bar = ttk.Progressbar(self.__root, orient="horizontal", mode="determinate", length=300, maximum=100)

  def play(self):
        """começa a progressão da barra"""
        if self.__progress == 0: 
            self.__progress_bar["value"] = 0
        self.__is_paused = False
        
        self.update_progress()

  def pause(self):
      """pausa a progressao da barra"""
      self.__is_paused = True 

  def update_progress(self):
      """atualiza a progressão da barra"""
      if not self.__is_paused and self.__progress < self.__duration:
          self.__progress += 1
          self.__progress_bar["value"] = (self.__progress / self.__duration) * 100
          self.__root.after(1000, self.update_progress)
  
  def set_duration(self, duration):
      self.__duration=duration
  
  def get_progress_bar(self):
      """retorna a barra de progressao"""
      return self.__progress_bar