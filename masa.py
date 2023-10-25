def kg_gramos (kilogramos):
    return kilogramos * 1000

def kg_toneladas  (kilogramos):
    return kilogramos / 1000

def toneladas_gramos (toneladas):
    return toneladas * 1000

if __name__=="__main__":
    kilogramos =  2.5
    gramos= kg_gramos(kilogramos)
    print(f"{kilogramos}kg son equivalentesa {gramos} g ")