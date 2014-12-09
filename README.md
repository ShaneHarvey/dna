#DNA
DNA is a simple encoding scheme that translates data to and from double helix format.

Simply build & run
```bash
$ gcc -Wall -Werror -o dna dna.c
$ ./dna dna > dna.dna
$ ./dna -d dna.dna > newdna
$ chmod +x newdna
$ ./newdna dna.c
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
     AT
    C--G
   G---C
  C----G
 C----G
A----T
G---C
A--T
 AT
 AT
T--A
T---A
...
```

Similarly run the Python version
```bash
$ ./dna.py dna.py > dna.py.dna
$ ./dna.py -d dna.py.dna > dna2.py
$ diff dna.py dna2.py

```
#Inspiration
Inspired by [Yusuke Endoh](https://github.com/mame)'s Ruby [DoubleHelix](https://github.com/mame/doublehelix) utility.
