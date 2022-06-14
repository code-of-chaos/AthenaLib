# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def fix_nested_asyncio():
    """Simple function to create nested asyncio loops"""
    try:
        import nest_asyncio
        nest_asyncio.apply()
    except ImportError:
        raise ImportError("nest-asyncio package has to be installed for this to work")