from static_map import StaticMap, Line

m = StaticMap(600, 600, 80)

greenlake = [-122.3296, 47.6786]
udub = [-122.3066, 47.6562]

coordinates = [greenlake, udub]
line_outline = Line(coordinates, 'white', 6)
line = Line(coordinates, '#D2322D', 4)

m.add_line(line_outline)
m.add_line(line)

image = m.render()
image.save('northseattle.png')