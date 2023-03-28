all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(listColors):
	onlySexy = list(filter(lambda item : item["sexy"] == True, listColors))
	return onlySexy

onlySexysColors = filter_colors(all_colors)

def generate_li():
	createLI = list(map(lambda item : "<li>"+ item["label"] + "</li>", onlySexysColors))
	return createLI

print(generate_li())
