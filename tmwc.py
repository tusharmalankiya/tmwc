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

    empty_args = True
    for key, value in vars(args).items():
        if key != "filename" and value is True:
            empty_args = False
            break

    if args.filename:
        filename = args.filename
        with open(filename, 'rb') as f:
            text = f.read()
        text = text.decode('utf-8')
    else:
        text = sys.stdin.read()

    if args.bytes:
        total_bytes = count_bytes(text)
    if args.lines:
        lines = count_lines(text)
    if args.words:
        words = count_words(text)
    if args.chars:
        chars = count_chars(text)
    if empty_args:
        total_bytes = count_bytes(text)
        lines = count_lines(text)
        words = count_words(text)
        print(f'''  {lines}  {words}  {total_bytes}  {filename if args.filename else ''}''')
        return

    print(f'''{lines if args.lines else ''}  {words if args.words else ''}  {chars if args.chars else ''}  {total_bytes if args.bytes else '' }  {filename if args.filename else ''}''')


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
