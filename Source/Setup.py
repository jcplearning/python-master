# Setup program for the project
import setuptools
setuptools.setup(
    name="Arthimetic",
    author="Chenni",
    author_email="abc@example.com",
    description="A simple arithmetic operations package",
    url="https://github.com/yourusername/arthimetic",
    version="0.1",
    packages=['Arthimetic'],
    python_requires='>=3.6',
    install_requires=['numpy', 'pandas'],
    entry_points={
        "console_scripts": [
            "arthimetic = Arthimetic:main",  # calls main() from __init__.py
        ]
    }
)
