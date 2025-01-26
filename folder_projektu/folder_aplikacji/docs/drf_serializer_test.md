from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji. serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# worzymy nowe obiekty

stanowisko = Stanowisko.objects.create(nazwa = "Kierownik", opis = "Zarządza tymi co zarządzają")
osoba = Osoba.objects.create(imie = "Jan", nazwisko = "Malinowski", plec = 2, stanowisko = stanowisko)

# inicjalizacja serializera dla Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# ('id" : 6, 'imie" : "Jan', 'nazwisko' : 'Malinowski', plec : 'Mezczyzna', 'stanowisko.id' : 4, 'data_dodania' : 'osoba.data_dodania')

osoba_json = JSONRenderer().render(osoba_serializer.data)
# ('id" : 6, 'imie" : "Jan', 'nazwisko' : 'Malinowski', plec : 'Mezczyzna', 'stanowisko' : 4, 'data_dodania' : '2025-01-26')

import io
# strumien danych JSON
stream = io.BytesIO(osoba_json)

# parsowanie json do słownika
data = JSONParser().parse(stream)

# tworzymy obiekt deserializera dla danych JSON
deserializer = OsobaSerializer(data= data)

# walidacja danych
print(deserializer.is_valid())
print(deserializer.errors)

# True


# błędne dane
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 'Nieznany', 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data = invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# False
# {'plec': 'Nieznany' is not valid choice.'}

# zapis do bazy danych
if deserializer.is_valid():
    deserializer.save()

# inicjowanie serializera dla stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają'}

# serializacja do JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają'}

# deserializacja z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data = data)

print(deserializer.is_valid())

if deserializer.is_valid():
    deserializer.save()

