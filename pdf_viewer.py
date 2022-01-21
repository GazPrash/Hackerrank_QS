import string
def designerPdfViewer(h, word):
    alpha = string.ascii_lowercase
    heights = []
    for char in word:
        heights.append(h[alpha.find(char)])

    return max(heights)





