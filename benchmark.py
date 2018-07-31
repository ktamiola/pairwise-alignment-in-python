from modules.alignment import needle, water
from modules.alignmentJit import needleJ, waterJ

import time

# Init protein sequences
seq1 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

seq2 = 'AAAAAAAAPAAAAPAAAAAAAAAAPAAAAPAAAAAAAAAAPAAAAPAA'

def testMe(func, *args):
    start = time.time()
    for i in range(args[2]):
        func(args[0], args[1])
    end = time.time()
    print('- {:^10} {:8.1f}/s'.format(func.__name__, args[2]/(end-start)))


print('')
testMe(needle, seq1, seq2, 100)
testMe(water, seq1, seq2, 100)
print('')

print('')
testMe(needleJ, seq1, seq2, 100)
testMe(waterJ, seq1, seq2, 100)
print('')
