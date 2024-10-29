import os

import pd

from score.chord import chord

if os.name == "nt":
    os.environ["QT_QPA_PLATFORM"] = "windows"

from neoscore.common import *

def py4pdLoadObjects():
    currentFile = os.path.dirname(__file__)
    patchZoom = pd.get_patch_zoom()
    if patchZoom == 1:
        scoreImage = f"{currentFile}/resources/score_nozoom.gif"
    elif patchZoom == 2:
        scoreImage = f"{currentFile}/resources/score.gif"
    
    # py.chord
    chordObj = pd.new_object("py.chord")
    chordObj.addmethod_anything(chord)
    chordObj.image = scoreImage
    chordObj.fig_size = (250, 250)
    chordObj.type = pd.VIS
    chordObj.add_object()
    

