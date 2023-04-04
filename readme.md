# Disable Mkdocs' sitemap

Mkdocs officially only supports relative links. While this makes sense there are situation where it is useful to make use of absolute links. For example when creating a document with absolute links to an image folder. 
If that file is to be moved later on, links are kept intact.

## Installation

```bash
pip install mkdocs-no-sitemap-plugin
```

## Usage

In your `mkdocs.yml` file add `no-sitemap` to the plugins entry:

```yaml
plugins:
  - no-sitemap
```