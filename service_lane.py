def lane(width, cases):
    note = []
    for case in cases:
        note.append(min(width[case[0]:(case[1]+1)]))

    return note
