# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages
from AthenaLib.HTML.models.html import HTMLElement
from AthenaLib.functions.type_check import type_check_error
from AthenaLib.functions.string import enclose_double_quote
from AthenaLib.decorators.dataclass import dataclass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Comment(HTMLElement):
    def __init__(self, *wraps, **kwargs):
        super(Comment, self).__init__(*wraps,name="COMMENT",**kwargs)

    def to_tag(self) -> str:
        return f"<!--"

    def to_tag_end(self) -> str:
        return f"<-->"

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class A(HTMLElement):
    name="a"
    download:str
    href:str
    hreflang:str
    media:str
    ping:str
    referrerpolicy:str
    rel:str
    target:str
    type:str

    def __init__(self, *wraps,
                 download:str,
                 href:str,
                 hreflang:str,
                 media:str,
                 ping:str,
                 referrer_policy:str,
                 rel:str,
                 target:str,
                 type_str:str,
                 **kwargs):
        super(A, self).__init__(*wraps,name=A.name,**kwargs)
        self.download:str = type_check_error(download, str) if download else False
        self.href:str = type_check_error(href, str) if href else False
        self.hreflang:str = type_check_error(hreflang, str) if hreflang else False
        self.media:str = type_check_error(media, str) if media else False
        self.ping:str = type_check_error(ping, str) if ping else False
        self.referrerpolicy:str = type_check_error(referrer_policy, str) if referrer_policy else False
        self.rel:str = type_check_error(rel, str) if rel else False
        self.target:str = type_check_error(target, str) if target else False
        self.type:str = type_check_error(type_str, str) if type_str else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Abbr(HTMLElement):
    name="abbr"

    def __init__(self, *wraps, **kwargs):
        super(Abbr, self).__init__(*wraps,name=Abbr.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Address(HTMLElement):
    name="address"

    def __init__(self, *wraps, **kwargs):
        super(Address, self).__init__(*wraps,name=Address.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Area(HTMLElement):
    name="area"

    def __init__(self, *wraps, **kwargs):
        super(Area, self).__init__(*wraps,name=Area.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Article(HTMLElement):
    name="article"

    def __init__(self, *wraps, **kwargs):
        super(Article, self).__init__(*wraps,name=Article.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Aside(HTMLElement):
    name="aside"

    def __init__(self, *wraps, **kwargs):
        super(Aside, self).__init__(*wraps,name=Aside.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Audio(HTMLElement):
    name="audio"

    def __init__(self, *wraps, **kwargs):
        super(Audio, self).__init__(*wraps,name=Audio.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class B(HTMLElement):
    name="b"

    def __init__(self, *wraps, **kwargs):
        super(B, self).__init__(*wraps,name=B.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Base(HTMLElement):
    name="base"
    href: str
    target: str

    def __init__(self, *wraps,
                 href: str,
                 target: str,
                 **kwargs):
        super(Base, self).__init__(*wraps, name=Base.name, **kwargs)
        self.href: str = type_check_error(href, str) if href else False
        self.target: str = type_check_error(target, str) if target else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Basefont(HTMLElement):
    name="basefont"

    def __init__(self, *wraps, **kwargs):
        super(Basefont).__init__(*wraps,name=Basefont.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Bdi(HTMLElement):
    name="bdi"

    def __init__(self, *wraps, **kwargs):
        super(Bdi, self).__init__(*wraps,name=Bdi.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Bdo(HTMLElement):
    name="bdo"

    def __init__(self, *wraps, **kwargs):
        super(Bdo, self).__init__(*wraps,name=Bdo.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Blockquote(HTMLElement):
    name="blockquote"
    cite: str

    def __init__(self, *wraps,
                 cite: str,
                 target: str,
                 **kwargs):
        super(Blockquote, self).__init__(*wraps, name=Blockquote.name, **kwargs)
        self.cite: str = type_check_error(cite, str) if cite else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Body(HTMLElement):
    name="body"

    def __init__(self, *wraps, **kwargs):
        super(Body, self).__init__(*wraps,name=Body.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Br(HTMLElement):
    name="br"

    def __init__(self, *wraps, **kwargs):
        super(Br, self).__init__(*wraps,name=Br.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Button(HTMLElement):
    name="button"
    autofocus:str
    disabled:str
    form:str
    formaction:str
    formenctype:str
    formmethod:str
    fromnovalidate:str
    formtarget:str
    name_button:str
    type:str
    value:str

    def __init__(self,
                 *wraps,
                 autofocus:str=False,
                 disabled:str=False,
                 form:str=False,
                 form_action:str=False,
                 form_enc_type:str=False,
                 form_method:str=False,
                 from_no_validate:str=False,
                 form_target:str=False,
                 name_button:str=False,
                 type:str=False,
                 value:str=False,
                 **kwargs):
        super(Button, self).__init__(*wraps,name=Button.name,**kwargs)
        self.autofocus = type_check_error(autofocus, str) if autofocus else False
        self.disabled = type_check_error(disabled, str) if disabled else False
        self.form = type_check_error(form, str) if form else False
        self.formaction = type_check_error(form_action, str) if form_action else False
        self.formenctype = type_check_error(form_enc_type, str) if form_enc_type else False
        self.formmethod = type_check_error(form_method, str) if form_method else False
        self.fromnovalidate = type_check_error(from_no_validate, str) if from_no_validate else False
        self.formtarget = type_check_error(form_target, str) if form_target else False
        self.name_button = type_check_error(name_button, str) if name_button else False
        self.type = type_check_error(type, str) if type else False
        self.value = type_check_error(value, str) if value else False

    # needs a special generator as the 'name' value has to be included
    def _to_tag_generator(self) -> str:
        yield self.name # always yield an element name
        if self.classes:
            yield f"class={enclose_double_quote(' '.join(self.classes))}"

        if self.name_button:
            yield f"name={enclose_double_quote(self.name_button)}"

        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                yield f"{attr_name}={enclose_double_quote(attr_value)}"

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Canvas(HTMLElement):
    name="canvas"
    width:str|int
    height:str|int

    def __init__(self, *wraps,
                 width:str|int = False,
                 height:str|int = False,
                 **kwargs):
        super(Canvas, self).__init__(*wraps,name=Canvas.name,**kwargs)
        self.width = type_check_error(width,str|int) if width else False
        self.height = type_check_error(height,str|int) if height else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Caption(HTMLElement):
    name="caption"

    def __init__(self, *wraps, **kwargs):
        super(Caption, self).__init__(*wraps,name=Caption.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Cite(HTMLElement):
    name="cite"

    def __init__(self, *wraps, **kwargs):
        super(Cite, self).__init__(*wraps,name=Cite.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Code(HTMLElement):
    name="code"

    def __init__(self, *wraps, **kwargs):
        super(Code, self).__init__(*wraps,name=Code.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Col(HTMLElement):
    name="col"
    span:str|int

    def __init__(self, *wraps,
                 span:str|int=False,
                 **kwargs):
        super(Col, self).__init__(*wraps,name=Col.name,**kwargs)
        self.span = type_check_error(span, str|int) if span else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Colgroup(HTMLElement):
    name="colgroup"
    span:str|int

    def __init__(self, *wraps,
                 span:str|int=False,
                 **kwargs):
        super(Colgroup).__init__(*wraps,name=Colgroup.name,**kwargs)
        self.span = type_check_error(span, str|int) if span else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Data(HTMLElement):
    name="data"
    value:str|int

    def __init__(self, *wraps,
                 value:str=False,
                 **kwargs):
        super(Data, self).__init__(*wraps,name=Data.name,**kwargs)
        self.value = type_check_error(value, str) if value else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Datalist(HTMLElement):
    name="datalist"

    def __init__(self, *wraps, **kwargs):
        super(Datalist).__init__(*wraps,name=Datalist.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dd(HTMLElement):
    name="dd"

    def __init__(self, *wraps, **kwargs):
        super(Dd, self).__init__(*wraps,name=Dd.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Del(HTMLElement):
    name="del"
    cite:str
    datetime:str

    def __init__(self, *wraps,
                 cite:str=False,
                 datetime:str=False,
                 **kwargs):
        super(Del, self).__init__(*wraps,name=Del.name,**kwargs)
        self.cite = type_check_error(cite, str) if cite else False
        self.datetime = type_check_error(datetime, str) if datetime else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Details(HTMLElement):
    name="details"
    open:str

    def __init__(self, *wraps,
                 open_str:str=False,
                 **kwargs):
        super(Details, self).__init__(*wraps,name=Details.name,**kwargs)
        self.open = type_check_error(open_str, str) if open_str else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dfn(HTMLElement):
    name="dfn"

    def __init__(self, *wraps, **kwargs):
        super(Dfn, self).__init__(*wraps,name=Dfn.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dialog(HTMLElement):
    name="dialog"
    open:str

    def __init__(self, *wraps,
                 open_str:str=False,
                 **kwargs):
        super(Dialog, self).__init__(*wraps,name=Dialog.name,**kwargs)
        self.open = type_check_error(open_str, str) if open_str else False

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dir(HTMLElement):
    name="dir"

    def __init__(self, *wraps, **kwargs):
        super(Dir, self).__init__(*wraps,name=Dir.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Div(HTMLElement):
    name="div"

    def __init__(self, *wraps, **kwargs):
        super(Div, self).__init__(*wraps,name=Div.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dl(HTMLElement):
    name="dl"

    def __init__(self, *wraps, **kwargs):
        super(Dl, self).__init__(*wraps,name=Dl.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Dt(HTMLElement):
    name="dt"

    def __init__(self, *wraps, **kwargs):
        super(Dt, self).__init__(*wraps,name=Dt.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Em(HTMLElement):
    name="em"

    def __init__(self, *wraps, **kwargs):
        super(Em, self).__init__(*wraps,name=Em.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Embed(HTMLElement):
    name="embed"

    def __init__(self, *wraps, **kwargs):
        super(Embed, self).__init__(*wraps,name=Embed.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Fieldset(HTMLElement):
    name="fieldset"
    disabled:str
    form:str
    name_field:str

    def __init__(self, *wraps,
                 disabled:str = False,
                 form:str = False,
                 name_field:str = False,
                 **kwargs):
        super(Fieldset).__init__(*wraps,name=Fieldset.name,**kwargs)
        self.disabled =  type_check_error(disabled,str) if disabled else False
        self.form =  type_check_error(form,str) if form else False
        self.name_field =  type_check_error(name_field,str) if name_field else False

    # needs a special generator as the 'name' value has to be included
    def _to_tag_generator(self) -> str:
        yield self.name # always yield an element name
        if self.classes:
            yield f"class={enclose_double_quote(' '.join(self.classes))}"

        if self.name_field:
            yield f"name={enclose_double_quote(self.name_field)}"

        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                yield f"{attr_name}={enclose_double_quote(attr_value)}"

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Figcaption(HTMLElement):
    name="figcaption"

    def __init__(self, *wraps, **kwargs):
        super(Figcaption, self).__init__(*wraps,name=Figcaption.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Figure(HTMLElement):
    name="figure"

    def __init__(self, *wraps, **kwargs):
        super(Figure, self).__init__(*wraps,name=Figure.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Font(HTMLElement):
    name="font"

    def __init__(self, *wraps, **kwargs):
        super(Font, self).__init__(*wraps,name=Font.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Footer(HTMLElement):
    name="footer"

    def __init__(self, *wraps, **kwargs):
        super(Footer, self).__init__(*wraps,name=Footer.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Form(HTMLElement):
    name="form"

    def __init__(self, *wraps, **kwargs):
        super(Form, self).__init__(*wraps,name=Form.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H1(HTMLElement):
    name="h1"

    def __init__(self, *wraps, **kwargs):
        super(H1, self).__init__(*wraps,name=H1.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H2(HTMLElement):
    name="h2"

    def __init__(self, *wraps, **kwargs):
        super(H2, self).__init__(*wraps,name=H2.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H3(HTMLElement):
    name="h3"

    def __init__(self, *wraps, **kwargs):
        super(H3, self).__init__(*wraps,name=H3.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H4(HTMLElement):
    name="h4"

    def __init__(self, *wraps, **kwargs):
        super(H4, self).__init__(*wraps,name=H4.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H5(HTMLElement):
    name="h5"

    def __init__(self, *wraps, **kwargs):
        super(H5, self).__init__(*wraps,name=H5.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class H6(HTMLElement):
    name="h6"

    def __init__(self, *wraps, **kwargs):
        super(H6, self).__init__(*wraps,name=H6.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Head(HTMLElement):
    name="head"

    def __init__(self, *wraps, **kwargs):
        super(Head, self).__init__(*wraps,name=Head.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Header(HTMLElement):
    name="header"

    def __init__(self, *wraps, **kwargs):
        super(Header, self).__init__(*wraps,name=Header.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Hr(HTMLElement):
    name="hr"

    def __init__(self, *wraps, **kwargs):
        super(Hr, self).__init__(*wraps,name=Hr.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Html(HTMLElement):
    name="html"

    def __init__(self, *wraps, **kwargs):
        super(Html, self).__init__(*wraps,name=Html.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class I(HTMLElement):
    name="i"

    def __init__(self, *wraps, **kwargs):
        super(I, self).__init__(*wraps,name=I.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Iframe(HTMLElement):
    name="iframe"

    def __init__(self, *wraps, **kwargs):
        super(Iframe, self).__init__(*wraps,name=Iframe.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Img(HTMLElement):
    name="img"

    def __init__(self, *wraps, **kwargs):
        super(Img, self).__init__(*wraps,name=Img.name,**kwargs)
@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Input(HTMLElement):
    name="input"

    def __init__(self, *wraps, **kwargs):
        super(Input, self).__init__(*wraps,name=Input.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ins(HTMLElement):
    name="ins"

    def __init__(self, *wraps, **kwargs):
        super(Ins, self).__init__(*wraps,name=Ins.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Kbd(HTMLElement):
    name="kbd"

    def __init__(self, *wraps, **kwargs):
        super(Kbd, self).__init__(*wraps,name=Kbd.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Label(HTMLElement):
    name="label"

    def __init__(self, *wraps, **kwargs):
        super(Label, self).__init__(*wraps,name=Label.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Legend(HTMLElement):
    name="legend"

    def __init__(self, *wraps, **kwargs):
        super(Legend, self).__init__(*wraps,name=Legend.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Li(HTMLElement):
    name="li"

    def __init__(self, *wraps, **kwargs):
        super(Li, self).__init__(*wraps,name=Li.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Link(HTMLElement):
    name="link"

    def __init__(self, *wraps, **kwargs):
        super(Link, self).__init__(*wraps,name=Link.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Main(HTMLElement):
    name="main"

    def __init__(self, *wraps, **kwargs):
        super(Main, self).__init__(*wraps,name=Main.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Map(HTMLElement):
    name="map"

    def __init__(self, *wraps, **kwargs):
        super(Map, self).__init__(*wraps,name=Map.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Mark(HTMLElement):
    name="mark"

    def __init__(self, *wraps, **kwargs):
        super(Mark, self).__init__(*wraps,name=Mark.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Meta(HTMLElement):
    name="meta"

    def __init__(self, *wraps, **kwargs):
        super(Meta, self).__init__(*wraps,name=Meta.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Meter(HTMLElement):
    name="meter"

    def __init__(self, *wraps, **kwargs):
        super(Meter, self).__init__(*wraps,name=Meter.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Nav(HTMLElement):
    name="nav"

    def __init__(self, *wraps, **kwargs):
        super(Nav, self).__init__(*wraps,name=Nav.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Noframes(HTMLElement):
    name="noframes"

    def __init__(self, *wraps, **kwargs):
        super(Noframes).__init__(*wraps,name=Noframes.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Noscript(HTMLElement):
    name="noscript"

    def __init__(self, *wraps, **kwargs):
        super(Noscript).__init__(*wraps,name=Noscript.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Object(HTMLElement):
    name="object"

    def __init__(self, *wraps, **kwargs):
        super(Object, self).__init__(*wraps,name=Object.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ol(HTMLElement):
    name="ol"

    def __init__(self, *wraps, **kwargs):
        super(Ol, self).__init__(*wraps,name=Ol.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Optgroup(HTMLElement):
    name="optgroup"

    def __init__(self, *wraps, **kwargs):
        super(Optgroup).__init__(*wraps,name=Optgroup.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Option(HTMLElement):
    name="option"

    def __init__(self, *wraps, **kwargs):
        super(Option, self).__init__(*wraps,name=Option.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Output(HTMLElement):
    name="output"

    def __init__(self, *wraps, **kwargs):
        super(Output, self).__init__(*wraps,name=Output.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class P(HTMLElement):
    name="p"

    def __init__(self, *wraps, **kwargs):
        super(P, self).__init__(*wraps,name=P.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Param(HTMLElement):
    name="param"

    def __init__(self, *wraps, **kwargs):
        super(Param, self).__init__(*wraps,name=Param.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Picture(HTMLElement):
    name="picture"

    def __init__(self, *wraps, **kwargs):
        super(Picture, self).__init__(*wraps,name=Picture.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Pre(HTMLElement):
    name="pre"

    def __init__(self, *wraps, **kwargs):
        super(Pre, self).__init__(*wraps,name=Pre.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Progress(HTMLElement):
    name="progress"

    def __init__(self, *wraps, **kwargs):
        super(Progress).__init__(*wraps,name=Progress.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Q(HTMLElement):
    name="q"

    def __init__(self, *wraps, **kwargs):
        super(Q, self).__init__(*wraps,name=Q.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Rp(HTMLElement):
    name="rp"

    def __init__(self, *wraps, **kwargs):
        super(Rp, self).__init__(*wraps,name=Rp.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Rt(HTMLElement):
    name="rt"

    def __init__(self, *wraps, **kwargs):
        super(Rt, self).__init__(*wraps,name=Rt.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ruby(HTMLElement):
    name="ruby"

    def __init__(self, *wraps, **kwargs):
        super(Ruby, self).__init__(*wraps,name=Ruby.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class S(HTMLElement):
    name="s"

    def __init__(self, *wraps, **kwargs):
        super(S, self).__init__(*wraps,name=S.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Samp(HTMLElement):
    name="samp"

    def __init__(self, *wraps, **kwargs):
        super(Samp, self).__init__(*wraps,name=Samp.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Script(HTMLElement):
    name="script"

    def __init__(self, *wraps, **kwargs):
        super(Script, self).__init__(*wraps,name=Script.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Section(HTMLElement):
    name="section"

    def __init__(self, *wraps, **kwargs):
        super(Section, self).__init__(*wraps,name=Section.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Select(HTMLElement):
    name="select"

    def __init__(self, *wraps, **kwargs):
        super(Select, self).__init__(*wraps,name=Select.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Small(HTMLElement):
    name="small"

    def __init__(self, *wraps, **kwargs):
        super(Small, self).__init__(*wraps,name=Small.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Source(HTMLElement):
    name="source"

    def __init__(self, *wraps, **kwargs):
        super(Source, self).__init__(*wraps,name=Source.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Span(HTMLElement):
    name="span"

    def __init__(self, *wraps, **kwargs):
        super(Span, self).__init__(*wraps,name=Span.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Strike(HTMLElement):
    name="strike"

    def __init__(self, *wraps, **kwargs):
        super(Strike, self).__init__(*wraps,name=Strike.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Strong(HTMLElement):
    name="strong"

    def __init__(self, *wraps, **kwargs):
        super(Strong, self).__init__(*wraps,name=Strong.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Style(HTMLElement):
    name="style"

    def __init__(self, *wraps, **kwargs):
        super(Style, self).__init__(*wraps,name=Style.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Sub(HTMLElement):
    name="sub"

    def __init__(self, *wraps, **kwargs):
        super(Sub, self).__init__(*wraps,name=Sub.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Summary(HTMLElement):
    name="summary"

    def __init__(self, *wraps, **kwargs):
        super(Summary, self).__init__(*wraps,name=Summary.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Sup(HTMLElement):
    name="sup"

    def __init__(self, *wraps, **kwargs):
        super(Sup, self).__init__(*wraps,name=Sup.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Svg(HTMLElement):
    name="svg"

    def __init__(self, *wraps, **kwargs):
        super(Svg, self).__init__(*wraps,name=Svg.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Table(HTMLElement):
    name="table"

    def __init__(self, *wraps, **kwargs):
        super(Table, self).__init__(*wraps,name=Table.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tbody(HTMLElement):
    name="tbody"

    def __init__(self, *wraps, **kwargs):
        super(Tbody, self).__init__(*wraps,name=Tbody.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Td(HTMLElement):
    name="td"

    def __init__(self, *wraps, **kwargs):
        super(Td, self).__init__(*wraps,name=Td.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Template(HTMLElement):
    name="template"

    def __init__(self, *wraps, **kwargs):
        super(Template).__init__(*wraps,name=Template.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Textarea(HTMLElement):
    name="textarea"

    def __init__(self, *wraps, **kwargs):
        super(Textarea).__init__(*wraps,name=Textarea.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tfoot(HTMLElement):
    name="tfoot"

    def __init__(self, *wraps, **kwargs):
        super(Tfoot, self).__init__(*wraps,name=Tfoot.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Th(HTMLElement):
    name="th"

    def __init__(self, *wraps, **kwargs):
        super(Th, self).__init__(*wraps,name=Th.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Thead(HTMLElement):
    name="thead"

    def __init__(self, *wraps, **kwargs):
        super(Thead, self).__init__(*wraps,name=Thead.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Time(HTMLElement):
    name="time"

    def __init__(self, *wraps, **kwargs):
        super(Time, self).__init__(*wraps,name=Time.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Title(HTMLElement):
    name="title"

    def __init__(self, *wraps, **kwargs):
        super(Title, self).__init__(*wraps,name=Title.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tr(HTMLElement):
    name="tr"

    def __init__(self, *wraps, **kwargs):
        super(Tr, self).__init__(*wraps,name=Tr.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Track(HTMLElement):
    name="track"

    def __init__(self, *wraps, **kwargs):
        super(Track, self).__init__(*wraps,name=Track.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Tt(HTMLElement):
    name="tt"

    def __init__(self, *wraps, **kwargs):
        super(Tt, self).__init__(*wraps,name=Tt.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class U(HTMLElement):
    name="u"

    def __init__(self, *wraps, **kwargs):
        super(U, self).__init__(*wraps,name=U.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Ul(HTMLElement):
    name="ul"

    def __init__(self, *wraps, **kwargs):
        super(Ul, self).__init__(*wraps,name=Ul.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Var(HTMLElement):
    name="var"

    def __init__(self, *wraps, **kwargs):
        super(Var, self).__init__(*wraps,name=Var.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Video(HTMLElement):
    name="video"

    def __init__(self, *wraps, **kwargs):
        super(Video, self).__init__(*wraps,name=Video.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Wbr(HTMLElement):
    name="wbr"

    def __init__(self, *wraps, **kwargs):
        super(Wbr, self).__init__(*wraps,name=Wbr.name,**kwargs)

# ----------------------------------------------------------------------------------------------------------------------
# - Pseudo elements -
# ----------------------------------------------------------------------------------------------------------------------
class _Pseudo(HTMLElement):
    def __init__(self, *wraps, **kwargs):
        super().__init__(*wraps,name=self.name,**kwargs)

class _PseudoWithValue(_Pseudo):
    value:Any

    def __init__(self, value,*wraps, **kwargs):
        self.value=value
        super().__init__(*wraps,**kwargs)

    def to_tag(self):
        return None
    def to_tag_end(self):
        return None
    def __str__(self):
        return None

    def to_css_selector(self, full: bool = False) -> str:
        classes = f".{'.'.join(self.classes)}" if self.classes else ""
        id_str = f"#{self.id}" if self.id else ""

        attr: list[str] = []
        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                attr.append(f"{attr_name}={enclose_double_quote(attr_value)}")

        if isinstance(self.value,HTMLElement):
            value = self.value.to_css_selector()
        elif isinstance(self.value, type) and issubclass(self.value, HTMLElement):
            value = self.value().to_css_selector()
        else:
            value=str(self.value)

        if not full or not attr:
            return f"{classes}{id_str}{self.name}({value})"
        else:
            return f"{classes}{id_str}[{','.join(attr)}]{self.name}({value})"


class PseudoActive(_Pseudo):
    name = ":active"
class PseudoAfter(_Pseudo):
    name = "::after"
class PseudoBefore(_Pseudo):
    name = "::before"
class PseudoChecked(_Pseudo):
    name = ":checked"
class PseudoDefault(_Pseudo):
    name = ":default"
class PseudoDisabled(_Pseudo):
    name = ":disabled"
class PseudoEmpty(_Pseudo):
    name = ":empty"
class PseudoEnabled(_Pseudo):
    name = ":enabled"
class PseudoFirstChild(_Pseudo):
    name = ":first-child"
class PseudoFirstLetter(_Pseudo):
    name = ":first-letter"
class PseudoFirstLine(_Pseudo):
    name = "::first-line"
class PseudoFirstOfType(_Pseudo):
    name = ":first-of-type"
class PseudoFocus(_Pseudo):
    name = ":focus"
class PseudoFullscreen(_Pseudo):
    name = ":fullscreen"
class PseudoHover(_Pseudo):
    name = ":hover"
class PseudoInRange(_Pseudo):
    name = ":in-range"
class PseudoIndeterminate(_Pseudo):
    name = ":indeterminate"
class PseudoInvalid(_Pseudo):
    name = ":invalid"
class PseudoLang(_PseudoWithValue):
    name = ":lang"
class PseudoLastChild(_Pseudo):
    name = ":last-child"
class PseudoLastOfType(_Pseudo):
    name = ":last-of-type"
class PseudoLink(_Pseudo):
    name = ":link"
class PseudoMarker(_Pseudo):
    name = "::marker"
class PseudoNot(_PseudoWithValue):
    name = ":not"
class PseudoNthChild(_PseudoWithValue):
    name = ":nth-child"
class PseudoNthLastChild(_PseudoWithValue):
    name = ":nth-last-child"
class PseudoNthLastOfType(_PseudoWithValue):
    name = ":nth-last-of-child"
class PseudoNthOfType(_PseudoWithValue):
    name = ":nth-of-child"
class PseudoOnlyOfType(_Pseudo):
    name = ":only-of-type"
class PseudoOnlyChild(_Pseudo):
    name = ":only-child"
class PseudoOptional(_Pseudo):
    name = ":optional"
class PseudoOutOfRange(_Pseudo):
    name = ":out-of-range"
class PseudoPlaceholder(_Pseudo):
    name = "::placeholder"
class PseudoReadOnly(_Pseudo):
    name = ":read-only"
class PseudoReadWrite(_Pseudo):
    name = ":read-write"
class PseudoRequired(_Pseudo):
    name = ":required"
class PseudoRoot(_Pseudo):
    name = ":root"
class PseudoSelection(_Pseudo):
    name = "::selection"
class PseudoTarget(_Pseudo):
    name = ":target"
class PseudoValid(_Pseudo):
    name = ":valid"
class PseudoVisited(_Pseudo):
    name = ":visited"