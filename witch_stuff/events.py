from witch_stuff.witch_event import witch_event

events = []

events.append(witch_event())
events[-1].where = ((1, 1), None)
events[-1].messages.append("Elo mordo")
events[-1].messages.append("Witaj w mojej kuchniWitaj w mojej kuchniWitaj w mojej kuchniWitaj w mojej kuchniWitaj w mojej kuchniWitaj w mojej kuchniWitaj w mojej kuchni")

for i in range(len(events)):
    events[i].index = i
