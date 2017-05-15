from tkinter import * 

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('i can has clipboardz?')
r.destroy()

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

value = StringVar() 
value.set("texte par défaut")

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# entrée
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()

fenetre.mainloop()

