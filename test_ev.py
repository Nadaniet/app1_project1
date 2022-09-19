from fltk import *

cree_fenetre(400,400)

ev = attend_ev()

print("evenement",ev)

if type_ev(ev) == "ClicGauche":
	print("click gauche", abscisse(ev), ordonnee(ev))

ferme_fenetre()