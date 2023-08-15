from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="jogo_pedra_papel_tesoura",
    version="0.0.1",
    author="j040",
    author_email="my_email",
    description="Um pacote para jogar o jogo Pedra, Papel e Tesoura",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)