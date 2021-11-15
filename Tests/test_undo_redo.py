from Logic.crud import create, read
from Logic.undo_redo import do_undo, do_redo


def test_undo_si_redo():
    undo_list = []
    redo_list = []
    facturi = []

    facturi = create(facturi, 1, 10, 500, '16/12/2020', 'caldura', undo_list, redo_list)
    facturi = create(facturi, 2, 10, 700, '1/12/2020', 'chirie', undo_list, redo_list)
    facturi = create(facturi, 3, 12, 850, '6/1/2020', 'intretinere', undo_list, redo_list)

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi[0] == [1, 10, 500, '16/12/2020', 'caldura']
    assert facturi[1] == [2, 10, 700, '1/12/2020', 'chirie']
    assert read(facturi, 3) is None

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi[0] == [1, 10, 500, '16/12/2020', 'caldura']
    assert read(facturi, 2) is None
    assert read(facturi, 3) is None

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert read(facturi, 1) is None
    assert read(facturi, 2) is None
    assert read(facturi, 3) is None

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert read(facturi, 1) is None
    assert read(facturi, 2) is None
    assert read(facturi, 3) is None

    facturi = create(facturi, 2, 13, 500, '10/2/2021', 'caldura', undo_list, redo_list)
    facturi = create(facturi, 9, 13, 120, '12/12/2021', 'gaz', undo_list, redo_list)
    facturi = create(facturi, 8, 13, 850, '6/9/2020', 'intretinere', undo_list, redo_list)

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [9, 13, 120, '12/12/2021', 'gaz']
    assert facturi[2] == [8, 13, 850, '6/9/2020', 'intretinere']

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert read(facturi, 9) is None
    assert read(facturi, 8) is None

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [9, 13, 120, '12/12/2021', 'gaz']
    assert read(facturi, 8) is None

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [9, 13, 120, '12/12/2021', 'gaz']
    assert facturi[2] == [8, 13, 850, '6/9/2020', 'intretinere']

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
        if len(undo_list) > 0:
            facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert read(facturi, 9) is None
    assert read(facturi, 8) is None

    facturi = create(facturi, 4, 40, 450, '8/8/2008', 'caldura', undo_list, redo_list)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [4, 40, 450, '8/8/2008', 'caldura']

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [4, 40, 450, '8/8/2008', 'caldura']

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert read(facturi, 4) is None

    if len(undo_list) > 0:
        facturi = do_undo(undo_list, redo_list, facturi)
    assert facturi == []

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [4, 40, 450, '8/8/2008', 'caldura']

    if len(redo_list) > 0:
        facturi = do_redo(undo_list, redo_list, facturi)
    assert facturi[0] == [2, 13, 500, '10/2/2021', 'caldura']
    assert facturi[1] == [4, 40, 450, '8/8/2008', 'caldura']
