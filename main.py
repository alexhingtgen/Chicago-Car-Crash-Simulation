"""
Alex Hingtgen and Zak Zahner
"""

import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
from utilities import *


class AllTkinterWidgets:
      def __init__(self, master):
        frame = Frame(master, width=800, height=800, bg= "red")
        frame.pack(expand = 0)
        frame.pack(side = TOP, anchor = N)
        self.lb1 = Label(frame, text= '2020 Chicago Roadway Collision Data: Car Crash Prevention Simulator')
        self.lb1.pack(fill = X, side = TOP)
        self.lb2 = Label(frame, text='Analyze Past Car Crash Impacts from Chicago')
        self.lb2.pack(fill = X, side = TOP)
        self.label1 = tkinter.Label()



        # ---------------------Menu Creation ------------------------
        self.mbar = Frame(frame, relief = 'raised', width=2, bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)

 

        # ----------------- RadioButtonBar Creation ----------------
        self.rbbar = Frame(frame, relief = 'sunken', width=2, bd = 2)
        self.rbbar.pack(expand = 1, fill = BOTH, side = BOTTOM, pady = 5)

        # Radio buttons specified as string variables with values to run a certain action
        self.v = StringVar()
        Label(self.rbbar, text='Roadway Surface Conditions:').pack(side=LEFT, padx=5)
        self.rDry  = Radiobutton(self.rbbar, text='Dry', variable = self.v, value='Dry', command=self.OnDry)
        self.rWet    = Radiobutton(self.rbbar, text='Wet', variable = self.v, value='Wet', command=self.OnWet)
        self.rSnowSlush = Radiobutton(self.rbbar, text = 'Snow or Slush', variable = self.v, value='Snow or Slush', command=self.OnSnowSlush)
        self.rIce = Radiobutton(self.rbbar, text = 'Ice', variable = self.v, value='Ice', command=self.OnIce)
        self.rAll = Radiobutton(self.rbbar, text = 'All', variable = self.v, value='All', command=self.OnAll)


        self.rDry.pack(side=LEFT)
        self.rWet.pack(side=LEFT)
        self.rSnowSlush.pack(side=LEFT)
        self.rIce.pack(side=LEFT)
        self.rAll.pack(side=LEFT)
        


        # ------------------- ButtonBar Creation --------------------
        self.bbar = Frame(frame, relief = 'sunken', width=2, bd = 2)
        self.bbar.pack(expand = 1, fill = BOTH, side = BOTTOM, pady = 5, before = self.rbbar)



        # -------------------- entry box frame ---------------------
        self.t = StringVar()
        self.ef = Frame(frame, bd=2, relief='groove')
        self.lb2 = Label(self.ef, text='File:')
        self.lb2.pack(side= LEFT)
        self.entry = Entry(self.ef, textvariable = self.t, bg='white')
        self.bt = Button(self.ef, text = 'Load Crash Data...', command = self.load)
        self.entry.pack(side = LEFT, padx = 5)
        self.bt.pack(side = LEFT, padx= 5)
        self.ef.pack(expand=0, fill=X, pady=5, before = self.bbar, side = TOP)

 

        #--------------------- listbox frame ------------------------
        self.lf = Frame(frame, bd=2, relief='groove')
        self.lb = Label(self.lf, text='Crash Data Analysis Options:')
        self.bt1 = Button(self.lf, text = 'Clear', command = self.clear)
        self.bt2 = Button(self.lf, text = 'Average Crash Cost by Speed Zone', command = self.getAverageCostHistogram)
        self.bt3 = Button(self.lf, text = 'Calculate 2020 Monthly Crashes', command = self.getMonthlyCrashesGraph)
        self.bt4 = Button(self.lf, text = 'Compute Crash Injury Potential', command = self.getInjuryPieCharts)
        self.bt5 = Button(self.lf, text = 'Calculate Crashes based on Road Conditions', command = self.getConditionsLineGraphs)
        self.listbox = Listbox(self.lf, height=8)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.lb.pack(side=LEFT, padx=5)
        self.bt1.pack(side = BOTTOM)
        self.bt2.pack(side = BOTTOM)
        self.bt3.pack(side = BOTTOM)
        self.bt4.pack(side = BOTTOM)
        self.bt5.pack(side = RIGHT)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(padx=5, fill = X)
        self.lf.pack(expand=0, fill=X, pady=5, before = self.ef, side = BOTTOM)
        
        self.image1 = None


      # -------------------- Function defs ------------------------        
      def clear(self):
          self.listbox.delete(0, END)
          self.label1.destroy()
          self.label1 = Label()
          self.lbl1.destroy()
          
      def getMonthlyCrashesGraph(self):
          self.listbox.delete(0, END)
          self.listbox.delete(0, END)
          self.graphImage = Image.open('CrashesPerMonth.png')
          test = ImageTk.PhotoImage(self.graphImage)
          self.lbl1 = tkinter.Label(image=test)
          self.lbl1.image = test
          self.lbl1.place(x=500, y=325)
          
      def getInjuryPieCharts(self):
          self.listbox.delete(0, END)
          self.graphImage = Image.open('InjuryPotential.png')
          test = ImageTk.PhotoImage(self.graphImage)
          self.lbl1 = tkinter.Label(image=test)
          self.lbl1.image = test
          self.lbl1.place(x=500, y=325)
             
      def getAverageCostHistogram(self):
          self.graphImage = Image.open('AverageCostHist.png')
          test = ImageTk.PhotoImage(self.graphImage)
          self.lbl1 = tkinter.Label(image=test)
          self.lbl1.image = test
          self.lbl1.place(x=500, y=325)
          
      def getConditionsLineGraphs(self):
          self.listbox.delete(0, END)
          r_b_v = self.v
          if r_b_v == 'all':
            self.graphImage = Image.open('AllConditionsPlot.png')
            test = ImageTk.PhotoImage(self.graphImage)
            self.lbl1 = tkinter.Label(image=test)
            self.lbl1.image = test
            self.lbl1.place(x=500, y=325)
          elif r_b_v == 'dry':
            self.graphImage = Image.open('DryPlot.png')
            test = ImageTk.PhotoImage(self.graphImage)
            self.lbl1 = tkinter.Label(image=test)
            self.lbl1.image = test
            self.lbl1.place(x=500, y=325)
          elif r_b_v == 'wet':
            self.graphImage = Image.open('WetPlot.png')
            test = ImageTk.PhotoImage(self.graphImage)
            self.lbl1 = tkinter.Label(image=test)
            self.lbl1.image = test
            self.lbl1.place(x=500, y=325) 
          elif r_b_v == 'Snow or Slush':
            self.graphImage = Image.open('SnoworSlushPlot.png')
            test = ImageTk.PhotoImage(self.graphImage)
            self.lbl1 = tkinter.Label(image=test)
            self.lbl1.image = test
            self.lbl1.place(x=500, y=325) 
          elif r_b_v == 'ice':
            self.graphImage = Image.open('IcePlot.png')
            test = ImageTk.PhotoImage(self.graphImage)
            self.lbl1 = tkinter.Label(image=test)
            self.lbl1.image = test
            self.lbl1.place(x=500, y=325) 
                       
      def OnDry(self):
          self.v = 'dry'
          
      def OnWet(self):
          self.v = 'wet'
          
      def OnSnowSlush(self):
          self.v = 'Snow or Slush'

      def OnIce(self):
          self.v = 'ice'
          
      def OnAll(self):
          self.v = 'all'

      def load(self):
          try:
             print(self.t.get())
             self.image1 = Image.open(self.t.get())
             test = ImageTk.PhotoImage(self.image1)
             self.label1.config(image='')
             self.label1.config(image=test)
             self.label1.image = test
             self.label1.place(x=425, y=0)
          except Exception as e:
              print(e)
              self.listbox.insert(END, 'Error loading file' + self.t.get())
          
          self.listbox.insert(END, 'Loaded File' + self.t.get())
          
      def loading(self,file):
          try:
              img = Image.open(file)
              test = ImageTk.PhotoImage(img)
              print(file)
              self.label1.config(image='')
              self.label1.config(image=test)
              self.label1.image = test
              self.label1.place(x=425, y = 0)
              print(file)
          except Exception as e:
              print(e)
              self.listbox.insert(END, 'Error loading file' + file)
              
          self.listbox.insert(END, 'Loaded file' + file)

 
if __name__ == '__main__':
    # Preparing Graphs 
    getMonthlyCrashesGraph()
    getInjuryPieCharts()
    getAverageCostHistogram()
    onDry()
    onAll()
    onWet()
    onSnoworSlush()
    onIce()
    # main--display the menu
    root = Tk()
    
    root.configure(background='Black')
    root.geometry('1500x1200')
    
    all = AllTkinterWidgets(root)
    root.title('Computational Thinking ~ Final Project')

root.mainloop()
