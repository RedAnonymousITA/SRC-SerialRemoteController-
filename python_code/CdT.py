# Sviluppatore Pop Mario Denis (RA-ITA2,RedAnonumousITA2)
# Licenza MIT .
#Scritto in python3.
# RA-ITA2 autorizza la copia e modifica di questo software a solo scopo educativo
# E severamente e vietato usare questo software in maniera comerciale e
# RA-ITA2 richiede in caso di modifica o fork del software di nominare L'autore .
# Se e stato modificato indicare Autore RA-ITA2 e il nome di chi ha modificato il software.
#RA-ITA2 non si assume nessuna responsabilita se lo scaricate da terzi ed ha un virus
#in caso di attaco craker informare le autorita e denuciare l'autore che ha publicato il software infetto da
# un virus

from ast import Import
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as mssbox
import math 
class Main:
    def __init__(self,root):
        self.Frame_1()
        
        
        pass
    def calcolo(self):
        self.button_back()
        S_list =[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240]

        Watt =self.P.get() 
        w =  eval(Watt)
        Kwatt = w *1000
        FP_txt = self.FP.get()
        FP =float(FP_txt) 
        V_txt = self.v.get()
        Volt = int(V_txt)
        km_txt = self.l.get()
        L = eval(km_txt)
        
        ru = self.Ru.get()
        Ru=eval(ru)
        
        xu = self.Xu.get()
        Xu = eval(xu)
                    
        
        I0 =1.73*Volt*FP #I == Ib 

        I = Kwatt/I0
            

        Acos = math.degrees(math.acos(FP))
        Sin0 = math.sin(math.radians(Acos))
        r= Sin0 *100  
        r0 =round(r)
        r1 = r0 /100
        Sin= r1
        DVc= Ru*FP+Xu*Sin
        DVb = 1.73*L*I*(Ru*FP+Xu*Sin)
        DV = int(DVb)
        perc = DV/400*100

        if int(perc) <= 4:
            if DV <= 16:
                mss ="""
Caduta di tensione e :%s %s
Tensione :%s V
Caduta di tensione verificato 


""" %(int(perc),'%',DV)
                mssbox.showinfo(title='CdT',message=mss)
        else:
                mssbox.showwarning(title='CdT',message="Caduta della tensine non e a norma CEI ")
     
    def Frame2(self):
        self.frame = ttk.Frame(root)
        self.frame.place(x=0,y=0,height=400,width=300)
        self.label()
        self.entry()
        self.button_back()
        self.button()
        self.comboboxGomma()
    def Frame_1(self):
        def nxt():
            
            c0 = c.get()
            if c0 in "PVC":
                self.Frame_0() 
            
            elif c0 in "Gomma":
                self.Frame2()

            else:
                pass
        frame1 = ttk.Frame(root)
        frame1.place(x=0,y=0,height=300,width=300)
        txt = ttk.Label(frame1,text='Che tipo di cavo e ?') 
        txt.pack()
        c =  ttk.Combobox(frame1,values=["PVC","Gomma"])
        c.pack()
        b = ttk.Button(frame1,text='OK',command=nxt)
        b.pack()
        

        pass
    
    def Frame_0 (self):
        self.frame = ttk.Frame(root)
        self.frame.place(x=0,y=0,height=400,width=300)
        self.label()
        self.entry()
        self.button_back()
        self.button()
        self.comboboxPVC()
    def label (self):
        p_txt = ttk.Label(self.frame,text='Watt (KW):')
        p_txt.place(x=100,y=1)
        
        fp_txt = ttk.Label(self.frame,text='Fattore di potenza:')
        fp_txt.place(x=85,y=40)
        
        v_txt = ttk.Label(self.frame,text='Volt:')
        v_txt.place(x=115,y=80)
        
        l_txt = ttk.Label(self.frame,text='Lunghezza cavo:')
        l_txt.place(x=85,y=120)
        
        Ru_txt = ttk.Label(self.frame,text='Ru: ')
        Ru_txt.place(x=100,y=160)
        
               
        Xu_txt = ttk.Label(self.frame,text='Xu: ')
        Xu_txt.place(x=100,y=200)
        
               
        #S_txt = ttk.Label(self.frame,text='Sezione cavo: ')
        #S_txt.place(x=100,y=160)
        pass
 
        pass
    def button_back(self):
        def f1():
            self.frame.destroy()
            self.Frame_1()
        bt0 = ttk.Button(self.frame,text='Home',command=f1)
        bt0.place(x=200,y=0)
    def button(self):
        global bt_x
        bt_x =100
        def f0():
            
            
            self.calcolo()
            pass
        bt = ttk.Button(self.frame,text='Calcola',command=f0)
        bt.place(x=bt_x,y=280)
    def comboboxPVC(self):
        Ru_list =[15.91,9.55,5.92,3.95,2.29,1.45,0.93,0.66,0.089,0.085,0.082,0.081,0.099]
        Xu_list =[0.145,0.132,0.127,0.119,0.110,0.102,0.097,0.092,0.089,0.085,0.082,0.0800]
        S_list =[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240]
        #self.S = ttk.Combobox(self.frame,values=S_list)
        #self.S.place(x=70,y=180)
        
        self.Ru= ttk.Combobox(self.frame,values=Ru_list)
        self.Ru.place(x=70,y=180)
        self.Xu = ttk.Combobox(self.frame,values=Xu_list)
        self.Xu.place(x=70,y=220)
    def comboboxGomma(self):
        Ru_list =[16.96,10.17,6.31,4.21,2.44,1.54,0.99,0.71,0.49,0.35,0.26,0.21,0.17,0.14,0.11]
        Xu_list =[0.144,0.132,0.122,0.144,0.105,0.098,0.93,0.89,0.85,0.084,0.083,0.080,0.078]
        S_list =[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240]
        
        #self.S = ttk.Combobox(self.frame,values=Ru_list)
        #self.S.place(x=70,y=180)
        self.Ru= ttk.Combobox(self.frame,values=Ru_list)
        self.Ru.place(x=70,y=180)
        self.Xu = ttk.Combobox(self.frame,values=Xu_list)
        self.Xu.place(x=70,y=220)
    def entry(self):
        self.P = ttk.Entry(self.frame)
        self.P.place(x=70,y=20)
        
        
        self.FP = ttk.Entry(self.frame)
        self.FP.place(x=70,y=60)
        
        
        self.v = ttk.Entry(self.frame)
        self.v.place(x=70,y=100)
        
        
        self.l = ttk.Entry(self.frame)
        self.l.place(x=70,y=140)
        

        
root = tk.Tk()
root.title('CdT By Pop Mario Denis')
root.geometry("300x400")
root.resizable(False,False)
if __name__ in "__main__":
    main = Main(root)
    root.mainloop()