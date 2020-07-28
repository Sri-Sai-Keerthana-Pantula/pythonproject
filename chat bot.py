from tkinter import *
root=Tk()
def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        text.insert(END,"\n"+"Bot:hello")
    elif(a.get()=='hello'):
        text.insert(END,"\n","Bot:hi")
    elif(a.get()=='how are u'):
        text.insert(END,"\n"+"Bot:i am fine how are u")
    elif(a.get()=='I am fine'):
        text.insert(END,"\n"+"Bot:nice to hear u")
    else:
        text.insert(END,"\n"+"Bot:I didn't get u")
text=Text(root,bg='white')
text.grid(row=0,column=0,columnspan=4)
a=Entry(root,width=100)
send=Button(root,text='Send',bg='white',width=16,command=send)
send.place(x=540,y=380)
a.grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('simple chatbot')
root.mainloop()
