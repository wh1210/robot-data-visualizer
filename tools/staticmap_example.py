# install using "pip install staticmap"

from staticmap import StaticMap, Line
from PIL import Image

m = StaticMap(600, 600, 80)

greenlake = [-122.3296, 47.6786]
udub = [-122.3066, 47.6562]

coordinates = [greenlake, udub]
line_outline = Line(coordinates, 'white', 6)
line = Line(coordinates, '#D2322D', 4)

m.add_line(line_outline)
m.add_line(line)

# image = m.render()
base_image = Image.new('RGB', (m.width, m.height), m.background_color)
image = m._draw_base_layer(base_image)
image.save('northseattle.png')