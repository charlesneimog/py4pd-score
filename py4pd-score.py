import os

import pd

from src.chord import chord

if os.name == "nt":
    os.environ["QT_QPA_PLATFORM"] = "windows"
try:
    from neoscore.common import *
except Exception as e:
    pd.error(str(e))
    pd.error(
        "To fix this, send the message 'pipinstall global neoscore' to the object py4pd and restart Pd."
    )


def py4pdLoadObjects():
    patchZoom = pd.get_patch_zoom()
    if patchZoom == 1:
        scoreImage = "./resources/score_nozoom.gif"
    elif patchZoom == 2:
        scoreImage = "./resources/score.gif"
    
    # py.chord
    chordObj = pd.new_object("py.chord")
    chordObj.addmethod_anything(chord)
    chordObj.image = scoreImage
    chordObj.fig_size = (250, 250)
    chordObj.type = pd.VIS
    chordObj.add_object()
    

