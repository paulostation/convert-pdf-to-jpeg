from pdf2image import convert_from_path

import argparse

parser = argparse.ArgumentParser(description='Read a PDF file and store all pages in JPEG format.')

parser.add_argument("input_file", type=str, 
                   help='Source file with pdf content')

args = parser.parse_args()

INPUT_FILE = args.input_file

pages = convert_from_path(INPUT_FILE, 500)

for index,page in enumerate(pages):
    page.save('{0}_{1}.jpg'.format(INPUT_FILE[:-4], index), 'JPEG')