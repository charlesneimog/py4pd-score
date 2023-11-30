import pd
from src.chord import chord


def py4pdLoadObjects():
    patchZoom = pd.get_patch_zoom()
    pd.print(patchZoom)
    if (patchZoom == 1):
        scoreImage = './resources/score.gif'
    elif (patchZoom == 2):
        scoreImage = './resources/score_nozoom.gif'
    else:
        pd.error("The zoom of the patch is other than 1 or 2, using the default image")
        scoreImage = './resources/score.png'
    pd.add_object(chord, 'py.chord', objtype=pd.VIS), objimage=scoreImage)
        
    pd.add_object(chord, 'py.chord', objtype=pd.VIS, objimage=scoreImage)
