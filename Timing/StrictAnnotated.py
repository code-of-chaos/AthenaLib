# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import timeit
import profile

# Custom Library
from AthenaLib.StrictAnnotated.StrictAnnotated import StrictAnnotated

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def AnnotatedTest_1(a:str):
    return a

@StrictAnnotated
def AnnotatedTest_2(a:str) -> str:
    return a

@StrictAnnotated
def AnnotatedTest_3(a:str, b:str):
    return a,b

@StrictAnnotated
def AnnotatedTest_4(a:str, b:str) -> tuple[str,str]:
    return a,b

@StrictAnnotated
def AnnotatedTest_5(a:str, b:str,c):
    return a,b,c

@StrictAnnotated
def AnnotatedTest_6(a, b, c):
    return a,b,c

@StrictAnnotated
def AnnotatedTest_7(a:str, b:str, c:str, d:str, e:str, f:str, g:str) -> tuple[str,str,str,str,str,str,str]:
    return a,b,c,d,e,f,g


# ----------------------------------------------------------------------------------------------------------------------
# - Testing -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(f"AnnotatedTest_1: {timeit.repeat(lambda: AnnotatedTest_1('a'))}")
    print(f"AnnotatedTest_2: {timeit.repeat(lambda: AnnotatedTest_2('a'))}")
    print(f"AnnotatedTest_3: {timeit.repeat(lambda: AnnotatedTest_3('a','b'))}")
    print(f"AnnotatedTest_4: {timeit.repeat(lambda: AnnotatedTest_4('a','b'))}")
    print(f"AnnotatedTest_5: {timeit.repeat(lambda: AnnotatedTest_5('a','b','c'))}")
    print(f"AnnotatedTest_6: {timeit.repeat(lambda: AnnotatedTest_6('a','b','c'))}")
    print(f"AnnotatedTest_7: {timeit.repeat(lambda: AnnotatedTest_7('a','b','c','d','e','f','g'))}")

    # profile.run("AnnotatedTest_1('a')")