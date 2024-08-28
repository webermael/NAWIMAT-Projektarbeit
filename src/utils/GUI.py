import tkinter
from tkinter import ttk

class Startpage:
  def __init__(self, config):
    #configs
    self.startpage = tkinter.Tk()
    Config(self.startpage)

    #widgets
    self.label1 = tkinter.ttk.Label(self.startpage, text = "SimEvolator", font = ('Arial'))  
    self.label1.place(relx = 0.2, rely = 0.1, relwidth = 0.6) 

    self.button1 = tkinter.ttk.Button(self.startpage, text = "Start!", font = ('Arial'), command = self.start)
    self.button1.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheigt = 0.247) 
    
    self.startpage.mainloop()
    
    def start (self):
      self.startpage.destroy()# closes Startpage
      Settings()# opens Settings
    
class Settings:
  def __init__(self, config):
    #configs
    self.settings = tkinter.Tk()
    Config(self.settings)
    
    #widgets
    self.scales = {
      self.scaleRowLength = Scale(self.settings, 1, 5000)    
      self.scaleColumnLength = Scale(self.settings, 1, 5000)
      self.scalePopulation = Scale(self.settings, 10, 1000)
      self.scaleGeneration = Scale(self.settings, 1, 1000)
      }
    
    self.scrollbar = tkinter.ttk.Scrollbar(self.settings, orient='vertical', command=self.scales.yview)# .yview is a problem yet
    self.scrollbar.grid(row=0, column=1, sticky=tkinter.NS)
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
    # root = tkinter.Tk() and root.mainloop() have to be directly in the specific class
    self.geometry = "800x600"
    root.geometry(self.geometry)
    root.resizable(width = False, heigth = False)
    
    self.title = "Simulation"
    root.title(self.title)

class Scale:
  def __init__(self, root, scaleLow, scaleHigh):
    self.scale = tkinter.ttk.Scale(root, from_ = scaleLow, to = scaleHigh)
    self.scale.pack(expand = True) # not really a solution
        
