import argparse

parser = argparse.ArgumentParser(prog='git')
parser.add_argument('number1',type=int)
parser.add_argument('number2',type=int)
parser.add_argument('-x','--exclusive',action='store_true')
parser.add_argument('--steps',type=int,default=1)

args = parser.parse_args()

if args.exclusive:
    [print(i) for i in range(args.number1, args.number2,args.steps)]
else:
    [print(i) for i in range(args.number1, args.number2+1,args.steps)]





