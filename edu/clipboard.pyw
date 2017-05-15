from tkinter import * 

fenetre = Tk()

value = StringVar() 
value.set("texte par défaut")

# entrée
value = StringVar() 
value.set("texte")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

fenetre.clipboard_clear()
fenetre.clipboard_append('i can has clipboardz ?')

fenetre.mainloop()

