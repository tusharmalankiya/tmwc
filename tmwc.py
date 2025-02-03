import argparse
import sys

def main():
    parser = argparse.ArgumentParser(prog='tmwc', description='The clone of linux command line tool WC')

    parser.add_argument('filename', nargs='?', help='Name of the file')
    parser.add_argument('-c', '--bytes', help='print the number of bytes', action='store_true')
    parser.add_argument('-l', '--lines', help='print the number of lines', action='store_true')
    parser.add_argument('-w', '--words', help='print the number of words', action='store_true')
    parser.add_argument('-m', '--chars', help='print the number of characters', action='store_true')

    args = parser.parse_args()
    
    if args.filename:
        filename = args.filename
        with open(filename, 'rb') as f:
            text = f.read()
        text = text.decode('utf-8')
    else:
        text = sys.stdin.read()

    if args.bytes:
        total_bytes = count_bytes(text)
        print(f'''{total_bytes} {filename if args.filename else ''}''')
    elif args.lines:
        lines = count_lines(text)
        print(f'''{lines} {filename if args.filename else ''}''')
    elif args.words:
        words = count_words(text)
        print(f'''{words} {filename if args.filename else ''}''')
    elif args.chars:
        chars = count_chars(text)
        print(f'''{chars} {filename if args.filename else ''}''')
    else:
        total_bytes = count_bytes(text)
        lines = count_lines(text)
        words = count_words(text)
        print(f'''  {lines}  {words}  {total_bytes}  {filename if args.filename else ''}''')


def count_bytes(text):
    return len(text.encode('utf-8'))

def count_lines(text):
    l_count = 0
    for _ in text:
        if _ == '\n':
            l_count += 1
    return l_count

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

if __name__ == "__main__":
    main()
