# task3 artifacts

**Пример 1 без файла-аргумента**

```commandline
    $ python3 HomeWork1/task3/task3.py 
abc
abc
      2       2      8
```

```commandline
    $ wc
abc
abc
      2       2       8
```

**Пример 2 без файла-аргумента**

```commandline
    $ python3 HomeWork1/task3/task3.py
abc
abc      1       2      7
```

```commandline
    $ wc
abc
abc      1       2       7
```

**Пример 3 с несуществуюзим файлом**

```commandline
    $ python3 HomeWork1/task3/task3.py not_exists.txt
Could not open/read file: not_exists.txt
```

**Пример 4 с пустым файлом**

```commandline
    $ python3 HomeWork1/task3/task3.py HomeWork1/task3/test_files/empty.txt
1 0 1 HomeWork1/task3/test_files/empty.txt
```

```commandline
    $ wc HomeWork1/task3/test_files/empty.txt 
1 0 1 HomeWork1/task3/test_files/empty.txt
```

**Пример 5 с одним файлом-аргументом**

```commandline
    $ python3 HomeWork1/task3/task3.py HomeWork1/task3/test_files/test1.txt 
 11 52 305 HomeWork1/task3/test_files/test1.txt
```

```commandline
    $ wc  HomeWork1/task3/test_files/test1.txt 
 11  52 305 HomeWork1/task3/test_files/test1.txt
```

**Пример 6  с нексколькими файлами-аргументами**

```commandline
    $ python3 HomeWork1/task3/task3.py HomeWork1/task3/test_files/test1.txt HomeWork1/task3/test_files/test2.txt 
 11 52 305 HomeWork1/task3/test_files/test1.txt
 6 41 237 HomeWork1/task3/test_files/test2.txt
 17 93 542 total
```

```commandline
    $ wc  HomeWork1/task3/test_files/test1.txt HomeWork1/task3/test_files/test2.txt 
 11  52 305 HomeWork1/task3/test_files/test1.txt
  6  41 237 HomeWork1/task3/test_files/test2.txt
 17  93 542 итого
```