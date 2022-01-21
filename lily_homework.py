def lilysHomework(arr):
    valdic = {index:val for (index, val) in enumerate(arr)}

    sarr = arr[::]
    sarr.sort()

    changes = 0
    for ind, item in enumerate(arr):
        if item != sarr[ind]:
            changes += 1

    # TODO Karo ise koi please



    