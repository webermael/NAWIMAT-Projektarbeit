import tkinter

class GUI:
  def __init__(self, config):
    self.root = tkinter.TK()
    
    self.title = "Simulation" #Title should prly be changed
    self.root.title(self.title)
    
    self.geometry = (f"{config.tile_width}x{config.tile_length}") 
    self.root.geometry = (self.geometry)

    self.label1 = tkinter.Label(self.root, text = "SimEvolator", font = ('Arial')) # Isn't really nessecary
    self.label1.place(relx = 0.2, rely = 0.1, relwidth = 0.6)

    self.button1 = tkinter.Button(self.root, text = "Start!", font = ('Arial'), command = start_sim)
    self.button1.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheigt = 0.247) # relheight = golden section from relwidth
    
    self.root.mainloop()
    def start_sim():
      #start the simulation
      self.root.destroy() # closes the root window 
    
    
