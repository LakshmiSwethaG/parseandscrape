from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    version='1.0.0',
    install_requires=[
        'flask'
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
    },
)