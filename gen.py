import argparse
import os
import sys
from django.template import Engine, Context

description = """
Generate the final webpage from the Django template files.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument(
    "template_file",
    help="specify the template filename e.g.: index_t.html"
)

parser.add_argument(
    "relative_level",
    type=int,
    help="level of current template file relative to index page"
)

args = parser.parse_args()

if args.relative_level == 0:
    relative_url = "."
elif args.relative_level > 0:
    relative_url = "../" * args.relative_level
else:
    raise ValueError("level should be >=0")

args.template_file = os.path.abspath(args.template_file)

django_engine = Engine(
    dirs = ['/'],
)

context = Context({
    "RELATIVE_URL": os.path.join(relative_url, ""),
    "STATIC_URL": os.path.join(relative_url, "static", ""),
    # CURRENT_FILE used for navbar
    "CURRENT_FILE": os.path.basename(args.template_file),
})
print(django_engine.get_template(args.template_file).render(context))