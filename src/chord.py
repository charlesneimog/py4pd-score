import pd
import os
from random import randint
from .pdscoreutils import getpitchKey, neoscore_midicent2note

os.environ['QT_QPA_PLATFORM'] = "xcb" 
if os.name == 'nt':
    os.environ['QT_QPA_PLATFORM'] = "windows"
try:
    from neoscore.common import *
except Exception as e:
    pd.error(str(e))
    pd.error("To fix this, send the message 'pipinstall local neoscore' to the object py4pd and restart Pd.")

def chord(pitches, **kwargs):
    neoscore.setup()
    if isinstance(pitches, str):
        pitches = [pitches]
    elif isinstance(pitches, int):
        try:
            pitches = [neoscore_midicent2note(pitches, **kwargs)]
        except BaseException as e:
            pd.error(str(e))
            return
    elif isinstance(pitches, float):
        try:
            pitches = [neoscore_midicent2note(int(pitches), **kwargs)]
        except BaseException:
            pd.error("The float must be a midicent")
            return

    if isinstance(pitches, list):
        newPitches = []
        for pitch in pitches:
            if isinstance(pitch, str):
                newPitches.append(pitch)
            elif isinstance(pitch, int):
                newPitches.append(neoscore_midicent2note(pitch, **kwargs))
            elif isinstance(pitch, float):
                newPitches.append(neoscore_midicent2note(int(pitch, **kwargs)))

            else:
                pd.error("The list must contain only strings (c4, c#4, c+4, etc) or integers (midicents)")
                return
        pitches = newPitches
    pitches = [x.lower() for x in pitches]
    py4pdTMPfolder = pd.get_temp_dir()
    staffSoprano = Staff((Mm(0), Mm(0)), None, Mm(30))
    trebleClef = 'treble'
    Clef(ZERO, staffSoprano, trebleClef)
    staffBaixo = Staff((ZERO, Mm(15)), None, Mm(30))
    bassClef = 'bass'
    Clef(ZERO, staffBaixo, bassClef)
    Path.rect((Mm(-10), Mm(-10)), None, Mm(42), Mm(42),
              Brush(Color(255, 255, 255, 0)), Pen(thickness=Mm(0)))

    for pitch in pitches:
        pitchWithoutNumber = pitch.replace(pitch[-1], '')
        pitchOctave = int(pitch[-1])
        pitchClass, accidental = getpitchKey(pitchWithoutNumber)
        note = [(pitchClass, accidental, pitchOctave)]
        try:
            if pitchOctave < 4:
                Chordrest(Mm(5), staffBaixo, note, (int(1), int(1)))
            else:
                Chordrest(Mm(5), staffSoprano, note, (int(1), int(1)))
        except Exception as e:
            pd.error(e)
            return

    scoreNumber = pd.get_obj_var('scoreNumber')
    if scoreNumber is None:
        scoreNumber = 0
    notePathName = py4pdTMPfolder + "/" + pd.get_obj_pointer() + "_" + str(scoreNumber) + ".ppm"
    pd.set_obj_var('scoreNumber', scoreNumber + 1)
    patchZoom = pd.get_patch_zoom()
    if (patchZoom == 1):
        scoreZoom = 75
    elif (patchZoom == 2):
        scoreZoom = 150
    else:
        pd.error("The zoom of the patch is other than 1 or 2, using the default image")
        scoreZoom = 75


    neoscore.render_image(rect=None, dest=notePathName, dpi=scoreZoom, wait=True)
    neoscore.shutdown()
    if os.name == 'nt':
        notePathName = notePathName.replace("\\", "/")
    pd.show_image(notePathName)
    return None

