# Versió 1 
assignatures = ['Matemàtiques','Llengua Catalana','Ciències Naturals','Història','Educació Física','Anglès']
inp= input("Ecriu les notes de cada assignatura: ")
notes=inp.split()
print(assignatures)
print(notes)
i=0
for x in assignatures:
    print("A "+x+" ha tret "+notes[i])
    i+=1

# Versió 2 
assignatures = ('Matemàtiques','Llengua Catalana','Ciències Naturals','Història','Educació Física','Anglès')
inp= input("Ecriu les notes de cada assignatura: ")
notes=inp.split()
print(assignatures)
print(notes)
i=0
for x in assignatures:
    print("A "+x+" ha tret "+notes[i])
    i+=1
