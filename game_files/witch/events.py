from game_files.witch.witch_event import witch_event

events = []

""" base for an event
events.append(witch_event())
events[-1].where = ((1, 1), None)
events[-1].messages.append("
events[-1].messages.append("
events[-1].messages.append("
events[-1].messages.append("
"""

events.append(witch_event())
events[-1].where = ((400, 0), None)
events[-1].messages.append("MUAHUAEHEUAHEUHAHUEHA!! [space]")
events[-1].messages.append("Znowu wpadłeś w moją pułapkę!")
events[-1].messages.append("Tym razem udało mi się zamknąć cię w grze komputerowej i zmienić cię w marny, czarny żeton!")
events[-1].messages.append("HAHAHAHAHAHAHH!")
events[-1].messages.append("Poruszasz się na WASD, spróbuj dość do jakiegoś poziomu")

events.append(witch_event())
events[-1].where = ((1, 0), None)
events[-1].messages.append("Dobrze ci idzie. Niektórzy mają taki pomysł, by wejść na tę czerwoną płytkę i zobaczyć, co się stanie.")
events[-1].messages.append("Mam nadzieję, że ty tego nie zrobiłeś.")
events[-1].messages.append("Zabiłoby cię to.")
events[-1].messages.append("Na szczęście udostępniam ci trochę moich mocy czasowych.")
events[-1].messages.append("Po kliknięciu Q cofasz czas o jedną jednostkę. R resetuje aktualny poziom.")
events[-1].messages.append("A ta czerwona płytka zmieni się w zieloną kiedy przejdziesz poziomy, które właśnie widzisz.")

events.append(witch_event())
events[-1].where = ((1, 6), None)
events[-1].messages.append("Świetnie ci idzie. Czy wiesz, że tylko 0.000001% ludzi dochodzi tak daleko?")

events.append(witch_event())
events[-1].where = ((1, 9), None)
events[-1].messages.append("Wszystkie poziomy są do przejścia. Sprawdzałam 6 razy.")

events.append(witch_event())
events[-1].where = ((1, 10), None)
events[-1].messages.append("Pamiętasz, kiedy mówiłam że tylko 0.000001% ludzi dochodzi tak daleko?")
events[-1].messages.append("Kłamałam.")
events[-1].messages.append("0.000001% ludzi nie dochodzi tak daleko.")
events[-1].messages.append("Najczęstsze przyczyny to: znudzenie, odcięcie prądu i śmierć ze starości.")
events[-1].messages.append("Ale i tak radzisz sobie świetnie!")

events.append(witch_event())
events[-1].where = ((1, 11), None)
events[-1].messages.append("DFS, mówi ci to coś, panie Ferdku?")

events.append(witch_event())
events[-1].where = ((1, 12), None)
events[-1].messages.append("Ten poziom jest prostszy niż się wydaje. Spróbuj wczuć się w rytm.")

events.append(witch_event())
events[-1].where = ((1, 13), None)
events[-1].messages.append("Super, to ostatni poizom z tego zone.")
events[-1].messages.append("Wygląda znajomo, nie?")
events[-1].messages.append("Mam nadzieję, że poprzedni poziom cię czegoś nauczył.")

events.append(witch_event())
events[-1].where = ((400, 0), (6, 2, 0))
events[-1].messages.append("No i zajebiście.")
events[-1].messages.append("Przed tobą następny hub.")

events.append(witch_event())
events[-1].where = ((101, 0), None)
events[-1].messages.append("To zone z poziomami generowanymi losowo.")
events[-1].messages.append("Za jego skończenie nie czeka cię absolutnie nic, ale możesz się poćwiczyć w tym najprostszym rodzaju poziomów.")

events.append(witch_event())
events[-1].where = ((400, 1), (5, 5, 0))
events[-1].messages.append("Masz przed sobą rozwidlenie.")
events[-1].messages.append("Jak możesz się domyślać, możesz kończyć te zone'y w dowolnej kolejności, ale i tak potrzebujesz przejsć oba")

events.append(witch_event())
events[-1].where = ((2, 1), None)
events[-1].messages.append("Ten klocek nie jest szczególnie ciekawy, ale i tak można z nim tworzyć fajne poziomy")

events.append(witch_event())
events[-1].where = ((2, 5), None)
events[-1].messages.append("Być może zastanawiasz się, co na ciebie czeka na końcu tego wszystkiego.")

events.append(witch_event())
events[-1].where = ((2, 6), None)
events[-1].messages.append("Czy Shrek coś ci mówi?")
events[-1].messages.append("Bo nagrodą na pewno nie jest wypuszczenie cię.")

events.append(witch_event())
events[-1].where = ((2, 7), None)
events[-1].messages.append("Będziesz rozwiązywał moje zagadki do końca świata.")

events.append(witch_event())
events[-1].where = ((2, 8), None)
events[-1].messages.append("O, a ten poziom może powinien ci się kojarzyć z pewną inną grą.")
events[-1].messages.append("Jej tytuł zaczyna się na U")
events[-1].messages.append("...a kończy na ndertale.")

events.append(witch_event())
events[-1].where = ((2, 9), None)
events[-1].messages.append("Ten poziom jest trudny. Spróbuj się skupić na trzech trójkach.")

events.append(witch_event())
events[-1].where = ((2, 10), None)
events[-1].messages.append("No dawaj, ostatni.")
events[-1].messages.append("Jak przeszedłeś poprzedni to ten też dasz radę.")

events.append(witch_event())
events[-1].where = ((501, 0), None)
events[-1].messages.append("O nie! To Giszowiec, Kolista! Szybko, uciekaj stąd zanim jakiś dres cię skroi!")


for i in range(len(events)):
    events[i].index = i
