def retornaIndicesCateg(lIndex, lCateg, nomCateg)
    nuevaLista = []
    nuevaLista2 = []

    for i in lCateg:
        if nomCateg == i:
            indice = lCateg,index(i)
            nuevaLista.append(indice)
            lCateg.remove(nomCateg)
            lCateg.insert(indice, "")
    for a in lIndex:
        for b in nuevaLista:
            if a == b:
                nuevaLista2. append(a)
    return nuevaLista2

    print(retornaIndicesCateg([3, 2, 0, 4, 6], ['futbol', 'voleibol', 'voleibol', 'voleibol', 'atletismo', 'ajedrez', 'futbol', 'boxeo', 'natación'], 'voleibol')
