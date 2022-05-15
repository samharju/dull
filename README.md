# dull

This is a plain and boring package providing one decorator for dumping profile stats to console
or to a file for further inspections.

There are a million of nice packages providing decorators and context managers that
can dump cProfile stats and generate visual stuff from them. But usually that is a little
too much for just taking a peek at performance of a function. I found myself writing this
wrapper again and again or copypasting it around, so why not package it for convenience?

Install with pip:

```python
pip install dull
```

Wrap a function with profiler:

```python
from dull import profile


@profile()
def foo():
    print("well hello")


print("hello there")
foo()
print("goodbye")
```

Output:

```bash
hello there
well hello
---------------------------------------profile foo---------------------------------------
         3 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 joku.py:4(foo)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


-----------------------------------------------------------------------------------------
goodbye
```

Dump profile to file:

```python
@profile(to_file=True)  # output defaults to profile/foo.dat
def foo():
    print("well hello")
```

Output:

```bash
hello there
well hello
--------------------------foo: profile saved to profile/foo.dat--------------------------
goodbye
```

Files are plain pstat dumps, get fancy with [snakeviz](https://github.com/jiffyclub/snakeviz) or similar visualizers:

```bash
snakeviz profile/foo.dat
```
