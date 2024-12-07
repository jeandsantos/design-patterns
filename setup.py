from setuptools import find_packages, setup


def read_requirements(file_path: str) -> list[str]:
    """Read a requirements.txt file and return a list of packages with their versions."""
    packages = []
    with open(file_path) as file:
        for line in file:
            line_stripped = line.strip()
            if line_stripped and not line_stripped.startswith("#"):
                packages.append(line_stripped)
    return packages


setup(
    name="design_patterns",
    author="Jean Dos Santos",
    author_email="jeandsantos88@gmailcom",
    readme="README.md",
    python_requires=">=3.11",
    packages=find_packages(exclude=["tests"]),
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
    },
)
