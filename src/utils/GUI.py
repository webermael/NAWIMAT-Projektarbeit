import tkinter

class Startpage:
  def __init__(self, config):
    self.startpage = tkinter.TK() 
    
    self.title = "Simulation" 
    self.startpage.title(self.title) 
    
    self.geometry = ("800x600") 
    self.startpage.geometry = (self.geometry)
    self.startpage.resizable(width = False, heigth = False)
    

    self.label1 = tkinter.Label(self.startpage, text = "SimEvolator", font = ('Arial'))  
    self.label1.place(relx = 0.2, rely = 0.1, relwidth = 0.6) 

    self.button1 = tkinter.Button(self.startpage, text = "Start!", font = ('Arial'), command = self.start)
    self.button1.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheigt = 0.247) 
    
    self.startpage.mainloop()
    def start (self):
      self.startpage.destroy()
      Settings()


class Settings:
  def __init__(self, config):
    self.settings = tkinter.TK()

    self.title = "Simulation"
    self.settings.title(self.title)

    self.geometry = (f"{config.tile_width}x{config.tile_length}") 
    self.settings.geometry = (self.geometry)

    self.scaleWidth = 50
    self.scaleLength = 300
    self.scaleLow = 1
    self.scaleHigh = 5000
    
    self.scaleRowLength = tkinter.Scale(self.settings, from_= self.scaleLow, to = self.scaleHigh, width = self.scaleWidth, length = self.scaleLength) 
    #self.scaleRowLength.place(x = 60 , y = 75)
    
    self.scaleColumnLength = tkinter.Scale(self.settings, from_= self.scaleLow, to = self.scaleHigh, width = self.scaleWidth, length = self.scaleLength) 
    #self.scaleRowLength.place(x = 210 , y = 75)

    self.scalePopulation = tkinter.Scale(self.settings, from_= self.scaleLow, to = self.scaleHigh, width = self.scaleWidth, length = self.scaleLength) 
    #self.scaleRowLength.place(x = 360 , y = 75)

    self.scaleGeneration = tkinter.Scale(self.settings, from_= self.scaleLow, to = self.scaleHigh, width = self.scaleWidth, length = self.scaleLength) 
    #self.scaleRowLength.place(x = 510 , y = 75)

    self.buttonStart = tkinter.Button(self.settings, text = "Start!", command = )
    #self.buttonStart.place()

def getScaleValue(self):
  value1 = self.scaleRowlength.get() # Var names are all wrong
  value2 = self.scaleColumnLenght.get()
  value3 = self.scalePopulation.get()
  value4 = self.scaleGeneration.get()
  self.settings.destroy()    #closes the window
  #start the sim
  
  
    

    
        
