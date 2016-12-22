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
    "static_level",
    type=int,
    help="level of static directory relative to template file"
)

args = parser.parse_args()

if args.static_level == 0:
    static_url = "."
elif args.static_level > 0:
    static_url = "../" * args.static_level
else:
    raise ValueError("level should be >=0")

args.template_file = os.path.abspath(args.template_file)

django_engine = Engine(
    dirs = ['/'],
)

context = Context({
    "STATIC_URL": os.path.join(static_url, "static", ""),
    # CURRENT_FILE used for navbar
    "CURRENT_FILE": os.path.basename(args.template_file),
})
print(django_engine.get_template(args.template_file).render(context))