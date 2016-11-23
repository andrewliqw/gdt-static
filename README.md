# gdt-static
The static version of official website for Galaxy Dragon Travel Pty Ltd.

Previously http://www.igalaxydragon.com was developed using Python/Django. Later
on the dynamic part has been isolated into another independent website
http://www.bendiyou.com, which keeps using Python/Django.

In order to improve speed and efficiency, the static part is rewritten directly
using HTML/CSS/Javascript and Bootstrap framework.

However, Django template language is used to develop the static pages. It solves
the "include" problem: it is difficult to DIRECTLY include a HTML file into
another HTML file.

All of template files are inside the src/templates directory. The Python script
gen.py is used to generate the final static pages and put them inside dist
directory.
