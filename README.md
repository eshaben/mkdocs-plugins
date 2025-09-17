# MkDocs Plugins Collection

A collection of custom [MkDocs](https://www.mkdocs.org/) plugins designed to extend [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Currently included:

- **Cards**: Turn simple Markdown blocks into responsive grid cards, with clickable or non-clickable layouts.
- **Minify**: Minify HTML, JS, and CSS files globally or by scope to optimize your site's performance.

## Installation

TODO: Add installation instructions.

## Usage

Enable one or more plugins in your `mkdocs.yml`:

```yaml
plugins:
  - cards
  - minify:
      minify_html: true
      minify_css: true
      minify_js: true
```

## Documentation

- [Cards Plugin Documentation](docs/cards.md)
- [Minify Plugin Documentation](docs/minify.md)

## License

This repository is licensed under the [BSD-2-Clause License](LICENSE).