from fltk import *


def parse_file(filename):
	f = open(filename)
	nb_values = 0
	all_values = []
	for l in f.readlines():
		t = l.split()	
		for s in t:
			if len(s)>0 and s[0] == '#':
				break # commentaire detecte
			if nb_values == 0:
				# doit etre PP3
				if s != 'P3':
					raise Exception('pas au format PP3')
			else:
				v = int(s)
				if nb_values == 1:
					width = v 
				elif nb_values == 2:
					height = v
				elif nb_values == 3:
					color_max = v
				else:
					all_values.append(v)
			nb_values += 1
	return width, height, color_max, all_values



def show_image(window_w, window_h, data):
	width, height, color_max, all_values = data
	w = window_w / width
	h = window_h / height
	if w == 0 or h == 0:
		raise Exception("image trop grande")
	c = min(w,h)
	t = 0
	for j in range(height):
		for i in range(width):
			r,g,b = all_values[t], all_values[t+1], all_values[t+2]
			r = int(255*r/color_max)
			g = int(255*g/color_max)
			b = int(255*b/color_max)
			color = "#%02x%02x%02x"%(r,g,b)
			rectangle(c*i, c*j, c*(i+1), c*(j+1), remplissage=color, couleur=color)
			t += 3

r,g,b=200,255,14
print("#%02x%02x%02x"%(r,g,b))

window_w, window_h = 400,400

cree_fenetre(window_w, window_h)
data = parse_file("ex100.ppm")
show_image(window_w, window_h, data)

#ligne(0, 0, 399, 399)  

attend_ev()
ferme_fenetre()