import re
from copy import deepcopy

from markdown import Markdown
from material.extensions import emoji as material_emoji
from mkdocs.plugins import BasePlugin

CARDS_RE = re.compile(r"::: *cards(?P<options>.*?)\n(?P<content>.*?)\n:::", re.DOTALL)


class CardsPlugin(BasePlugin):
    def on_page_markdown(self, markdown_text, page, config, files):
        # Copy markdown_extensions from mkdocs.yml
        extensions = deepcopy(config.get("markdown_extensions", []))
        extension_configs = {
            "pymdownx.emoji": {
                "emoji_index": material_emoji.twemoji,
                "emoji_generator": material_emoji.to_svg,
            }
        }

        md = Markdown(extensions=extensions, extension_configs=extension_configs)

        def parse_cards(block, clickable=False):
            cards = []
            current = {}
            for line in block.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("- "):
                    if current:
                        cards.append(current)
                        current = {}
                    current["title"] = line[2:].strip()
                    current["description"] = ""
                elif clickable and line.startswith("(") and line.endswith(")"):
                    current["link"] = line[1:-1].strip()
                elif (
                    not clickable
                    and line.startswith("[")
                    and "]" in line
                    and "(" in line
                    and ")" in line
                ):
                    text = line.split("]")[0][1:]
                    url = line.split("](")[1].split(")")[0]
                    current["link_text"] = text
                    current["link"] = url
                else:
                    if current.get("description"):
                        current["description"] += " " + line
                    else:
                        current["description"] = line
            if current:
                cards.append(current)
            return cards

        def replace_cards(match):
            options = match.group("options").strip()
            clickable = "clickable" in options
            raw_content = match.group("content").strip()
            cards = parse_cards(raw_content, clickable=clickable)

            html = [f'<div class="grid cards{" clickable" if clickable else ""}">']

            if clickable:
                for card in cards:
                    link = card.get("link", "#")
                    print("Converted:", md.convert(":material-arrow-right:"))

                    title_html = md.convert(card.get("title", ""))
                    desc_html = md.convert(card.get("description", ""))
                    html.append(
                        f'<a href="{link}" class="card-link">'
                        f'<span class="card-title">{title_html}</span>'
                        f'<span class="card-desc">{desc_html}</span>'
                        f"</a>"
                    )
            else:
                html.append("<ul>")
                for card in cards:
                    print("Converted:", md.convert(":material-arrow-right:"))

                    title_html = md.convert(card.get("title", ""))
                    desc_html = md.convert(card.get("description", ""))
                    link = card.get("link", "#")
                    link_text = md.convert(card.get("link_text", "Learn more"))
                    html.append("<li>")
                    html.append(title_html)
                    html.append(desc_html)
                    if link:
                        html.append(f'<p><a href="{link}">{link_text}</a></p>')
                    html.append("</li>")
                html.append("</ul>")

            html.append("</div>")
            return "\n".join(html)

        return CARDS_RE.sub(replace_cards, markdown_text)
