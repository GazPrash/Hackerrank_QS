def fairRations(B):
    n = len(B)
    sums = 0
    last_ind = -1

    for x in B:
        if (x%2) != 0:
            if last_ind == -1:
                last_ind = note_ind
            else:
                sums += abs(last_ind - x) * 2
                last_ind = -1

    if len(note_ind) %2 != 0:
        return 'NO'

    return str(sums)


# YET ANOTHER CRASH LANDED....Cant have a home on this planet...
