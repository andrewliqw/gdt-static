import argparse
import os
import sys
from django.template import Engine, Context

description = """
Generate the final webpage from the Django template files.

It accept one or more template files, and output to final HTML files. The
default output directory is "dist". The output HTML filename is the same to
template filename. If the output file already exists in the output directory,
the program exits with an error.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument(
    "filename",
    nargs="+",
    help="specify the webpage name e.g.: index.html"
)

parser.add_argument(
    "-t",
    "--template-dir",
    help="specify the directory of template files"
)

parser.add_argument(
    "-d",
    "--out-directory",
    help="specify the output direcotry, default is dist"
)

args = parser.parse_args()
#print(args)

# if not args.filename:
#     sys.exit(0)

top_dir = os.path.dirname(os.path.abspath(__file__))
# print(top_dir)
# sys.exit(0)

if not args.template_dir:
    args.template_dir = "src/templates"
args.template_dir = os.path.join(top_dir, args.template_dir)

if not args.out_directory:
    args.out_directory = "dist"
args.out_directory = os.path.join(top_dir, args.out_directory)
if not os.path.exists(args.out_directory):
    raise FileExistsError("output directory " + args.out_directory + " not exist")

django_engine = Engine(
    dirs = [args.template_dir],
)

for filename in args.filename:
    infile = os.path.join(args.template_dir, filename)
    if not os.path.exists(infile):
        raise FileNotFoundError(infile + " not found")

    outfile = os.path.join(args.out_directory, filename)
    if os.path.exists(outfile):
        raise FileExistsError(outfile + " already exists in " + args.directory)

    with open(outfile, "w") as f:
        print(django_engine.get_template("index.html").render(Context()), file=f)
