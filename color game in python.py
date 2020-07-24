import tkinter
import random

colors=['Red','Blue','Green','pink','Black','orange','Yellow','White','purple']
score=0
timeleft=5

def startGame(event):
    if timeleft==5:
        countdown()
    nextColor()
def nextColor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            score+=1
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]),text=str(colors[0]))
        scoreLabel.config(text="Score"+str(score))
    else:
        print("end game")
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text="Timeleft"+str(timeleft))
        timeLabel.after(1000,countdown)

root=tkinter.Tk()
root.title("colorgame")
root.geometry("400x200")
scoreLabel=tkinter.Label(root,text='press enter')
scoreLabel.pack()
timeLabel=tkinter.Label(root,text="Timeleft:"+str(timeleft))
timeLabel.pack()
label=tkinter.Label(root,font=("helvetica",60))
label.pack()
e=tkinter.Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()
        
