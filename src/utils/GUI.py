import tkinter
from tkinter import ttk

class Startpage:
  def __init__(self, config):
    self.startpage = tkinter.Tk() 
    
    self.title = "Simulation" 
    self.startpage.title(self.title) 
    
    self.geometry = ("800x600") 
    self.startpage.geometry = (self.geometry)
    self.startpage.resizable(width = False, heigth = False)
    

    self.label1 = tkinter.Label(self.startpage, text = "SimEvolator", font = ('Arial'))  
    self.label1.place(relx = 0.2, rely = 0.1, relwidth = 0.6) 

    self.button1 = tkinter.ttk.Button(self.startpage, text = "Start!", font = ('Arial'), command = self.start)
    self.button1.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheigt = 0.247) 
    
    self.startpage.mainloop()
    def start (self):
      self.startpage.destroy()
      Settings()

class Scale:
  def __init__(self, root, scaleLow, scaleHigh):
    self.scale = tkinter.ttk.Scale(root, from_ = scaleLow, to = scaleHigh)
    
class Settings:
  def __init__(self, config):
    self.settings = tkinter.Tk()

    self.title = "Simulation"
    self.settings.title(self.title)

    self.geometry = ("800x600") 
    self.settings.geometry = (self.geometry)

    self.scaleRowLength = Scale(self.settings, 1, 5000)    
    self.scaleColumnLength = Scale(self.settings, 1, 5000)
    self.scalePopulation = Scale(self.settings, 10, 1000)
    self.scaleGeneration = Scale(self.settings, 1, 1000)
    
    self.scales = {self.scaleRowLength, self.scaleColumnLength, self.scalePopulation, self.scaleGeneration}# Prly last 4 lines are able to be directly here (not on my vs code)
    self.scrollbar = tkinter.ttk.Scrollbar(self.settings, orient='vertical', command=self.scales.yview)# .yview is a problem yet
    self.scrollbar.grid(row=0, column=1, sticky=tkinter.NS)
    self.scales['yscrollcommand'] = self.scrollbar.set

    self.settings.mainloop()
    

    

def getScaleValue(self):    #command for getting values from scales
  value1 = self.scaleRowLength.get() # Var names are all wrong
  value2 = self.scaleColumnLenght.get()
  value3 = self.scalePopulation.get()
  value4 = self.scaleGeneration.get()
  self.settings.destroy()    #closes the window
  #start the sim
  
  
    

    
        
