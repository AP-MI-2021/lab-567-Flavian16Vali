from Domain.factura import get_data
from Domain.factura import get_suma
from Domain.factura import get_nr_ap

def get_luna(factura):
    '''
    Returneaza luna
    :param factura:O factura
    :return: Data in care a fost emisa factura
    '''
    data_dorita=0
    p=1
    s=0
    luna_factura=get_data(factura)
    for j in luna_factura:
        if j=='/':
            s=s+1
        if s==1 and j!='/':
            data_dorita=data_dorita*p+int(float(j))
            p=p*10
    return data_dorita

def suma_ap(facturi):
    '''
    Sa se determine suma de la un apartament pentru o luna
    :param facturi: Lista cu facturi
    :return: Sumele facturilor
    '''
    sume_ap1=[0]*99999
    sume_ap2=[0]*99999
    sume_ap3=[0]*99999
    sume_ap4=[0]*99999
    sume_ap5=[0]*99999
    sume_ap6=[0]*99999
    sume_ap7=[0]*99999
    sume_ap8=[0]*99999
    sume_ap9=[0]*99999
    sume_ap10=[0]*99999
    sume_ap11=[0]*99999
    sume_ap12=[0]*99999
    nr_apartament=[-1]*99999
    for factura in facturi:
        if nr_apartament[get_nr_ap(factura)]==-1:
            nr_apartament[get_nr_ap(factura)]=0

    for i in range(0,len(nr_apartament)):
        for factura in facturi:
            if i==get_nr_ap(factura):
                if 1==get_luna(factura):
                    sume_ap1[i]=sume_ap1[i]+get_suma(factura)
                if 2==get_luna(factura):
                    sume_ap2[i]=sume_ap2[i]+get_suma(factura)
                if 3==get_luna(factura):
                    sume_ap3[i]=sume_ap3[i]+get_suma(factura)
                if 4==get_luna(factura):
                    sume_ap4[i]=sume_ap4[i]+get_suma(factura)
                if 5==get_luna(factura):
                    sume_ap5[i]=sume_ap5[i]+get_suma(factura)
                if 6==get_luna(factura):
                    sume_ap6[i]=sume_ap6[i]+get_suma(factura)
                if 7==get_luna(factura):
                    sume_ap7[i]=sume_ap7[i]+get_suma(factura)
                if 8==get_luna(factura):
                    sume_ap8[i]=sume_ap8[i]+get_suma(factura)
                if 9==get_luna(factura):
                    sume_ap9[i]=sume_ap9[i]+get_suma(factura)
                if 10==get_luna(factura):
                    sume_ap10[i]=sume_ap10[i]+get_suma(factura)
                if 11==get_luna(factura):
                    sume_ap11[i]=sume_ap11[i]+get_suma(factura)
                if 12==get_luna(factura):
                    sume_ap12[i]=sume_ap12[i]+get_suma(factura)

    a=0
    print("Luna ianuarie:")
    for i in range(0,len(sume_ap1)):
        if nr_apartament[i]!=-1:
            if sume_ap1[i]!=0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap1[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna februarie")
    for i in range(0,len(sume_ap2)):
        if nr_apartament[i]!=-1:
            if sume_ap2[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap2[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna martie:")
    for i in range(0, len(sume_ap3)):
        if nr_apartament[i] != -1:
            if sume_ap3[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap3[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna aprilie:")
    for i in range(0, len(sume_ap4)):
        if nr_apartament[i] != -1:
            if sume_ap4[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap4[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna mai:")
    for i in range(0, len(sume_ap5)):
        if nr_apartament[i] != -1:
            if sume_ap5[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap5[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna iunie:")
    for i in range(0, len(sume_ap6)):
        if nr_apartament[i] != -1:
            if sume_ap6[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap6[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna iulie")
    for i in range(0, len(sume_ap7)):
        if nr_apartament[i] != -1:
            if sume_ap7[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap7[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna august:")
    for i in range(0, len(sume_ap8)):
        if nr_apartament[i] != -1:
            if sume_ap8[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap8[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna septembrie:")
    for i in range(0, len(sume_ap9)):
        if nr_apartament[i] != -1:
            if sume_ap9[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap9[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna octombrie:")
    for i in range(0, len(sume_ap10)):
        if nr_apartament[i] != -1:
            if sume_ap10[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap10[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna noiembrie")
    for i in range(0, len(sume_ap11)):
        if nr_apartament[i] != -1:
            if sume_ap11[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap11[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")

    a=0
    print("Luna decembrie")
    for i in range(0, len(sume_ap12)):
        if nr_apartament[i] != -1:
            if sume_ap12[i] != 0:
                print("Apartamentul cu numarul: ",i," are de achitat suma: ",sume_ap12[i], " RON")
                a=1
    if a==0:
        print("Nu exista facturi in aceasta luna.")
