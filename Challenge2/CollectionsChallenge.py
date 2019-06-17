
def ShowCollection(myList, name):
    print(f"\nShowing {name}")
    for element in myList:
        print(element)

def CreateListsAndShowThem():
    strings = list()
    strings.append("uno")
    strings.append("dos")
    strings.append("tres")
    strings.append("quatro")
    strings.append("cinco")
    strings.append("seis")
    strings.append("siete")
    strings.append("ocho")
    strings.append("neueve")
    strings.append("diez")

    rangeList = list(range(50, 100, 2))
    ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ShowCollection(strings, "String List")
    ShowCollection(rangeList, "Range List")
    ShowCollection(ints, "Integer List")

def CreateTupleAndShowIt():
    myTuple = ("test", 3, 9.99)
    ShowCollection(myTuple, "Tuple")

def CreateSetAndShow():
    set1 = set(range(1, 11))
    set2 = set(range(5, 16, 2))

    setUnion = set1.union(set2)
    setIntersection = set1.intersection(set2)
    set2Except = set2.difference(set1)

    ShowCollection(setUnion, "Set Union")
    ShowCollection(setIntersection, "Set Intersection")
    ShowCollection(set2Except, "Set Except")

def FavoriteFruits():
    fruits = frozenset(("apple", "orange", "grape", "mango", "watermelon", "strawberry"))
    favorites = set()
    favorites.add("strawberry")
    favorites.add("cantelope")

    fruitExceptoins = fruits.difference(favorites)
    print(f"All favorites are in the fruit list? {len(fruitExceptoins) == 0}")

def EnglishSpanishNumerTranslations():
    numberTranslations = {
        "one": "uno",
        "two": "tres",
        "three": "tres",
        "four": "cuatro",
        "five": "cinco",
        "six": "seis",
        "seven": "siete",
        "eight": "ocho",
        "nie": "nueve",
        "ten": "diez"
    }

    print(f"three --> {numberTranslations['three']}")
    print(f"six --> {numberTranslations['six']}")
    print(f"eight --> {numberTranslations['eight']}")