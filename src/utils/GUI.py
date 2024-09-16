import tkinter as tk
from tk import ttk

class Startpage:
  def __init__(self, config):
    # setup
    self.root = tk.Tk()
    Config(self.startpage)

    # widgets
    self.lTitle = tk.ttk.Label(self.root , text = "SimEvolator", font = ('Arial'))  
    self.lTitle.place(relx = 0.2, rely = 0.1, relwidth = 0.6) 

    self.bStart = tk.ttk.Button(self.root , text = "Start!", font = ('Arial'), command = self.start)
    self.bStart.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheigt = 0.247) 
    
    self.root.mainloop()
    
    def start(self):
      self.root.destroy()# closes Startpage
      Settings()# opens Settings
    
class Settings:
  def __init__(self, config):
    #configs
    self.settings = tk.Tk()
    Config(self.settings)
    
    #widgets
    self.scales = {
      self.scaleRowLength = Scale(self.settings, 1, 5000)    
      self.scaleColumnLength = Scale(self.settings, 1, 5000)
      self.scalePopulation = Scale(self.settings, 10, 1000)
      self.scaleGeneration = Scale(self.settings, 1, 1000)
      }
    
    self.scrollbar = tk.ttk.Scrollbar(self.settings, orient='vertical', command=self.scales.yview)# .yview is a problem yet
    self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
    self.scales['yscrollcommand'] = self.scrollbar.set

    self.settings.mainloop()
    
  def getScaleValue(self):# command for getting values from scales
    value1 = self.scaleRowLength.get()# Var names are all wrong
    value2 = self.scaleColumnLenght.get()
    value3 = self.scalePopulation.get()
    value4 = self.scaleGeneration.get()
    self.settings.destroy()# closes the window
    #start the sim

class Config:# maybe the class name is problematic
  def __init__(self,root):
    # root = tk.Tk() and root.mainloop() have to be directly in the specific class
    self.geometry = "800x600"
    root.geometry(self.geometry)
    root.resizable(width = False, heigth = False)
    
    self.title = "Simulation"
    root.title(self.title)

class Scale:
  def __init__(self, root, scaleLow, scaleHigh):
    self.scale = tk.ttk.Scale(root, from_ = scaleLow, to = scaleHigh)
    self.scale.pack(expand = True) # not really a solution
        
