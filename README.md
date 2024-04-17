# weasyprint memory check

## Overview (English)

- This repository checks the memory usage when converting HTML containing multibyte characters to PDF using [weasyprint](https://github.com/Kozea/WeasyPrint) .
- For measuring memory, we use [memory_profiler](https://github.com/pythonprofilers/memory_profiler).

## Overview( Japanese )

- このリポジトリは [weasyprint](https://github.com/Kozea/WeasyPrint) を使用してマルチバイトの文字列を含む HTML を PDF に変換した際のメモリ使用量を確認するリポジトリです
- メモリ計測のため [memory_profiler](https://github.com/pythonprofilers/memory_profiler) を使用しています

## Usage

### Setup

Replace `<full-path-to-your-local-directory>` with the full path to the directory where you want to mount the volume inside the container.

```
git clone git@github.com:yamap55/weasyprint_memory_check.git
docker build -t weasyprint_memory_check .
docker run -v <full-path-to-your-local-directory>:/app -it weasyprint_memory_check /bin/bash
```

### Execute

```
python main.py
```

## Output

```
root@da77985c9dc8:/app# python main.py
start.
finished. 1.2 seconds
start.
finished. 0.3 seconds
start.
finished. 0.3 seconds
start.
finished. 0.3 seconds
start.
finished. 0.3 seconds
Filename: /app/main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     44.5 MiB     44.5 MiB           1   @profile()
     7                                         def create_pdf(file_path: str):
     8     51.7 MiB      7.2 MiB           1       generate(file_path)
     9     52.8 MiB      1.1 MiB           1       generate(file_path)
    10     54.2 MiB      1.4 MiB           1       generate(file_path)
    11     55.3 MiB      1.1 MiB           1       generate(file_path)
    12     56.4 MiB      1.1 MiB           1       generate(file_path)
    13     56.4 MiB      0.0 MiB           1       return True


start.
finished. 5.0 seconds
start.
finished. 4.9 seconds
start.
finished. 5.0 seconds
start.
finished. 5.0 seconds
start.
finished. 5.0 seconds
Filename: /app/main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     56.4 MiB     56.4 MiB           1   @profile()
     7                                         def create_pdf(file_path: str):
     8    117.9 MiB     61.5 MiB           1       generate(file_path)
     9    182.9 MiB     65.0 MiB           1       generate(file_path)
    10    200.0 MiB     17.1 MiB           1       generate(file_path)
    11    236.8 MiB     36.8 MiB           1       generate(file_path)
    12    272.8 MiB     36.0 MiB           1       generate(file_path)
    13    272.8 MiB      0.0 MiB           1       return True
```
