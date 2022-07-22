# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import setuptools

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def readme_handler() -> str:
    with open("README.md", "r") as readme_file:
        return readme_file.read()

def version_handler() -> str:
    # ------------------------------------------------------------------------------------------------------------------
    version = 1,5,0 # <-- DEFINE THE VERSION IN A TUPLE FORMAT HERE
    # ------------------------------------------------------------------------------------------------------------------
    version_str = ".".join(str(i) for i in version)

    with open("src/AthenaLib/_info/_v.py", "w") as file:
        file.write(f"def _version():\n    return '{version_str}'")

    return version_str

# ------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    setuptools.setup(
        name="AthenaLib",
        version=version_handler(),
        author="Andreas Sas",
        author_email="",
        description="A Library for Directive Athena related Python Packages",
        long_description=readme_handler(),
        long_description_content_type="text/markdown",
        url="https://github.com/DirectiveAthena/AthenaLib",
        project_urls={
            "Bug Tracker": "https://github.com/DirectiveAthena/AthenaLib/issues",
        },
        license="GPLv3",
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        python_requires=">=3.10",
        install_requires=[
            "AthenaColor~=6.0.1"
        ]
    )