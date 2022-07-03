# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import threading

from AthenaLib.models import HTMLElement
import AthenaLib.data.html as HTMLElementLib

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestHTML(TestStructure):
    def test_SingleElement(self):
        self.subtest_multiple_cases(
            # result    object_factory
            ("<span>",              lambda:HTMLElement(name="span").to_tag()),
            ("""<span class="test">""", lambda:HTMLElement(name="span", classes=["test"]).to_tag()),
            ("""<span class="test test2">""", lambda:HTMLElement(name="span", classes=["test", "test2"]).to_tag()),
            ("""<span id="test">""", lambda:HTMLElement(name="span", id="test").to_tag()),
            ("""<span class="test test2" id="test">""", lambda:HTMLElement(name="span", classes=["test", "test2"], id="test").to_tag()),
        )

    def test_NestedElement(self):
        self.assertEqual(
            "<span><p>Hello</p></span>",
            HTMLElementLib.Span(HTMLElementLib.P("Hello"))
        )
        self.assertEqual(
            '<span class="test"><p>Hello</p></span>',
            HTMLElementLib.Span(
                HTMLElementLib.P("Hello"),
                classes=["test"]
            )
        )
        self.assertEqual(
            '<span class="test"><p class="test2">Hello</p></span>',
            HTMLElementLib.Span(
                HTMLElementLib.P(
                    "Hello",
                    classes=["test2"]
                ),
                classes=["test"]
            )
        )

    def test_to_dict(self):
        self.assertEqual(
            {
                'alt': "something",
                'classes': ['test', 'test2'],
                'height': 100,
                'href': "next.html",
                'id': 'test',
                'img': "blank.jpg",
                'lang': "EN",
                'name': 'span',
                'style': "color:red;",
                'title': "Itsme",
                'width': 100
            },
            HTMLElement(
                name="span",
                classes=["test", "test2"],
                id="test",
                alt="something",
                height=100,
                width=100,
                img="blank.jpg",
                href="next.html",
                lang="EN",
                style="color:red;",
                title="Itsme"
            
            ).to_dict()
        )
