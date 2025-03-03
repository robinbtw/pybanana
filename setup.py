from setuptools import setup, find_packages

setup(
    name="pybanana",
    version="0.4.3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.0",
        "python-dateutil>=2.8.2",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "requests-mock>=1.11.0",
        ],
    },
    author="robin",
    author_email="xrobinsong@gmail.com",
    description="A Python wrapper for the GameBanana API",
    long_description="A powerful and intuitive Python client library for interacting with the GameBanana API",
    long_description_content_type="text/plain",
    url="https://github.com/robinbtw/pybanana",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)