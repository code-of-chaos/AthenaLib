# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy
from dataclasses import dataclass
from typing import Any

# Custom Library

# Custom Packages
from AthenaLib.functions.string import enclose_double_quote
from AthenaLib.functions.type_check import type_check_error

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class HTMLElement:
    """
    A bare HTML element. This is a base class to be used to define already establish HTML elements or create a totally
    new named elements.

    Parameters:
    - name:str -> HTML element name, like "p"/ "span"/ ...
    - *wrap:list[HTMLElement|str|int|...] -> other objects the element wraps.
    - classes:list[str] -> a list of assigned CSS classes
    - id_str:str
    """
    name:str
    wraps:list[HTMLElement|str|int|...]

    # default attributes
    accesskey:str
    classes:list[str]
    contenteditable:str
    dir:str
    draggable:str
    hidden:str
    id:str
    style:str
    title:str

    def __init__(
            self,
            *wrap:Any,
            access_key:str=False,
            classes:list[str]=False,
            content_editable:str=False,
            direction:str=False,
            draggable:str=False,
            hidden:str=False,
            name:str,
            id_str:str=False,
            style:str=False,
            title:str=False
        ):
        self.name = type_check_error(name, str)
        self.wraps = list(wrap)

        # all below can have a truthy FALSE value
        self.accesskey = type_check_error(access_key, str) if access_key else False
        self.classes = type_check_error(classes, list) if classes else False
        self.contenteditable = type_check_error(content_editable, str) if content_editable else False
        self.dir = type_check_error(direction, str) if direction else False
        self.draggable = type_check_error(draggable, str) if draggable else False
        self.hidden = type_check_error(hidden, str) if hidden else False
        self.id = type_check_error(id_str, str) if id_str else False
        self.style = type_check_error(style, str) if style else False
        self.title = type_check_error(title, str) if title else False


    # ------------------------------------------------------------------------------------------------------------------
    # - Casting -
    # ------------------------------------------------------------------------------------------------------------------
    def _to_tag_generator(self) -> str:
        yield self.name # always yield an element name
        if self.classes:
            yield f"class={enclose_double_quote(' '.join(self.classes))}"

        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                yield f"{attr_name}={enclose_double_quote(attr_value)}"

    def to_tag(self) -> str:
        """Returns the start tag of the HTML element with all correctly defined attributes"""
        # because every element in segments is truthy, we can just skip False statements
        return f"<{' '.join(self._to_tag_generator())}>"

    def to_tag_end(self) -> str:
        """Returns the end tag of the HTML element"""
        return f"</{self.name}>"

    def to_dict(self) -> dict:
        """Returns a copy of the object's attributes"""
        return copy.copy(self.__dict__)

    def to_css_selector(self, full:bool=False) -> str:
        classes = f".{'.'.join(self.classes)}" if self.classes else ""
        id_str = f"#{self.id}" if self.id else ""

        attr: list[str] = []
        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                attr.append(f"{attr_name}={enclose_double_quote(attr_value)}")

        if not full or not attr:
            return f"{self.name}{classes}{id_str}"
        else:
            return f"{self.name}{classes}{id_str}[{','.join(attr)}]"

    def __str__(self):
        """Returns a completely wrapped html element, meaning it has with all the content within it, and it's end tag"""
        return f"{self.to_tag()}{' '.join(str(w) for w in self.wraps)}{self.to_tag_end()}"

# ----------------------------------------------------------------------------------------------------------------------
# - PREDEFINED HTML elements -
# ----------------------------------------------------------------------------------------------------------------------


@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class A(HTMLElement):
    name="a"
    href:str
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False, href:str=False):
        super(A, self).__init__(*wrap, name=A.name, classes=classes, id_str=id_str, style=style, title=title)
        self.href = type_check_error(href, str) if href else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Abbr(HTMLElement):
    name="abbr"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Abbr, self).__init__(*wrap, name=Abbr.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Acronym(HTMLElement):
    name="acronym"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Acronym, self).__init__(*wrap, name=Acronym.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Address(HTMLElement):
    name="address"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Address, self).__init__(*wrap, name=Address.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Applet(HTMLElement):
    name="applet"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Applet, self).__init__(*wrap, name=Applet.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Area(HTMLElement):
    name="area"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Area, self).__init__(*wrap, name=Area.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Article(HTMLElement):
    name="article"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Article, self).__init__(*wrap, name=Article.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Aside(HTMLElement):
    name="aside"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Aside, self).__init__(*wrap, name=Aside.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Audio(HTMLElement):
    name="audio"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Audio, self).__init__(*wrap, name=Audio.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class B(HTMLElement):
    name="b"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(B, self).__init__(*wrap, name=B.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Base(HTMLElement):
    name="base"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Base, self).__init__(*wrap, name=Base.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Basefont(HTMLElement):
    name="basefont"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Basefont, self).__init__(*wrap, name=Basefont.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Bdi(HTMLElement):
    name="bdi"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Bdi, self).__init__(*wrap, name=Bdi.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Bdo(HTMLElement):
    name="bdo"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Bdo, self).__init__(*wrap, name=Bdo.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Big(HTMLElement):
    name="big"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Big, self).__init__(*wrap, name=Big.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Blockquote(HTMLElement):
    name="blockquote"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Blockquote, self).__init__(*wrap, name=Blockquote.name, classes=classes, id_str=id_str, style=style,
                                         title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Body(HTMLElement):
    name="body"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Body, self).__init__(*wrap, name=Body.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Br(HTMLElement):
    name="br"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Br, self).__init__(*wrap, name=Br.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Button(HTMLElement):
    name="button"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Button, self).__init__(*wrap, name=Button.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Canvas(HTMLElement):
    name="canvas"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Canvas, self).__init__(*wrap, name=Canvas.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Caption(HTMLElement):
    name="caption"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Caption, self).__init__(*wrap, name=Caption.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Center(HTMLElement):
    name="center"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Center, self).__init__(*wrap, name=Center.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Cite(HTMLElement):
    name="cite"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Cite, self).__init__(*wrap, name=Cite.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Code(HTMLElement):
    name="code"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Code, self).__init__(*wrap, name=Code.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Col(HTMLElement):
    name="col"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Col, self).__init__(*wrap, name=Col.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Colgroup(HTMLElement):
    name="colgroup"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Colgroup, self).__init__(*wrap, name=Colgroup.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Data(HTMLElement):
    name="data"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Data, self).__init__(*wrap, name=Data.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Datalist(HTMLElement):
    name="datalist"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Datalist, self).__init__(*wrap, name=Datalist.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dd(HTMLElement):
    name="dd"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dd, self).__init__(*wrap, name=Dd.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Del(HTMLElement):
    name="del"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Del, self).__init__(*wrap, name=Del.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Details(HTMLElement):
    name="details"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Details, self).__init__(*wrap, name=Details.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dfn(HTMLElement):
    name="dfn"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dfn, self).__init__(*wrap, name=Dfn.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dialog(HTMLElement):
    name="dialog"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dialog, self).__init__(*wrap, name=Dialog.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dir(HTMLElement):
    name="dir"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dir, self).__init__(*wrap, name=Dir.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Div(HTMLElement):
    name="div"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Div, self).__init__(*wrap, name=Div.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dl(HTMLElement):
    name="dl"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dl, self).__init__(*wrap, name=Dl.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dt(HTMLElement):
    name="dt"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Dt, self).__init__(*wrap, name=Dt.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Em(HTMLElement):
    name="em"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Em, self).__init__(*wrap, name=Em.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Embed(HTMLElement):
    name="embed"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Embed, self).__init__(*wrap, name=Embed.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Fieldset(HTMLElement):
    name="fieldset"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Fieldset, self).__init__(*wrap, name=Fieldset.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Figcaption(HTMLElement):
    name="figcaption"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Figcaption, self).__init__(*wrap, name=Figcaption.name, classes=classes, id_str=id_str, style=style,
                                         title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Figure(HTMLElement):
    name="figure"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Figure, self).__init__(*wrap, name=Figure.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Font(HTMLElement):
    name="font"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Font, self).__init__(*wrap, name=Font.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Footer(HTMLElement):
    name="footer"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Footer, self).__init__(*wrap, name=Footer.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Form(HTMLElement):
    name="form"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Form, self).__init__(*wrap, name=Form.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Frame(HTMLElement):
    name="frame"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Frame, self).__init__(*wrap, name=Frame.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Frameset(HTMLElement):
    name="frameset"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Frameset, self).__init__(*wrap, name=Frameset.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H1(HTMLElement):
    name="h1"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H1, self).__init__(*wrap, name=H1.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H2(HTMLElement):
    name="h2"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H2, self).__init__(*wrap, name=H2.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H3(HTMLElement):
    name="h3"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H3, self).__init__(*wrap, name=H3.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H4(HTMLElement):
    name="h4"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H4, self).__init__(*wrap, name=H4.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H5(HTMLElement):
    name="h5"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H5, self).__init__(*wrap, name=H5.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H6(HTMLElement):
    name="h6"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(H6, self).__init__(*wrap, name=H6.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Head(HTMLElement):
    name="head"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Head, self).__init__(*wrap, name=Head.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Header(HTMLElement):
    name="header"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Header, self).__init__(*wrap, name=Header.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Hr(HTMLElement):
    name="hr"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Hr, self).__init__(*wrap, name=Hr.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Html(HTMLElement):
    name="html"
    lang:str
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False, lang:str=False):
        super(Html, self).__init__(*wrap, name=Html.name, classes=classes, id_str=id_str, style=style, title=title)
        self.lang = type_check_error(lang, str) if lang else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class I(HTMLElement):
    name="i"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(I, self).__init__(*wrap, name=I.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Iframe(HTMLElement):
    name="iframe"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Iframe, self).__init__(*wrap, name=Iframe.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Img(HTMLElement):
    name="img"
    src:str
    width:str|int
    height:str|int
    alt:str
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False, src:str=False,
                 width:str|int=False, height:str|int=False, alt:str=False):
        super(Img, self).__init__(*wrap, name=Img.name, classes=classes, id_str=id_str, style=style, title=title)
        self.src = type_check_error(src, str) if src else False
        self.width = type_check_error(width, str|int) if width else False
        self.height = type_check_error(height, str|int) if height else False
        self.alt = type_check_error(alt, str) if alt else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Input(HTMLElement):
    name="input"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Input, self).__init__(*wrap, name=Input.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ins(HTMLElement):
    name="ins"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Ins, self).__init__(*wrap, name=Ins.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Kbd(HTMLElement):
    name="kbd"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Kbd, self).__init__(*wrap, name=Kbd.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Label(HTMLElement):
    name="label"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Label, self).__init__(*wrap, name=Label.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Legend(HTMLElement):
    name="legend"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Legend, self).__init__(*wrap, name=Legend.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Li(HTMLElement):
    name="li"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Li, self).__init__(*wrap, name=Li.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Link(HTMLElement):
    name="link"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Link, self).__init__(*wrap, name=Link.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Main(HTMLElement):
    name="main"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Main, self).__init__(*wrap, name=Main.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Map(HTMLElement):
    name="map"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Map, self).__init__(*wrap, name=Map.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Mark(HTMLElement):
    name="mark"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Mark, self).__init__(*wrap, name=Mark.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Meta(HTMLElement):
    name="meta"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Meta, self).__init__(*wrap, name=Meta.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Meter(HTMLElement):
    name="meter"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Meter, self).__init__(*wrap, name=Meter.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Nav(HTMLElement):
    name="nav"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Nav, self).__init__(*wrap, name=Nav.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Noframes(HTMLElement):
    name="noframes"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Noframes, self).__init__(*wrap, name=Noframes.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Noscript(HTMLElement):
    name="noscript"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Noscript, self).__init__(*wrap, name=Noscript.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Object(HTMLElement):
    name="object"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Object, self).__init__(*wrap, name=Object.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ol(HTMLElement):
    name="ol"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Ol, self).__init__(*wrap, name=Ol.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Optgroup(HTMLElement):
    name="optgroup"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Optgroup, self).__init__(*wrap, name=Optgroup.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Option(HTMLElement):
    name="option"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Option, self).__init__(*wrap, name=Option.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Output(HTMLElement):
    name="output"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Output, self).__init__(*wrap, name=Output.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class P(HTMLElement):
    name="p"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(P, self).__init__(*wrap, name=P.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Param(HTMLElement):
    name="param"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Param, self).__init__(*wrap, name=Param.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Picture(HTMLElement):
    name="picture"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Picture, self).__init__(*wrap, name=Picture.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Pre(HTMLElement):
    name="pre"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Pre, self).__init__(*wrap, name=Pre.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Progress(HTMLElement):
    name="progress"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Progress, self).__init__(*wrap, name=Progress.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Q(HTMLElement):
    name="q"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Q, self).__init__(*wrap, name=Q.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Rp(HTMLElement):
    name="rp"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Rp, self).__init__(*wrap, name=Rp.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Rt(HTMLElement):
    name="rt"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Rt, self).__init__(*wrap, name=Rt.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ruby(HTMLElement):
    name="ruby"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Ruby, self).__init__(*wrap, name=Ruby.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class S(HTMLElement):
    name="s"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(S, self).__init__(*wrap, name=S.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Samp(HTMLElement):
    name="samp"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Samp, self).__init__(*wrap, name=Samp.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Script(HTMLElement):
    name="script"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Script, self).__init__(*wrap, name=Script.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Section(HTMLElement):
    name="section"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Section, self).__init__(*wrap, name=Section.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Select(HTMLElement):
    name="select"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Select, self).__init__(*wrap, name=Select.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Small(HTMLElement):
    name="small"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Small, self).__init__(*wrap, name=Small.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Source(HTMLElement):
    name="source"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Source, self).__init__(*wrap, name=Source.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Span(HTMLElement):
    name="span"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Span, self).__init__(*wrap, name=Span.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Strike(HTMLElement):
    name="strike"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Strike, self).__init__(*wrap, name=Strike.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Strong(HTMLElement):
    name="strong"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Strong, self).__init__(*wrap, name=Strong.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Style(HTMLElement):
    name="style"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Style, self).__init__(*wrap, name=Style.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Sub(HTMLElement):
    name="sub"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Sub, self).__init__(*wrap, name=Sub.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Summary(HTMLElement):
    name="summary"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Summary, self).__init__(*wrap, name=Summary.name, classes=classes, id_str=id_str, style=style,
                                      title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Sup(HTMLElement):
    name="sup"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Sup, self).__init__(*wrap, name=Sup.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Svg(HTMLElement):
    name="svg"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Svg, self).__init__(*wrap, name=Svg.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Table(HTMLElement):
    name="table"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Table, self).__init__(*wrap, name=Table.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tbody(HTMLElement):
    name="tbody"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Tbody, self).__init__(*wrap, name=Tbody.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Td(HTMLElement):
    name="td"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Td, self).__init__(*wrap, name=Td.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Template(HTMLElement):
    name="template"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Template, self).__init__(*wrap, name=Template.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Textarea(HTMLElement):
    name="textarea"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Textarea, self).__init__(*wrap, name=Textarea.name, classes=classes, id_str=id_str, style=style,
                                       title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tfoot(HTMLElement):
    name="tfoot"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Tfoot, self).__init__(*wrap, name=Tfoot.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Th(HTMLElement):
    name="th"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Th, self).__init__(*wrap, name=Th.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Thead(HTMLElement):
    name="thead"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Thead, self).__init__(*wrap, name=Thead.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Time(HTMLElement):
    name="time"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Time, self).__init__(*wrap, name=Time.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Title(HTMLElement):
    name="title"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Title, self).__init__(*wrap, name=Title.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tr(HTMLElement):
    name="tr"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Tr, self).__init__(*wrap, name=Tr.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Track(HTMLElement):
    name="track"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Track, self).__init__(*wrap, name=Track.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tt(HTMLElement):
    name="tt"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Tt, self).__init__(*wrap, name=Tt.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class U(HTMLElement):
    name="u"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(U, self).__init__(*wrap, name=U.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ul(HTMLElement):
    name="ul"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Ul, self).__init__(*wrap, name=Ul.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Var(HTMLElement):
    name="var"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Var, self).__init__(*wrap, name=Var.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Video(HTMLElement):
    name="video"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Video, self).__init__(*wrap, name=Video.name, classes=classes, id_str=id_str, style=style, title=title)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Wbr(HTMLElement):
    name="wbr"
    def __init__(self,*wrap:Any,classes:list[str]=False,id_str:str=False,style:str=False,title:str=False):
        super(Wbr, self).__init__(*wrap, name=Wbr.name, classes=classes, id_str=id_str, style=style, title=title)