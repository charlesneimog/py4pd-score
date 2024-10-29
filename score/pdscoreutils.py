import pd


def neoscore_midicent2note(midicent, **kwargs):
    """
    Converts a midicent note number to a note name string.
    """
    if isinstance(midicent, list):
        return [neoscore_midicent2note(x, **kwargs) for x in midicent]

    note_names = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
        "C",
    ]

    # multiply by 0.01, then round to nearest integer, then multiply by 100
    newmidicent = round(float(midicent) * 0.01) * 100
    desviation = midicent - newmidicent
    desviation = round(desviation, 1)
    octave = int(midicent // 1200) - 1
    note = int(newmidicent / 100) % 12

    if desviation > 45 and desviation < 55:
        return f"{note_names[note]}+{octave}"
    elif desviation < -45 and desviation > -55:
        return f"{note_names[note]}-{octave}"
    elif desviation > -5 and desviation < 5:
        return f"{note_names[note]}{octave}"
    else:
        pd.error(
            "Error: midicent2note: desviation out of range of our current notation system"
        )
        return f"{note_names[note]}{octave}"


def getpitchKey(pitch, cents=0):
    note = {
        # natural
        "c": ["c", ""],
        "d": ["d", ""],
        "e": ["e", ""],
        "f": ["f", ""],
        "g": ["g", ""],
        "a": ["a", ""],
        "b": ["b", ""],
        # sharp
        "c#": ["c", "accidentalSharp"],
        "d#": ["d", "accidentalSharp"],
        "e#": ["e", "accidentalSharp"],
        "f#": ["f", "accidentalSharp"],
        "g#": ["g", "accidentalSharp"],
        "a#": ["a", "accidentalSharp"],
        "b#": ["b", "accidentalSharp"],
        # flat
        "cb": ["c", "accidentalFlat"],
        "db": ["d", "accidentalFlat"],
        "eb": ["e", "accidentalFlat"],
        "fb": ["f", "accidentalFlat"],
        "gb": ["g", "accidentalFlat"],
        "ab": ["a", "accidentalFlat"],
        "bb": ["b", "accidentalFlat"],
        # quarter-tone sharp
        "c+": ["c", "accidentalQuarterToneSharpStein"],
        "d+": ["d", "accidentalQuarterToneSharpStein"],
        "e+": ["e", "accidentalQuarterToneSharpStein"],
        "f+": ["f", "accidentalQuarterToneSharpStein"],
        "g+": ["g", "accidentalQuarterToneSharpStein"],
        "a+": ["a", "accidentalQuarterToneSharpStein"],
        "b+": ["b", "accidentalQuarterToneSharpStein"],
        # quarter-tone flat
        "c-": ["c", "accidentalQuarterToneFlatStein"],
        "d-": ["d", "accidentalQuarterToneFlatStein"],
        "e-": ["e", "accidentalQuarterToneFlatStein"],
        "f-": ["f", "accidentalQuarterToneFlatStein"],
        "g-": ["g", "accidentalQuarterToneFlatStein"],
        "a-": ["a", "accidentalQuarterToneFlatStein"],
        "b-": ["b", "accidentalQuarterToneFlatStein"],
        # three-quarter-tone sharp
        "c#+": ["c", "accidentalThreeQuarterTonesSharpStein"],
        "d#+": ["d", "accidentalThreeQuarterTonesSharpStein"],
        "e#+": ["e", "accidentalThreeQuarterTonesSharpStein"],
        "f#+": ["f", "accidentalThreeQuarterTonesSharpStein"],
        "g#+": ["g", "accidentalThreeQuarterTonesSharpStein"],
        "a#+": ["a", "accidentalThreeQuarterTonesSharpStein"],
        "b#+": ["b", "accidentalThreeQuarterTonesSharpStein"],
        # three-quarter-tone flat
        "cb-": ["c", "accidentalThreeQuarterTonesFlatZimmermann"],
        "db-": ["d", "accidentalThreeQuarterTonesFlatZimmermann"],
        "eb-": ["e", "accidentalThreeQuarterTonesFlatZimmermann"],
        "fb-": ["f", "accidentalThreeQuarterTonesFlatZimmermann"],
        "gb-": ["g", "accidentalThreeQuarterTonesFlatZimmermann"],
        "ab-": ["a", "accidentalThreeQuarterTonesFlatZimmermann"],
        "bb-": ["b", "accidentalThreeQuarterTonesFlatZimmermann"],
    }
    return note[pitch]
