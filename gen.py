import argparse
import os
import sys
from django.template import Engine, Context

description = """
Generate the final webpage from the Django template files.
"""

"""
It accept one or more template files, and output to final HTML files. The
default output directory is "dist". The output HTML filename is the same to
template filename. If the output file already exists in the output directory,
the program exits with an error.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument(
    "template_file",
    # nargs="+",
    help="specify the template filename e.g.: index_t.html"
)

# parser.add_argument(
#     "-s",
#     "--static-dir",
#     default="src/static",
#     help="specify the directory of static files"
# )

# parser.add_argument(
#     "-t",
#     "--template-dir",
#     default="src/templates",
#     help="specify the directory of template files"
# )

# parser.add_argument(
#     "-d",
#     "--out-directory",
#     default="dist",
#     help="specify the output direcotry, default is dist"
# )

args = parser.parse_args()

# top_dir = os.path.dirname(os.path.abspath(__file__))

# args.template_dir = os.path.join(top_dir, args.template_dir)
# args.out_directory = os.path.join(top_dir, args.out_directory)
# args.static_dir = os.path.join("..", args.static_dir, "")

# if not os.path.exists(args.out_directory):
#     raise FileExistsError("output directory " + args.out_directory + " not exist")

django_engine = Engine(
    dirs = ['/'],
    # dirs = [args.template_dir],
    # libraries = {
    #     "staticfiles": "django.contrib.staticfiles.templatetags.staticfiles",
    # }
)

# context = Context({"STATIC_URL": args.static_dir})
# for filename in args.filename:
#     infile = os.path.join(args.template_dir, filename)
#     if not os.path.exists(infile):
#         raise FileNotFoundError(infile + " not found")

#     outfile = os.path.join(args.out_directory, filename)
#     if os.path.exists(outfile):
#         raise FileExistsError(outfile + " already exists in " + args.out_directory)

#     with open(outfile, "w") as f:
#         print(django_engine.get_template("index.html").render(context), file=f)

args.template_file = os.path.abspath(args.template_file)
context = Context({"STATIC_URL": os.path.join("./static", "")})
print(django_engine.get_template(args.template_file).render(context))