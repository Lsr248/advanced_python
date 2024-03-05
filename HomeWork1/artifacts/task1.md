# task1 artifacts

**Пример 1 без файла-аргумента**

```commandline
$ python3 HomeWork1/task1/task1.py
123 
        1 123
1234
        2 1234
13345
        3 13345
123456
        4 123456
line with spaces
        5 line with spaces
```

**Пример 2 для несуществующего файла**

```commandline
$ python3 HomeWork1/task1/task1.py not_exists.txt
Could not open/read file: not_exists.txt
```

**Пример 3 с пустым файлом**

```commandline
$ python3 HomeWork1/task1/task1.py HomeWork1/task1/test_files/empty.txt 


```

**Пример 4 с одним файлом-аргументом**

```commandline
    $ python3 HomeWork1/task1/task1.py HomeWork1/task1/test_files/test1.txt 
        1 1 some dummy text
        2 2
        3 3 Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        4 4
        5 5 Aenean commodo ligula eget dolor. Aenean massa.
        6 6
        7 7 Apple sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        8 8
        9 9 Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
        10 10
        11 11
        12 12
```