def do_undo(undo_list, redo_list, current_list):
    """
    Functionalitatea undo
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :param current_list: Lista curenta
    :return: undo_list
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo
    return None


def do_redo(undo_list, redo_list, current_list):
    """
    Functionalitatea redo
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :param current_list: Lista curenta
    :return: redo_list
    """

    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    return None
