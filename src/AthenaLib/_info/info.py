# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
import AthenaLib._info.formatting as f
from AthenaLib._info._v import _version

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def info(*, to_str: bool = False) -> None | str:
    line = "-" * 128
    header = f.header(f"""{line}
{f.title("AthenaLib", to_str)} v{_version()}
is made by Andreas Sas and is a standard library for "{f.reference("Athena...", to_str)}" packages
{line}
""", to_str)

    body = f"""
Package setup:
    {f.sub_modules("decorators", to_str)} : Decorators for functions or methods

    {f.sub_modules("fixes", to_str)} : Functions which resolve some issues which are brought up with Python
        An Example of this is nested asyncio loops. (A third party package is used for this, "{f.reference('nest_asyncio', to_str)}")

    {f.sub_modules("models", to_str)} : Basic classes which are meant to hold data. 
        These sort of classes are not meant to house a lot methods which interact with lots of other classes

    {f.sub_modules("functions", to_str)} : A collection of basic functions to handle various tasks
        This is often split up further into finer groups, like file manipulation, sorting algorithms, etc...
"""

    text = f"{header}{body}{line}"

    # export to console or string
    if to_str:
        return text
    else:
        print(text)