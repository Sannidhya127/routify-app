from rich import print
from rich.layout import Layout

layout = Layout()
print(layout)

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
# print(layout)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)
print(layout)
from rich.panel import Panel

layout["right"].split(
    Layout(Panel("Hello")),
    Layout(Panel("World!"))
)

layout["left"].update(
    "The mystery of life isn't a problem to solve, but a reality to experience."
)
print(layout)

print(layout.tree)

