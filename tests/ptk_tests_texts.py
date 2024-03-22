from prompt_toolkit import print_formatted_text, HTML

print_formatted_text(HTML('<b>This is bold</b>'))
print_formatted_text(HTML('<i>This is italic</i>'))
print_formatted_text(HTML('<u>This is underlined</u>'))

print_formatted_text(HTML('<ansired>This is red</ansired>'))
print_formatted_text(HTML('<ansigreen>This is green</ansigreen>'))

# Named colors (256 color palette, or true color, depending on the output).
print_formatted_text(HTML('<skyblue>This is sky blue</skyblue>'))
print_formatted_text(HTML('<seagreen>This is sea green</seagreen>'))
print_formatted_text(HTML('<violet>This is violet</violet>'))

# Colors from the ANSI palette.
print_formatted_text(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))

from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print_formatted_text(HTML('<aaa>Hello</aaa> <bbb>world</bbb>!'), style=style)

from prompt_toolkit import print_formatted_text, ANSI

print_formatted_text(ANSI('\x1b[31mhello \x1b[32mworld'))

from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

text = FormattedText([
    ('#ff0066', 'Hello'),
    ('', ' '),
    ('#44ff00 italic', 'World'),
])

print_formatted_text(text)

from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

# The text.
text = FormattedText([
    ('class:aaa', 'Hello'),
    ('', ' '),
    ('class:bbb', 'World'),
])

# The style sheet.
style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print_formatted_text(text, style=style)

from pygments.token import Token
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import PygmentsTokens

text = [
    (Token.Keyword, 'print'),
    (Token.Punctuation, '('),
    (Token.Literal.String.Double, '"'),
    (Token.Literal.String.Double, 'hello'),
    (Token.Literal.String.Double, '"'),
    (Token.Punctuation, ')'),
    (Token.Text, '\n'),
]

print_formatted_text(PygmentsTokens(text))

import pygments
from pygments.token import Token
from pygments.lexers.python import PythonLexer

from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit import print_formatted_text

# Printing the output of a pygments lexer.
tokens = list(pygments.lex('print("Hello")', lexer=PythonLexer()))
print_formatted_text(PygmentsTokens(tokens))

from prompt_toolkit.styles import Style

style = Style.from_dict({
    'pygments.keyword': 'underline',
    'pygments.literal.string': 'bg:#00ff00 #ffffff',
})
print_formatted_text(PygmentsTokens(tokens), style=style)

from prompt_toolkit.formatted_text import to_formatted_text, HTML
from prompt_toolkit import print_formatted_text

html = HTML('<aaa>Hello</aaa> <bbb>world</bbb>!')
text = to_formatted_text(html, style='class:my_html bg:#00ff00 italic')


from rich import print
from rich.panel import Panel
print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))


from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)


from rich.tree import Tree
from rich import print

tree = Tree("Rich Tree")
print(tree)

tree.add("foo")
tree.add("bar")
print(tree)

baz_tree = tree.add("baz")
baz_tree.add("[red]Red").add("[green]Green").add("[blue]Blue")
print(tree)

import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
    for row in range(12):
        time.sleep(0.4)  # arbitrary delay
        # update the renderable internally
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")


import random
import time

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())


import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
    for row in range(12):
        live.console.print(f"Working on row #{row}")
        time.sleep(0.4)
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")