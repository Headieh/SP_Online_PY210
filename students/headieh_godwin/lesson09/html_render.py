#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def open_tag(self, cur_ind=''):
        open_tag = [f'{cur_ind}{self.indent}<{self.tag}']

        for keys, values in self.attributes.items():
            open_tag.append(' {}="{}"'.format(keys, values))
        open_tag.append(">")
        return("".join(open_tag))

    def close_tag(self, cur_ind=''):
        return f'{cur_ind}{self.indent}</{self.tag}>'

    #def render(self, out_file):
    def render(self, out_file, cur_ind=""):
        out_file.write(self.open_tag(cur_ind))
        out_file.write("\n")
        for content in self.contents:
            if isinstance(content, Element):# string element
                content.render(out_file, cur_ind + self.indent)
            elif isinstance(content, str):
                out_file.write(f'{cur_ind}{self.indent*2}{content}')
                out_file.write("\n")
            else:# unknown objects
                raise(AttributeError, "Unknown object.")
        out_file.write(self.close_tag(cur_ind))
        out_file.write("\n")


class Html(Element):
    tag = "html"
    indent = ""

    def render(self, out_file, cur_ind=''):
        out_file.write(f'<!DOCTYPE html>\n')
        super().render(out_file, cur_ind + self.indent)

class OneLineTag(Element):
    tag = 'title'

    def render(self, out_file, cur_ind=""):
        out_file.write(self.open_tag(cur_ind))
        if isinstance(self.contents[0], str):
            out_file.write(f'{self.contents[0]}</{self.tag}>\n')
        else:
            print(f"content:{self.contents}")
            raise AttributeError("OneLineTag doesn't allow Object decalration")

    def append(self, new_content):
        if len(self.contents) == 0:
            self.contents.append(new_content)
        else:
            raise AttributeError("OneLineTag only has one content.")

class SelfClosingTag(Element):
    tag = 'hr'

    def __init__(self, content=None, **kwargs):
        if content is None:
            super().__init__(**kwargs)
        else:
            raise TypeError('Cannot append content to SelfClosingTag')

    def render(self, out_file, cur_ind=''):
        out_file.write(f'{self.open_tag(cur_ind)[:-1]} />\n')


class A(Element):
    tag = "a"

    def __init__(self, link=None, content=None, **kwargs):
        if link is None:
            self.link = '#'
        else:
            self.link = link
        if content is None:
            self.content = ['reload']
        else:
            self.content = [content]
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=''):
        out_file.write(f'{cur_ind}{self.indent}<{self.tag} \
href="{self.link}">{self.contents[0]}</a>\n')

class H(OneLineTag):
    tag = 'h'

    def __init__(self, level=-1, content=None, **kwargs):
        if level == -1:
            raise (AttributeError, "H tag needs an integer for header level.")
        else:
            if str(level).isdigit():
                self.tag = f'{self.tag}{level}'
            else:
                raise (ValueError, "H tag needs an integer for header level.")
        super().__init__(content, **kwargs)

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = 'title'

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class Meta(SelfClosingTag):
    tag = "meta"

class Table(Element):
    tag = "table"

class Tr(Element):
    tag = "tr"

class Th(OneLineTag):
    tag = "th"

class Td(OneLineTag):
    tag = "td"

class Style(Element):
    tag = "style"

class Customer(OneLineTag):
    tag = ''

    def render(self, out_file, cur_ind=''):
        out_file.write(f'{cur_ind}{self.indent}{self.contents[0]}\n')
