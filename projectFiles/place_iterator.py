class PlaceIterator:
    def __init__(self, places):
        self.places = places

    def iterate_places(self):
        return self.places

    def iterate_available_places(self):
        lst = []
        for temp in self.places:
            if "available" in temp:
               lst.append(temp)
        return lst
