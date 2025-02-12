import setuptools

found_packages = setuptools.find_packages(where="src")
print("Found packages:", found_packages)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Nikhil-1705"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "nikhil.bhandari17052002@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple text summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",  # corrected key name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=found_packages,
)
