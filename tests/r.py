from prompt_toolkit import Application
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit.widgets import TextArea

# Create four text areas for the four segments of the window.
large_text_area = TextArea('Large segment', style='bg:#88ff88 #000000')
small_text_area1 = TextArea('Small segment 1', style='bg:#8888ff #000000')
small_text_area2 = TextArea('Small segment 2', style='bg:#ff8888 #000000')
bottom_text_area = TextArea('Bottom segment', style='bg:#ffff88 #000000')

# Create a layout with a horizontal split: the large segment on the left and a vertical split on the right.
# The vertical split contains the two small segments.
# Below the horizontal split is the bottom segment.
root_container = VSplit([
    large_text_area,
    HSplit([
        small_text_area1,
        small_text_area2,
        bottom_text_area
    ])
])

layout = Layout(root_container)

# Create an application with the layout.
app = Application(layout=layout, full_screen=True)

app.run()