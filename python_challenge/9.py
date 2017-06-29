#http://www.pythonchallenge.com/pc/return/good.html

from PIL import Image,ImageDraw

a1 = []

a2 = []

pic = Image.new("RGBA", (600,600))
dr = ImageDraw.Draw(pic)

lines1 = []
for v in range(0, len(a1), 2):
	lines1.append((a1[v], a1[v+1]))
dr.line(lines1)


lines2 = []
for v in range(0, len(a2), 2):
	lines1.append((a2[v], a2[v+1]))
dr.line(lines2)

pic.show()

