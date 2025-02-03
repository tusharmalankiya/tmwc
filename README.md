# TMWC
This is a Python-based clone of the Unix `wc` (word count) command-line tool. It counts the number of lines, words, characters, and bytes in a file or from input passed via standard input (stdin). The tool supports multiple options and is designed to behave similarly to the original `wc` command.

## Features

- Count the number of **lines**, **words**, **characters**, and **bytes**.
- Supports reading from both a file and stdin (piped input).
- Flexible with multiple options that can be used together.

## Usage
The tool supports the following options:

```bash
usage: wc-tool.py [-h] [--bytes] [--lines] [--words] [--chars] [filename]
```

### Options:
#### -h, --help: 
Show help message and exit.

```bash
    python3 tmwc.py -h
```

#### -c, --bytes: 
Print the number of bytes.

```bash
    python3 tmwc.py -c <filename>
```

#### -l, --lines: 
Print the number of lines.

```bash 
    python3 tmwc.py -l <filename>
```

#### -w, --words: 
Print the number of words.

```bash 
    python3 tmwc.py -w <filename>
```

#### -m, --chars: 
Print the number of characters.

```bash 
    python3 tmwc.py -m <filename>
```

#### filename: 
The file to count. If no filename is provided, the tool reads from stdin.

```bash 
    cat <filename> | python3 tmwc.py -l
```
