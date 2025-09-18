# Cards Plugin

The **Cards Plugin** allows you to create responsive grid cards in Markdown with support for:

- Clickable and non-clickable cards
- Markdown-formatted titles, descriptions, and link text
- Icons supported by Material for MkDocs

## 🔹 Usage

Configure the plugin in your `mkdocs.yml` file:

```yaml
plugins:
  - cards
```

### Standard Cards

Wrap card content in a block fenced with `::: cards`. Cards can include just a title and description:

```markdown
::: cards
- :material-lightbulb: Feature One
  This is a description of the feature.

- :octicons-tools-16: Feature Two
  Another description
:::
```

> **Note**: The generated HTML follows the hierarchy and structure used by [Material for MkDocs cards](https://squidfunk.github.io/mkdocs-material/reference/grids/#using-card-grids), so any styling or layout rules applied to Material cards will also apply here.

### Cards with Inline Links

Cards can optionally include a link at the bottom; only the link text is clickable.

```markdown
::: cards
- :material-lightbulb: Feature One
  This is a description of the feature.
  [Learn more](feature1.md)

- :octicons-tools-16: Feature Two
  Another description
  [Learn more](feature2.md)
:::
```

### Clickable Cards

To make the entire card a link, add the `clickable` option and include the link in `()`:

```markdown
::: cards clickable
- :material-rocket: Launch Feature
  Fast and reliable launch process.
  (https://example.com/launch)
:::
```

> **Note**: Clickable cards deviate from the standard Material for MkDocs card HTML hierarchy. The entire card is wrapped in an `<a>` tag. Some CSS rules applied to standard Material cards may need adjustment for clickable cards.

The plugin adds the following classes to allow custom styling:

| Element          | CSS Class    |
|------------------|--------------|
| Card container   | `grid cards` |
| Clickable <a>    | `card-link`  |
| Card title       | `card-title` |
| Card description | `card-desc`  |

You can target these classes in your CSS files for custom styling.

## 🔹 Notes

- Only [icons supported by Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/?h=icons#icons-emojis) will render correctly. Example syntax: `:material-arrow-right:`.
- The plugin leverages Material's emoji system to convert icons into inline SVGs.
- Markdown inside card titles, descriptions, and link text is fully parsed — you can use **bold**, _italics_, links, and other formatting.
