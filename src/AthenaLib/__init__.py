# ----------------------------------------------------------------------------------------------------------------------
# - AthenaLib -
# ----------------------------------------------------------------------------------------------------------------------
def info(*,to_str:bool=False) -> None|str:
    # bare minimum import
    from AthenaColor import ForeNest, StyleNest
    from AthenaLib._version import _version

    line = "-"*128
    title = ForeNest.SlateGray(f"""{line}
{StyleNest.Bold("AthenaLib")} v{_version()}
is made by Andreas Sas and is a standard library for "{StyleNest.Italic("Athena...")}" packages
{line}
""")

    body = f"""
Package setup:
    {StyleNest.Bold(ForeNest.Pink("decorators"))} : Decorators for functions or methods
        
    {StyleNest.Bold(ForeNest.Pink("fixes"))} : Functions which resolve some issues which are brought up with Python
        An Example of this is nested asyncio loops. (A third party package is used for this, "{StyleNest.Italic('nest_asyncio')}")
    
    {StyleNest.Bold(ForeNest.Pink("models"))} : Basic classes which are meant to hold data. 
        These sort of classes are not meant to house a lot methods which interact with lots of other classes
    
    {StyleNest.Bold(ForeNest.Pink("functions"))} : A collection of basic functions to handle various tasks
        This is often split up further into finer groups, like file manipulation, sorting algorithms, etc...
"""

    text = f"{title}{body}"

    # export to console or string
    if to_str:
        return text
    else:
        print(text)