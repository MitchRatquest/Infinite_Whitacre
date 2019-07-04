# Infinite_Whitacre

This was inspired by [Added-Tone Sonorities in the Choral Music of Eric
Whitacre](https://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1736&context=etd) by Angela Hall. This thesis (dissertation?) has appendix B, starting on page 149, which details each permutation of Whitacre's chord structures. Appendix C, page 159, has a list of his chord types and their appearances in the sections of music analyzed. 

The author used twelve tone notation to describe these, which was new to me, but ultimately very useful and simple. Assuming the lowest sounding (or root) note is 0, we count the intervals which make up the chord. In this way, a major chord would be 047, which is a root, a major third(4), and a major fifth(7). The letters t and e are used for 10 and 11 respectively. 

So far, I have done the data entry of appendix C, only recording the chord Type and Appearance, as I did not care about the structures too much while doing so. They are the variable 'whitachords' in whitachords.py. I have some scales and a rudimentary chord object which help me place these chords in context with each other and any scale.

This is all **very much** an unstable first draft. I might decide to change everything up one day. Right now, I'm only playing with tonality vs atonality. I hope to include some very basic concepts of rhythm and grace notes, along with the probability of chords appearing, and using the huge 7 tone chords as 'pivot points' in the compositions. 

I also intend to create a puredata patch which will interface directly with the python script to do this all in real time. 
