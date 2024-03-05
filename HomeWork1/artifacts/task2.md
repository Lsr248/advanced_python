# task2 artifacts

**Пример 1 без файла с 20 строками**

```commandline
$ python3 HomeWork1/task2/task2.py
1 
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
18
20
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
18
20
```

**Пример 2 с 4 строками**

```commandline
$ python3 HomeWork1/task2/task2.py
1
2
3
4
1
2
3
4
```

** Пример 3 с несуществующим файлом**

```commandline
$ python3 HomeWork1/task2/task2.py not_exists.txt
Could not open/read file: not_exists.txt
```

** Пример 4 с пустым файлом**

```commandline
$ python3 HomeWork1/task2/task2.py HomeWork1/task2/test_files/empty.txt 


```

** Пример 4 с одним файлом-аргументом**

```commandline
    $  python3 HomeWork1/task2/task2.py HomeWork1/task2/test_files/test1.txt 
3 Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
4
5 Aenean commodo ligula eget dolor. Aenean massa.
6
7 Apple sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
8
9 Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
10
11
12
```
** Пример 5 с несколькими файлами-аргументами**

```commandline
    $ python3 HomeWork1/task2/task2.py HomeWork1/task2/test_files/test1.txt HomeWork1/task2/test_files/test2.txt 
==> HomeWork1/task2/test_files/test1.txt <==
3 Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
4
5 Aenean commodo ligula eget dolor. Aenean massa.
6
7 Apple sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
8
9 Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
10
11
12
==> HomeWork1/task2/test_files/test2.txt <==
1 some duumy text
2 Nulla consequat massa quis enim.
3 Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.
4 In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.
5 Nullam dictum felis eu pede mollis pretium.
6
```

```commandline
    $ python3 HomeWork1/task2/task2.py HomeWork1/task2/test_files/test1.txt not_exists.txt HomeWork1/task2/test_files/test2.txt 
==> HomeWork1/task2/test_files/test1.txt <==
3 Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
4
5 Aenean commodo ligula eget dolor. Aenean massa.
6
7 Apple sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
8
9 Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
10
11
12
Could not open/read file: not_exists.txt
```