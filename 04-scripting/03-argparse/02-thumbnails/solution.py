from pathlib import Path
import os, sys
from PIL import Image
import argparse
import re



def parse_size(string):
    match = re.fullmatch(r'(\d+)x(\d+)', string)

    if not match:
        print('Invalid size --- should have format WxH')
        sys.exit(-1)

    width, height = match.groups()

    return (int(width), int(height))


def derive_output_filename(pattern, input_file):
    path = Path(input_file)
    basename = path.stem
    extension = path.suffix
    return pattern.replace('%b', basename).replace('.%x', extension)


parser = argparse.ArgumentParser(prog='thumbnail')
parser.add_argument('files', help='Files', nargs='+')
parser.add_argument('--size', help='Size of the thumbnail', default='64x64')
parser.add_argument('--pattern', help='Pattern for output files', default='%b-thumbnail.%x')

args = parser.parse_args()

size = parse_size(args.size)
input_files = args.files
pattern = args.pattern


for input_file in input_files:
    output_file = derive_output_filename(pattern, input_file)

    image = Image.open(input_file)
    image.thumbnail(size)
    image.save(output_file)
