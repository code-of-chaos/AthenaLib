# ----------------------------------------------------------------------------------------------------------------------
# - AthenaLib -
# ----------------------------------------------------------------------------------------------------------------------
def info(*,to_str:bool=False) -> None|str:
    # bare minimum import
    from AthenaColor import ForeNest, StyleNest
    from AthenaLib._version import _version

    line = "-"*128
    title = ForeNest.SlateGray(f"""{line}
{StyleNest.Bold("AthenaLib")} v{_version().to_str()}
is made by Andreas Sas and is a standard library for "{StyleNest.Italic("Athena...")}" packages
{line}
""")

    text = title

    # export to console or string
    if to_str:
        return text
    else:
        print(text)