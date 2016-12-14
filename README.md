# gdt-static
The static version of official website for Galaxy Dragon Travel Pty Ltd.

Previously http://www.igalaxydragon.com was developed using Python/Django. Later
on the dynamic part has been isolated into another independent website
http://www.bendiyou.com, which keeps using Python/Django.

In order to improve speed and efficiency, the static part is rewritten directly
using HTML/CSS/Javascript and Bootstrap framework.

However, Django template language is used to develop these static pages. It solves
the "include" problem: it is difficult to DIRECTLY include a HTML file into
another HTML file. Compared to PHP include method, the inheritance and block
override from Django template language make this method very flexible.

All of template files are inside the src/templates directory. The Python script
gen.py is used to generate the final static pages. To use this python script, you
need install Django first:

$ python3 -m pip install django

Once the Django is installed properly, run gen.py to generate the HTML file:

$ python3 gen.py src/templates/index_t.html > src/index.html
