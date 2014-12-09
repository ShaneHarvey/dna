#!/bin/env python2.7
from __future__ import print_function
import sys
import collections


def encode(infile):
    bin_to_dna = {'00': 'AT', '01': 'CG', '10': 'GC', '11': 'TA'}
    space_dash = collections.deque([[1, 0], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 3], [4, 2], [5, 0], [5, 0], [4, 2], [3, 3], [2, 4], [1, 4], [0, 4], [0, 3], [0, 2], [1, 0]])
    with open(infile, 'r') as f:
        # read in 1024 byte chunks
        chars = f.read(1024)
        while chars:
            bin_str = ''.join(format(b, 'b').zfill(8) for b in bytearray(chars))
            for i in range(0, len(bin_str) - 1, 2):
                print(' '*space_dash[0][0] + ('-'*space_dash[0][1]).join(bin_to_dna[bin_str[i:i + 2]]))
                space_dash.rotate(-1)
            chars = f.read(1024)


def decode(infile):
    dna_to_bin = {'AT': '00', 'CG': '01', 'GC': '10', 'TA': '11'}
    chars = []
    bin_str = []
    for line in open(infile, 'r'):
        try:
            bin_str.append(dna_to_bin[line.strip()[0] + line.strip()[-1]])
        except KeyError as exc:
            raise Exception(infile + ": Not in valid DNA format.")

        if len(bin_str) == 4:
            chars.append(chr(int(''.join(bin_str), 2)))
            bin_str = []
        # write out in 1024 byte chunks
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
    print('Usage: ' + sys.argv[0] + ' [-d] file')

if __name__ == '__main__':
    main()
