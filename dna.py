from __future__ import print_function
import sys
import collections


def encode(infile):
    space_dash = collections.deque([[1, 0], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 3], [4, 2], [5, 0], [5, 0], [4, 2], [3, 3], [2, 4], [1, 4], [0, 4], [0, 3], [0, 2], [1, 0]])
    with open(infile, 'r') as f:
        while True:
            dna = []
            # read in 1024 byte chunks
            chars = f.read(1024)
            if not chars:
                break
            bin_str = ''.join(format(b, 'b').zfill(8) for b in bytearray(chars))
            for i in range(0, len(bin_str) - 1, 2):
                case = bin_str[i:i + 2]
                if(case == '00'):
                    dna.append('AT')
                elif(case == '01'):
                    dna.append('CG')
                elif(case == '10'):
                    dna.append('GC')
                elif(case == '11'):
                    dna.append('TA')
            for i in range(len(dna)):
                print(' '*space_dash[0][0] + ('-'*space_dash[0][1]).join(dna[i]))
                space_dash.rotate(-1)


def decode(infile):
    # write out in 1024 byte chunks
    chars = []
    bin_str = []
    for line in open(infile, 'r'):
        case = line.strip()[0] + line.strip()[-1]
        if(case == 'AT'):
            bin_str.append('00')
        elif(case == 'CG'):
            bin_str.append('01')
        elif(case == 'GC'):
            bin_str.append('10')
        elif(case == 'TA'):
            bin_str.append('11')
        else:
            raise Exception(infile + ": Not in valid DNA format.")

        if len(bin_str) == 4:
            chars.append(chr(int(''.join(bin_str), 2)))
            bin_str = []
        if len(chars) == 1024:
            print(''.join(chars), end='')
            chars = []
    if len(bin_str) != 0:
        raise Exception(infile + ": Not in valid DNA format.")
    if chars:
        print(''.join(chars), end='')


def main():
    if len(sys.argv) == 2:
        encode(sys.argv[1])
        return
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-d':
            decode(sys.argv[2])
            return
    print('Usage: \tdna.py file_to_encode\n\tdna.py -d file_to_decode.dna')

if __name__ == '__main__':
	main()