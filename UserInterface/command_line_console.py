from Domain.factura import get_str, creeaza_factura
from Logic.crud import create,update,delete


def help_dialog():
    print("Usage: \n"
          "add,<id>,<nr_ap>,<suma>,<data>,<tipul>;\n"
          "remove,<id>;\n"
          "update,<id>,<nr_ap>,<suma>,<data>,<tipul>;\n"
          "showall;\n"
          "exit;\n"
          "Use ',' pentru a separa argumentul de comanda si ';' pentru a marca sfarsitul comenzii.\n"
          "\n"
          "Comenzile disponobile sunt:\n"
          "add, remove, update, showall, exit\n"
          )


def run_console_ui():
    facturi = []
    undo_list=[]
    redo_list=[]
    print("Scrie comenzi separate prin ';' apoi apasa ENTER")
    while True:
        commands_str = input(">>>")
        commands_str_lst = commands_str.split(';')
        for command in commands_str_lst:
            if command == 'exit':
                return 0
            else:
                args = command.split(',')
                if args[0] == "add":
                    facturi = validate_add(args, facturi,undo_list, redo_list)
                elif args[0] == "remove":
                    facturi = validate_remove(args, facturi,undo_list, redo_list)
                elif args[0] == "update":
                    facturi = validate_update(args, facturi,undo_list, redo_list)
                elif args[0] == "showall":
                    validate_showall(args, facturi)
                elif args[0] == "exit":
                    break
                else:
                    print(f"'{args[0]}' nu este o comanda valida!")
                    help_dialog()


def validate_add(args, facturi,undo_list, redo_list):
    if len(args) == 6:
        try:
            facturi = create(facturi, int(args[1]), int(args[2]), float(args[3]), str(args[4]),
                             str(args[5]),undo_list, redo_list)
        except ValueError:
            print("Argumentul pentru ID trebuie sa fie un numar intreg valid.\n"
                  "Argumentul pentru suma ar trebui sa fie un float valid.")
    else:
        print("Comanda 'add' se asteapta la 5 argumente.")
    return facturi




def validate_update(args, facturi,undo_list, redo_list):
    if len(args) == 6:
        try:
            facturi = update(facturi, creeaza_factura(int(args[1]), int(args[2]), float(args[3]), str(args[4]),
                             str(args[5]))
                             ,undo_list, redo_list)
        except ValueError:
            print("Argumentul pentru ID trebuie sa fie un numar intreg valid.\n"
                  "Argumentul pentru suma ar trebui sa fie un float valid.")
    else:
        print("Comanda 'update' se asteapta 5 argumente.")
    return facturi


def validate_remove(args, facturi,undo_list, redo_list):
    if len(args) == 2:
        try:
            facturi = delete(facturi, int(args[1]),undo_list, redo_list)
        except ValueError:
            print("Argumentul pentru ID trebuie sa fie un numar intreg.")
    else:
        print("Comanda 'remove' se asteapta doar la un singur argument.")
    return facturi


def validate_showall(args, facturi):
    if len(args) == 1:
        for item in facturi:
            print(get_str(item))
    else:
        print("Comanda 'showall' nu se asteapta la argumente.")