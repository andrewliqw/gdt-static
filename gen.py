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

args = parser.parse_args()

args.template_file = os.path.abspath(args.template_file)

django_engine = Engine(
    dirs = ['/'],
)

context = Context({
    "STATIC_URL": os.path.join("./static", ""),
    "CURRENT_FILE": os.path.basename(args.template_file),
})
print(django_engine.get_template(args.template_file).render(context))