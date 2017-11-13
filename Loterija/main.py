#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        besedilo = "Ali zelis generirati 8 nakljucnih loto stevilk?"
        params = {"text":besedilo}
        return self.render_template("hello.html", params = params)
def loto(st):
    sez=[]
    st = range(st)
    x=0
    while x in st:
        y=random.randint(1, 39)
        if y not in sez:
            sez.append(y)
            x+=1
        else:
            continue
    return sez







class LotoHandler(BaseHandler):
    def get(self):
        tekst="Program bo nakljucno generiral in izpisal 8 Loto stevilk."


        seznam=loto(8)


        params={"besed":tekst, "izpis":seznam}
        return self.render_template("loto.html", params=params)




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', LotoHandler),
], debug=True)
