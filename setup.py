import setuptools

setuptools.setup(
    name="mkdocs-versioning",
    version="0.4.0",
    author="Trim21",
    author_email="trim21.me@gmail.com",
    description="A tool that allows for versioning sites built with mkdocs",
    long_description="checkout github",
    long_description_content_type="text/markdown",
    url="https://github.com/Trim21/mkdocs-versioning",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Documentation",
        'Topic :: Text Processing',
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-versioning = mkversion.entry:Entry',
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'PyYAML >= 5.3',
        'mkdocs >= 1.1'
    ]
)
