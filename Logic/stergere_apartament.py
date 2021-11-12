from Domain.factura import get_nr_ap

def delete_ap(lst_facturi,nr_ap,undo_list,redo_list):
    '''
    Eliminarea facturilor unui apartament
    :param lst_facturi: Lista facturilor
    :param nr_ap: Numarul apartamenului caruia i se sterg facturile
    :return: Lista facturilor fara cele de la un apartament dorit
    '''
    new_facturi= []
    undo_list.append(lst_facturi)
    redo_list.clear()
    for factura in lst_facturi:
        if get_nr_ap(factura)!=nr_ap:
            new_facturi.append(factura)
    return new_facturi


#undo_list.append(lst_facturi)

#def handle_delete_apartament(facturi):
  #  nr_ap=int(input("Dati numarul apartamentului caruia i se sterg facturile: "))
#    facturi=delete_ap(facturi,nr_ap)
  #  print(("Stergerea tuturor facturilor apartamentului selectat a fost efectuata cu succes."))
  #  return facturi
