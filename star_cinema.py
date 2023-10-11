from hall import Hall

class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls._hall_list.append(hall)
        else:
            print("Invalid object. Please provide an instance of the Hall class.")
