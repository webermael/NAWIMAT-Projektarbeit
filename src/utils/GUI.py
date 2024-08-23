import tkinter

class GUI:
  def __init__(self, config):
    self.root = tkinter.TK()
    self.title = "Simulation"
    root.title(self.title)  #Title should prly be changed
    self.geometry = (f"{config.tile_width}x{config.tile_length}") 
    root.geometry = (self.geometry)

    root.mainloop()
    
