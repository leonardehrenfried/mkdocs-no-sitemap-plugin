import os

import sys
from shutil import rmtree
from pathlib import Path
from setuptools import setup, Command


HERE = Path(__file__).parent

README = (HERE.joinpath("readme.md")).read_text()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(
            "{0} setup.py sdist bdist_wheel --universal".format(sys.executable)
        )

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        # self.status("Pushing git tags…")
        # os.system("git tag v{0}".format(about["__version__"]))
        # os.system("git push --tags")

        sys.exit()


setup(
    name="mkdocs-no-sitemap-plugin",
    version="0.0.1",
    packages=["mkdocs_no_sitemap_plugin"],
    url="https://github.com/leonardehrenfried/mkdocs-no-sitemap-plugin",
    license="MIT",
    author="leonardehrenfried",
    author_email="mail@leonard.io",
    description="Mkdocs plugin disable the generation.",
    long_description=README,
    long_description_content_type="text/markdown",
    entry_points={
        "mkdocs.plugins": [
            "no-sitemap = mkdocs_no_sitemap_plugin.plugin:NoSitemapPlugin"
        ]
    },
    cmdclass={"upload": UploadCommand},
)
