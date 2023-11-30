import pd
from src.chord import chord


def py4pdLoadObjects():
    patchZoom = pd.get_patch_zoom()
    if (patchZoom == 1):
        scoreImage = './resources/score_nozoom.gif'
    elif (patchZoom == 2):
        scoreImage = './resources/score.gif'
    pd.add_object(chord, 'py.chord', objtype=pd.VIS, objimage=scoreImage)
