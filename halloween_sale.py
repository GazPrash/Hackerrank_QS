def howManyGames(p, d, m, s):
    games = 0
    while s >= p:
        if games == 0:
            s -= p
            games += 1
        elif (p-d) > m:
            p -= d
            s -= p
            games += 1
        elif (p-d) <= m: 
            p = m
            s -= p
            games += 1

    return games

    