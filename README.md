#DNA
DNA is a simple encoding scheme that translates files to and from DNA.

Simply build & run
```bash
$ gcc dna.c -o dna
$ ./dna dna.c > dna.c.dna
$ ./dna -d dna.c.dna > dna2.c
$ diff dna.c dna2.c
```

Or run the Python version
```bash
$ python dna.py dna.py > dna.py.dna
$ python dna.py -d dna.py.dna > dna2.py
$ diff dna.py dna2.py
```

The output looks like this
```bash
$ ./dna dna.c
 AT
G--C
A---T
T----A
 C----G
  G----C
   G---C
    C--G
     CG
     GC
    T--A
   G---C
  C----G
 G----C
A----T
T---A
C--G
 GC
 TA
A--T
C---G
T----A
 C----G
  C----G
   C---G
    G--C
     CG
...
```

#Inspiration
Inspired by [Yusuke Endoh](https://github.com/mame)'s Ruby [DoubleHelix](https://github.com/mame/doublehelix) utility.
