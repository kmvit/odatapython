import setuptools

setuptools.setup(
    name="odatapython",
    version="0.0.2",
    author="Andrey Galkin",
    author_email="justscoundrel@yandex.ru",
    description="API for odata 1C",
    long_description="API for odata 1C 8",
    long_description_content_type="text/markdown",
    url="https://github.com/kmvit/odatapython.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
