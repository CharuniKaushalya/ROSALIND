from Bio.Seq import Seq
import Bio.Alphabet

# open txt file with sequence to transcribe
f = open('rosalind_revc.txt', 'r')
# read all lines by removing newline character
data = f.read().replace('\n', '')
# close file
f.close()

# assign sequence as a DNA sequence
t = Seq(data, Bio.Alphabet.IUPAC.unambiguous_dna)
# use transcribe function
o = open('_REVC.txt', 'w')
o.write(str(t.reverse_complement()))
o.close()