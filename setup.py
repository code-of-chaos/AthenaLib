# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import setuptools

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def version_handler() -> str:
    version = 1,0,0
    version_str = ".".join(str(i) for i in version)

    with open("src/AthenaLib/_v.py", "w") as file:
        file.write(f"def _version():\n    return '{version_str}'")

    return version_str

setuptools.setup(
    name="AthenaLib",
    version=version_handler(),
    author="Andreas Sas",
    author_email="",
    description="A Library of various code, used by Directive Athena Packages and applications",
    url="https://github.com/DirectiveAthena/VerSC-AthenaLib",
    project_urls={
        "Bug Tracker": "https://github.com/DirectiveAthena/VerSC-AthenaLib/issues",
    },
    license="GPLv3",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "nest_asyncio>=1.5.5"
    ]
)