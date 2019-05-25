Simple Words Puzzle Search

* This is program to generate random words puzzle and searched specified words int it.
* Works with python3.7. 
* Also, use `virtualenv`. 
* To run you need to execute in the command line:
    * `--puzzle_size` -- desirable words puzzle; 
    * `--words` -- words that you try to find in the generated puzzle.

```bash
python3 -m  main --puzzle_size 15 --words find col colax max asd qweqwe aslks sadfsdfasdfasdf

In the puzzle:
c w s i b a r e o q j n b p i
j b h j v i h s t g s o d m n
d a b i p o v a j w o h x f y
j m z p o a f v l h a q a v b
q l v e k j l b i m b e p v l
i w v i r p q f l k b u g q u
k l j o h g q c m a c y d n z
w o r b t e n m g o p r i d i
d c m k m k r u j g k m u x h
k s l d z w r h n m k q v s b
s y c s w f j y n m h l r x q
l e m i l v z w l x p g g y j
r f k f u h t l l x g w n p p
k s p s v x s j q k a n a s t
k z e i a n c s w j u f j a f.
Found words: ['col', 'kanas'].
Not found words: ['colax', 'max', 'sale', 'qwerty', 'asd', 'find']
```

* To see help documentation run in the command line: 
```bash
python3 -m  main --help

usage: main.py [-h] [--puzzle_size PUZZLE_SIZE] [--words WORDS [WORDS ...]]

This is program to search words in the random puzzle.

optional arguments:
  -h, --help            show this help message and exit
  --puzzle_size PUZZLE_SIZE
                        Describes puzzle's size
  --words WORDS [WORDS ...]
                        Describes words which would be tried found in the
                        puzzle.
```

* To install dependencies and run test you can use `Makefile`:
    * To install dependencies run in the command line:
```bash
make dep
```
   * To run tests:
  ```bash
make test
``` 
