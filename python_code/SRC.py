# Driver by RDAITA2 (Pop Mario Denis)
import os
from pydoc import text
import tkinter as tk
from tkinter import BOTH, END, LEFT, Y, ttk
from tkinter import filedialog as file
from tkinter import messagebox as msBox

try:
    import webbrowser
except:
    os.system('conf.bat')
class local_DB():
    def __init__(self,com3,com4,com5,com6,com7,com8,com9) : # comN = command  .N is number :com3.request String command :code.exe 
        self.c3 = com3
        self.c4 = com4
        self.c5 = com5
        
        self.c6 = com6 
        self.c7 = com7
        self.c8 = com8
        self.c9 = com9
    def code_DB(self):  # Driver code 
        text0="""import serial
import socket as sk
import os,sys
import json,re
import tkinter as tk
from tkinter import messagebox as msbox
import webbrowser as web
import psutil as ps
            
with open("data.json","r") as f:
    data_json = json.load(f)
read_json = (data_json["port"])
port_usb = re.sub("[']","",read_json[0])
hostname = sk.gethostname()
ip = sk.gethostbyname(hostname)
b= True

vol = 50
print('wait Debug  ')
print(port_usb)
# serial configuration and serial function 
ser = serial.Serial(port_usb,9600)
ms= "start serial port:  "+port_usb
msbox.askyesno(title="Info" ,message=ms)

if msbox.YES == "yes":
        
        while b:

            read = ser.readline()
            c= str(read)
            
            if "c" in c:
                 
                     CPU_COUNT = str(ps.cpu_count(logical=False))+' Core'
                 
                     ser.write(bytes(CPU_COUNT,'utf-8'))
            if "f" in c :
                CPU_FREQ= str(ps.cpu_freq()[0]/10000)+' FREQ'
                 
                ser.write(bytes(CPU_FREQ,'utf-8'))
            if "p" in c :
                for n in range(5):
                    CPU_PERC = str(ps.cpu_percent(1))
                 
                    ser.write(bytes(CPU_PERC,'utf-8'))
            if"e" in c:
                print('EXIT')
                sys.exit()
            if"0" in c:
                print('ip send')
                ser.write(bytes(ip,'utf-8'))
        

            if "1" in c:
                print('host send')
                ser.write(bytes(hostname , 'utf-8'))
            if "2" in c:
                print('reboot windows')
                os.system('shutdown /r ')
            if "3" in c:
                os.system('"%s"')
                
                
            if "4" in c:
            
                os.system('"%s"')
                
            if "5" in c :
                os.system('"%s"')
                
            if "6" in c :
                os.system('"%s"')
                
            if "+" in c:
              
                
                vol =vol+2
                vol_txt=str(vol)+"Vol"
                print(vol_txt)
                
                ser.write(bytes(vol_txt,'utf-8'))
                V1="SetVol "+ str(vol)
                os.system(V1)

                if vol >= 100:
                    ser.write(bytes("STOP",'utf-8'))
                    vol=vol -5
                    os.system("SetVol beep")
            if "-" in c:
              
                vol =vol-2
                vol_txt=str(vol)+"Vol"
                print(vol_txt)
                ser.write(bytes(vol_txt,'utf-8'))
                V2 = "SetVol "+str(vol)
                os.system(V2)
               
                if vol <=0:
                    ser.write(bytes("STOP",'utf-8'))
                    vol=vol +2
                    os.system("SetVol beep")
            if "7" in c :
                os.system('"%s"')
                
            elif "8" in c :
                os.system('"%s"')
                
            elif "9" in c :
                os.system('"%s"')"""%(self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9)
            
        w=open("mkCode/SRC_code.py",'w')
        w.write(text0)
        w.close()
                
class read_file():
    def __init__(self) -> None:
        pass
    def file3(self):
        
        filetypes0 = (
        ('.exe', '*.exe'),
        ('.Bat', '*.bat'),
        ('.TXT', '*.txt'),
        ('All files', '*.*')
        )
        f3= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        f=open(".Trash/f3.txt",'w')
        f.write(f3)
        f.close()
        print('write ok')
        
       

        
       
    
    def file4(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f4= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f4.txt",'w')
        f.write(f4)
        f.close()
        print('write ok')
        
   
        
    def file5(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f5= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f5.txt",'w')
        f.write(f5)
        f.close()
        print('write ok')
        
    def file6(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f6= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f6.txt",'w')
        f.write(f6)
        f.close()
        print('write ok')
        
        
    def file7(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f7= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f7.txt",'w')
        f.write(f7)
        f.close()
        print('write ok')
        
            
        
    def file8(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f8= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f8.txt",'w')
        f.write(f8)
        f.close()
        print('write ok')
        
        
    def file9(self):
                
        filetypes0 = (
        ('.exe', '*.exe'),
        ('All files', '*.*')
        )
        f9= file.askopenfilename(title='Open file',initialdir='/',filetypes=filetypes0)
        
        f=open(".Trash/f9.txt",'w')
        f.write(f9)
        f.close()
        print('write ok')
        
    
# ---- - ----- --- - --- -- -- -------- ----- ------ --- - - - -- -- - - - - --------------------------------------------------
class Win ():
    print('start SRC :')
    def __init__(self,root) -> None:
        self.frame_start()
        pass
    def frame_start(self):
        self.frame01= tk.Frame(root)
        self.frame01.place(x=0,y=0,height=300,width =300)
        self.title_01 = ttk.Label(self.frame01,text='SRC',font=("Italy",25))
        self.title_01.place(x=120,y=10)
        self.button_new = ttk.Button(self.frame01,text='New SRC command',command=self.sel_BT)
        self.button_new.place(x=100,y=100)
        self.button_info = ttk.Button(self.frame01,text='INFO',command=self.frame_info)
        self.button_info.place(x=110,y=125)
      #  self.button_new = ttk.Button(self.frame01,text='New SRI command')
      #  self.button_new.place(x=100,y=100)
    def EXE(self):
        json_data ="""{
    "port":[
        "COM7"
    ]
} """   
        B=msBox.showinfo(title='Info EXE',message='Start pyinstaller ')
        folder = 'mkCode/SRC_code.py'
        os.system('pyinstaller '+folder+' --onefile  --noconsole')
       
        print('Wait maker data.json')
        json=open('dist/data.json','w')
        json.write(json_data)
        json.close()
        print('Wait copy SetVol.exe')
        os.system('copy /Y /B SetVol/SetVol.exe dist')
        print('END')
        
    def frame_info(self):
        def Rda():
            l=open('License_SRC.txt','r')
            l.read()
            l.close()
        def Rob():
            
            def Back():
                self.frameL.destroy()
                self.frame_start()
                
            
            l=open('SetVol/License.txt','r')
            L=str(l.read())
            l.close()
            os.system('License.txt')
            
           
          
        def Back():
            self.frame02.destroy()
            self.frame_start()
        self.frame01.destroy()
        self.frame02= tk.Frame(root)
        self.frame02.place(x=0,y=0,height=300,width =300)
        self.title_01 = ttk.Label(self.frame02,text="""SRC(SerialRemoteController)""",font=("Italy",16))
        self.title_01.place(x=0,y=10)
        self.text01 = ttk.Label(self.frame02,text="""Author: RDAITA2.
Version Software:0.1 - Beta.
Building = 0.1.
Framework = 0.1 -Beta
SetVol by Rob Latour                                """,font=("Italy",16))
        self.text01.place(x=0,y=45)
        self.button_back = ttk.Button(self.frame02,text='Back',command=Back)
        self.button_back.place(x=0,y=250)
        
        self.button_rda = ttk.Button(self.frame02,text='License SRC',command=Back)
        self.button_rda.place(x=95,y=250)
        
        self.button_Rob = ttk.Button(self.frame02,text='License SetVol',command=Rob)
        self.button_Rob.place(x=195,y=250)
    def  sel_BT(self):
        def next():
            try:
                n = int(self.entry.get())
            
                if n > 7:
                    print('Error Max Button is 7')
                elif n < 2:
                     print('Error Min Button is 2')
                else:
                    if n == 2:
                        self.frame2()
                        print('next page')
                    elif n == 3:
                        self.frame3()
                       
                    elif n == 4:
                         self.frame4()
                       
                    elif n == 5:
                         self.frame5()
                    elif n ==6 :
                         self.frame6()
                    elif n == 7:
                         self.frame7()
            except:
                 print('Error Not Found Number  ') 
            
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
        
        self.txt_bt3=  tk.Label(self.frame03,text='choose Button Numer 2-7:')
        self.txt_bt3.place(x=0,y=10)
        
        self.entry= ttk.Entry(self.frame03)
        self.entry.place(x=156,y=10)
        
        self.bt_ok = ttk.Button(
            self.frame03,
            text='OK',
            command=next
            )
        self.bt_ok.place(x=100,y=35)
    def frame2(self):
        f=read_file()
        def back():
            self.frame03.destroy()
            self.frame_start()
            
        def save():
            r0 = open(".Trash/f3.txt",'r')
            rA=str(r0.read())
            r0.close()
           
            
            r1 = open(".Trash/f4.txt",'r')
            rB=str(r1.read())
            r1.close()
            
            db=local_DB(rA,rB,'false','false','false','false','false')
            db.code_DB()
            self.EXE()
            
    
    
            
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)

        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        
        
        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file3)
        self.button3.place(x=59,y=10)
        
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        
               
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file4)
        self.button4.place(x=59,y=35)
        
               
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
        
    def frame3(self):
        f=read_file()
        def back():
            self.frame03.destroy()
            self.frame_start()
        def save():
            
            r0 = open(".Trash/f3.txt",'r')
            rA=r0.read()
            r0.close()
            print(rA)
            
            r1 = open(".Trash/f4.txt",'r')
            rB=r1.read()
            r1.close()
            print(rB)
            
            r0 = open(".Trash/f5.txt",'r')
            rC=r0.read()
            r0.close()
            print(rC)
            
            db=local_DB(rA,rB,rC,'false','false','false','false')
            db.code_DB()    
            self.EXE()
            
       
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
            
        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        self.txt_bt5=  tk.Label(self.frame03,text='Buttom 5:')
        self.txt_bt5.place(x=0,y=65)
        
        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file3)
        self.button3.place(x=59,y=10)
        
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file4)
        self.button4.place(x=59,y=35)
        
        self.button5 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file5)
        self.button5.place(x=59,y=65)
                      
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
    def frame4(self):
        
        f=read_file()
        def back():
            self.frame03.destroy()
            self.frame_start()
        def save():
            
            r0 = open(".Trash/f3.txt",'r')
            rA=r0.read()
            r0.close()
            print(rA)
            
            r1 = open(".Trash/f4.txt",'r')
            rB=r1.read()
            r1.close()
            print(rB)
            
            r0 = open(".Trash/f5.txt",'r')
            rC=r0.read()
            r0.close()
            print(rC)
            
            r1 = open(".Trash/f6.txt",'r')
            rD=r1.read()
            r1.close()
            print(rD)
            db=local_DB(rA,rB,rC,rD,'false','false','false')
            db.code_DB() 
            self.EXE()
            
        self.frame01.destroy()
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
        
        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        self.txt_bt5=  tk.Label(self.frame03,text='Buttom 5:')
        self.txt_bt5.place(x=0,y=65)
        self.txt_bt6=  tk.Label(self.frame03,text='Buttom 6:')
        self.txt_bt6.place(x=0,y=95)
        
        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file3)
        self.button3.place(x=59,y=10)
        
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file4)
        self.button4.place(x=59,y=35)
        
        self.button5 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file5)
        self.button5.place(x=59,y=65)
        
        self.button6 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file6)
        self.button6.place(x=59,y=95)
                             
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
    def frame5(self):
         
        f=read_file()       
        def back():
            self.frame03.destroy()
            self.frame_start()
        def save():
            
            r0 = open(".Trash/f3.txt",'r')
            rA=r0.read()
            r0.close()
            print(rA)
            
            r1 = open(".Trash/f4.txt",'r')
            rB=r1.read()
            r1.close
            print(rB)
            
            r0 = open(".Trash/f5.txt",'r')
            rC=r0.read()
            r0.close()
            print(rC)
            
            r1 = open(".Trash/f6.txt",'r')
            rD=r1.read()
            r1.close()
            print(rD)
            
            r0 = open(".Trash/f7.txt",'r')
            rE=r0.read()
            r0.close()
            print(rE)
            db=local_DB(rA,rB,rC,rD,rE,'false','false')
            db.code_DB() 
            self.EXE()
            
           
        self.frame01.destroy()
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
        
        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        self.txt_bt5=  tk.Label(self.frame03,text='Buttom 5:')
        self.txt_bt5.place(x=0,y=65)
        self.txt_bt6=  tk.Label(self.frame03,text='Buttom 6:')
        self.txt_bt6.place(x=0,y=95)
        self.txt_bt7=  tk.Label(self.frame03,text='Buttom 7:')
        self.txt_bt7.place(x=0,y=135)
        
        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file3)
        self.button3.place(x=59,y=10)
        
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file4)
        self.button4.place(x=59,y=35)
        
        self.button5 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file5)
        self.button5.place(x=59,y=65)
        
        self.button6 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file6)
        self.button6.place(x=59,y=95)
        
        self.button7 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file7)
        self.button7.place(x=59,y=135)
               
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
        
        
    def frame6(self):
        
        f=read_file()               
        def back():
            self.frame03.destroy()
            self.frame_start()
        def save():
            
            r0 = open(".Trash/f3.txt",'r')
            rA=r0.read()
            r0.close()
            print(rA)
            
            r1 = open(".Trash/f4.txt",'r')
            rB=r1.read()
            r1.close()
            print(rB)
            
            r0 = open(".Trash/f5.txt",'r')
            rC=r0.read()
            r0.close()
            print(rC)
            
            r1 = open(".Trash/f6.txt",'r')
            rD=r1.read()
            r1.close()
            print(rD)
            
            r0 = open(".Trash/f7.txt",'r')
            rE=r0.read()
            r0.close()
            print(rE)
            
            r1 = open(".Trash/f8.txt",'r')
            rF=r1.read()
            r1.close()
            print(rF)
            
            db=local_DB(rA,rB,rC,rD,rE,rF,'false')
            db.code_DB()   
            self.EXE()

        self.frame01.destroy()
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
             
        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        self.txt_bt5=  tk.Label(self.frame03,text='Buttom 5:')
        self.txt_bt5.place(x=0,y=65)
        self.txt_bt6=  tk.Label(self.frame03,text='Buttom 6:')
        self.txt_bt6.place(x=0,y=95)
        self.txt_bt7=  tk.Label(self.frame03,text='Buttom 7:')
        self.txt_bt7.place(x=0,y=135)
        self.txt_bt8=  tk.Label(self.frame03,text='Buttom 8:')
        self.txt_bt8.place(x=0,y=165)
        
        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file3)
        self.button3.place(x=59,y=10)
        
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file4)
        self.button4.place(x=59,y=35)
        
        self.button5 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file5)
        self.button5.place(x=59,y=65)
        
        self.button6 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file6)
        self.button6.place(x=59,y=95)
        
        self.button7 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file7)
        self.button7.place(x=59,y=135)
        
        self.button8 = ttk.Button(self.frame03,text=' choose File .exe',command=f.file8)
        self.button8.place(x=59,y=165)
                
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
        
    def frame7(self):
        
        f=read_file()
        def back():
            self.frame03.destroy()
            self.frame_start()
        def save():
           
            r0 = open(".Trash/f3.txt",'r')
            rA=r0.read()
            r0.close()
            print(rA)
            
            r1 = open(".Trash/f4.txt",'r')
            rB=r1.read()
            r1.close()
            print(rB)
            
            r0 = open(".Trash/f5.txt",'r')
            rC=r0.read()
            r0.close()
            print(rC)
            
            r1 = open(".Trash/f6.txt",'r')
            rD=r1.read()
            r1.close()
            print(rD)
            
            r0 = open(".Trash/f7.txt",'r')
            rE=r0.read()
            r0.close()
            print(rE)
            
            r1 = open(".Trash/f8.txt",'r')
            rF=r1.read()
            r1.close()
            print(rF)
            
            r0 = open(".Trash/f9.txt",'r')
            rG=r0.read()
            r0.close()
            print(rG)
           
            db=local_DB(rA,rB,rC,rD,rE,rF,rG)
            db.code_DB()  
            self.EXE()
           

        self.frame01.destroy()
        self.frame03 = tk.Frame(root)
        self.frame03.place(x=0,y=0,height=300,width =300)
        File = read_file()
     
        self.txt_bt3=  tk.Label(self.frame03,text='Buttom 3:')
        self.txt_bt3.place(x=0,y=10)
        self.txt_bt4=  tk.Label(self.frame03,text='Buttom 4:')
        self.txt_bt4.place(x=0,y=35)
        self.txt_bt5=  tk.Label(self.frame03,text='Buttom 5:')
        self.txt_bt5.place(x=0,y=65)
        self.txt_bt6=  tk.Label(self.frame03,text='Buttom 6:')
        self.txt_bt6.place(x=0,y=95)
        self.txt_bt7=  tk.Label(self.frame03,text='Buttom 7:')
        self.txt_bt7.place(x=0,y=135)
        self.txt_bt8=  tk.Label(self.frame03,text='Buttom 8:')
        self.txt_bt8.place(x=0,y=165)
        self.txt_bt9=  tk.Label(self.frame03,text='Buttom 9:')
        self.txt_bt9.place(x=0,y=195)

        self.button3 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file3)
        self.button3.place(x=59,y=10)
        
        self.button4 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file4)
        self.button4.place(x=59,y=35)
        
        self.button5 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file5)
        self.button5.place(x=59,y=65)
        
        self.button6 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file6)
        self.button6.place(x=59,y=95)
        
        self.button7 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file7)
        self.button7.place(x=59,y=135)
        
        self.button8 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file8)
        self.button8.place(x=59,y=165)
        
        self.button9 = ttk.Button(self.frame03,text=' choose File .exe',command=File.file9)
        self.button9.place(x=59,y=195)
        
        self.buttonSave = ttk.Button(self.frame03,text='Save',command=save)
        self.buttonSave.place(x=59,y=235)
        
        self.buttonBack = ttk.Button(self.frame03,text='Back',command=back)
        self.buttonBack.place(x=159,y=235)
        
        
root = tk.Tk()
root.geometry("300x300")
root.title('SRC')
root.resizable(False,False)
if __name__ == '__main__':
    win = Win(root)
    root.mainloop()

