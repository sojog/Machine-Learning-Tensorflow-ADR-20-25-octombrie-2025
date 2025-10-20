## PYTHON este imperativ ( procedural + orientat obiect ) + functional
## OOP - Object Oriented Programming

## NUMELE clasei este cu litera MARE!!
class Masina:
    ## FUNCTIILE cu __ sunt considerate magice
    ## self -> echivalent lui this din alte limbaje  ( pointer catre obiectul curent)
    ## __init__ -> un fel de constructor (initializator)
    def __init__(self, cp, an):
        self.capacitate = cp
        self.an = an

    ## __str__ -> functie magica, folosita pentru conversie la string (este folosita de catre functia print) 
    def __str__(self):
        return f"Masina cu {self.capacitate} cp din anul {self.an}"


# __main__ -> modulul principal
print(Masina)

obiect_masina = Masina(100, 2024)
print(obiect_masina)


obiect_masina2 = Masina(70, 2014)
print(obiect_masina2)


