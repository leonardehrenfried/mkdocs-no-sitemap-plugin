# Disable Mkdocs' sitemap

This plugin disables the generation of a sitemap in Mkdocs sites.

This is useful if you build and commit documentation on every commit and don't want to
see the git history cluttered with changes to `sitemap.xml` and in particular `sitemap.xml.gz`.

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