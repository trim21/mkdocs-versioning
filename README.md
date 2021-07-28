# mkdocs-versioning

`mkdocs-versioning` is a plugin for [mkdocs](https://www.mkdocs.org/), a tool designed to create static websites usually for generating project documentation.

Support reading version from env var in ReadTheDocs.

## Setup

Install the plugin using pip:

```bash
pip install https://github.com/Trim21/mkdocs-versioning/archive/master.tar.gz
```

Next, add the following lines to your `mkdocs.yml`:

```yml
plugins:
  - search
  - mkdocs-versioning:
      version: READTHEDOCS_VERSION
#     default: developing
```
