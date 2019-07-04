import random 
import attr
import pprint

from whitachords import *
from exceptions import *

def niceprint(anything):
    pprint.PrettyPrinter(indent=2).pprint(anything)

def difference(original, comparison):
    return list(set(original) - set(comparison))

def similarity(original, comparison):
    try:
        return [x for x in original if x in original and x in comparison]
    except:
        print original, comparison

def percentSimilar(original, comparison):
    return float(len(similarity(original, comparison)))/float(len(original))

def percentDifferent(original, comparison):
    return float(len(difference(original, comparison)))/float(len(original))

class scales:
    @staticmethod
    def twelvetone(scale):
        return ''.join([str(x) for x in scale])\
                    .replace('10','t').replace('11','e')

    ionian = [0, 2, 4, 5, 7, 9, 11]
    major = ionian
    dorian = [0, 2, 3, 5, 7, 9, 10]
    phrygian = [0, 1, 3, 5, 7, 8, 10]
    lydian = [0, 2, 4, 6, 7, 9, 11]
    mixolydian = [0, 2, 4, 5, 7, 9, 10]
    aeolian = [0, 2, 3, 5, 7, 8, 10]
    minor = aeolian
    locrian = [0, 1, 3, 5, 6, 8, 10]
    acoustic = [0, 2, 4, 6, 7, 9, 10]
    double_harmonic = [0, 1, 4, 5, 7, 8, 11]
    algerian = [0, 2, 2, 3, 3, 5, 6, 7, 8, 11]
    altered = [0, 1, 3, 4, 6, 8, 10]
    augmented = [0, 3, 4, 7, 8, 11]
    bebop_dominant = [0, 2, 4, 5, 7, 9, 10, 11]
    blues = [0, 3, 5, 6, 7, 10]
    double_harmonic = [0, 1, 4, 5, 7, 8, 11]
    enigmatic = [0, 1, 4, 6, 8, 10, 11]
    flamenco = [0, 1, 4, 5, 7, 8, 11]
    romani = [0, 2, 3, 6, 7, 8, 10]
    half_diminished = [0, 2, 3, 5, 6, 8, 10]
    harmonic_major = [0, 2, 4, 5, 7, 8, 11]
    harmonic_minor = [0, 2, 3, 5, 7, 8, 11]
    hirajoshi = [0, 4, 6, 7, 11]
    hungarian = [0, 2, 3, 6, 7, 8, 11]
    in_ = [0, 1, 5, 7, 8]
    insen = [1, 1, 5, 7, 11]
    istrian = [1, 3, 4, 6]
    iwato = [0, 1, 5, 6, 10]
    major_pentatonic = [0, 2, 4, 7, 9]
    minor_pentatonic = [0, 3, 5, 7, 10]
    melodic_minor_asc = [0, 2, 3, 5, 7, 9, 11]
    melodic_minor_desc = [0, 2, 4, 5, 7, 9, 10]
    persian = [0, 1, 4, 5, 6, 8, 11]
    phrygian_dom = [0, 1, 4, 5, 7, 8, 10]
    prometheus = [0, 2, 4, 6, 9, 10]
    harmonics = [0, 3, 4, 5, 7, 9]
    tritone = [0, 1, 4, 6, 7, 10]
    ukranian_dorian = [0, 2, 3, 6, 7, 9, 10]
    whole = [0, 2, 4, 6, 8, 10]
    yo = [0, 3, 5, 7, 10]
    #chromatic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def keys(intervals, scale):
    #does this scale have intervals inside as valid notes?
    for note in scale:
        intersect = list(set(intervals).intersection([(x-note)%12 for x in scale])) 
        intersect.sort()
        if intersect == intervals:
            return True, scale.index(note) #return the offset
    return False, False


def allScales():
    return sorted(set([ x if '__' not in x else None for x in dir(scales) ]))[1:]


class chord(WhitaChord):
    def __init__(self, twelve_tone, root, appearances=1):
        super(chord, self).__init__()
        self.intervals = self._parseInput(twelve_tone)
        self.root = str(root).title()
        self.pitches = self._transpose()
        self.voices = len(self.intervals)
        self.appearances = int(appearances)

    def _parseInput(self, twelve_tone):
        if type(twelve_tone) == type([]):
            return twelve_tone
        if type(twelve_tone) == type('s'):
            chord = [ttconverter[x]  if x in ttconverter.keys()\
                     else int(x) for x in twelve_tone]
            return chord
        else:
            raise BadInput(twelve_tone)

    def _transpose(self):
        offset = pitchnames.index(self.root)
        notes = []
        for value in self.intervals:
            notes.append((offset + int(value)) % 12)
        return [pitchnames[x].title() for x in notes]

    def closestScale(self):
        bestfit = ['']
        previous_similarity = -1
        for name, scale in vars(scales).items():
            if type(scale) is not type([]):
                print 'byo'
                continue

            current_similarity = similarity(self.chord, scale)
            if len(current_similarity) >= previous_similarity:
                bestfit = scale
                bestname = name
                print name, bestfit, current_similarity
                previous_similarity = len(current_similarity)
        print bestname, bestfit



def demo():        
    print "MAJOR SCALE"
    print scales.twelvetone(scales.major)
    print "C MAJOR"
    b = chord('047', 'C')
    print b.pitches
    print "C MINOR"
    print chord(scales.minor, 'C').pitches

    SCALE1 = scales.major
    SCALE2 = scales.yo
    print difference(SCALE1, SCALE2)
    print similarity(SCALE1, SCALE2)

    print percentSimilar(SCALE1, SCALE2)
    print percentDifferent(SCALE1, SCALE2)
    print len(SCALE1), len(SCALE2)

    print  percentSimilar(SCALE1, SCALE2) + percentDifferent(SCALE1, SCALE2)


def demo2():
    #lets get all the chords and see which scales they can be fit into:
    all_my_chords = []
    chords = whitachords.split('\n')
    for ch in chords:
        c = chord(ch.split(' ')[0],'C', ch.split(' ')[1])
        for name, scale in vars(scales).items():
            if type(scale) is not type([]):
                continue
            a, b =  keys(c.intervals, scale)
            if a == True:
                c.keys.update({name:{'scale':scale, 'offset':b} } )
        all_my_chords.append(c)

    #niceprint(all_my_chords)

    current_chords = []
    for i in [3, 29, 77, 114]:
        #current_chords.append( all_my_chords[random.randint(0,len(all_my_chords))] )
        current_chords.append( all_my_chords[i] )

    allkeys = []
    for c in current_chords:
        allkeys.append( [a[0] for a in c.keys.iteritems() ])
    
    first = list(set(allkeys[0]).intersection(allkeys[1]))
    second =  list(set(allkeys[1]).intersection(allkeys[2]))
    third = list(set(allkeys[2]).intersection(allkeys[3]))
    
    a = list(set(first).intersection(second))
    b = list(set(second).intersection(third))

    print list(set(a).intersection(b))


class chordChange(WhitaChord):
    def __init__(self, current_chord, next_chord):
        self.current_chord = current_chord
        self.next_chord  = next_chord
        self.difference = self._getDifference()
        self.similarity = 1 - self.difference 
    
    def _getDifference(self):
        return percentDifferent(self.current_chord, self.next_chord)

    def _getSimilarity(self):
        return percentSimilar(self.current_chord, self.next_chord)


class toneSpace(chord):
    def __init__(self):
        self.tones = self._generateTones()

    def _generateTones(self):
        chords = whitachords.split('\n')
        just_chords = {}
        for chord in chords:
            just_chords.update({chord.split(' ')[0] : chord.split(' ')[1]})
        return just_chords



if __name__ == '__main__':
    demo()
    exit(0)

    all_my_chords = []
    chords = whitachords.split('\n')
    for ch in chords:
        c = chord(ch.split(' ')[0],'C', ch.split(' ')[1])
        for name, scale in vars(scales).items():
            if type(scale) is not type([]):
                continue
            a, b =  keys(c.intervals, scale)
            if a == True:
                #print "GOT ONES"
                #print c.intervals
                c.keys.update({name:{'scale':scale, 'offset':b} } )
        #print c.intervals
        #print c.keys
        all_my_chords.append(c)

    #niceprint(all_my_chords)

    current_chords = []
    for i in [3, 29, 77, 114]:
        #current_chords.append( all_my_chords[random.randint(0,len(all_my_chords))] )
        current_chords.append( all_my_chords[i] )

    allkeys = []
    for c in current_chords:
        #niceprint( [a[0] for a in c.keys.iteritems()] )
        allkeys.append( [a[0] for a in c.keys.iteritems() ])
        #keys = [a[0] for a in c.keys.iteritems()] 
    #niceprint(allkeys)
    #print set(allkeys[0])
    first = list(set(allkeys[0]).intersection(allkeys[1]))
    second =  list(set(allkeys[1]).intersection(allkeys[2]))
    third = list(set(allkeys[2]).intersection(allkeys[3]))
    #fourth = set(allkeys[3]).intersection(allkeys[4])

    #print first
    #print second
    #print third

    a = list(set(first).intersection(second))
    b = list(set(second).intersection(third))

    print list(set(a).intersection(b))


    exit(0)
