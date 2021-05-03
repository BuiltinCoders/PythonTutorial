import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "something went wrong!"

if __name__=='__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default=1.0, help="Give a float value for x variable.")

    parser.add_argument('--y', type=float, default=1.0, help="Give a float value for y variable.")

    parser.add_argument('--o', type=str, default="add", help="Write a operation performed on the two given variables.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))