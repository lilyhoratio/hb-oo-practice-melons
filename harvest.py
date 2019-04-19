############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = int(first_harvest)
        self.color = color
        self.is_seedless = bool(is_seedless)
        self.is_bestseller = bool(is_bestseller)
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        if type(pairing) == str:
            pairing = [pairing]
        self.pairings.extend(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType("musk", 1989, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    casaba = MelonType("cas", 2003, "orange", True, False, "casaba")
    casaba.add_pairing(["strawberries","mint"])
    crenshaw = MelonType("cren", 1996, "green", True, False, "crenshaw")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "yellow watermelon")
    yellow_watermelon.add_pairing("ice cream")

    # Fill in the rest
    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    return all_melon_types

# print(make_melon_types()) ## prints a list of objects: [<__main__.Melon Type object at 0x...> , ...]

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        pairing_string = ""
        for pairingtype in melon.pairings:
            pairing_string += f"\n- {pairingtype}"
        print(f"{melon.name} pairs well with {pairing_string}\n")

# print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_code = {}

    for melon in melon_types:
        melon_code[melon.code] = melon.name

    return melon_code  

# print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, 
        color_rating, field_num, harvested_by):
        # melon_type is instance of Class melon type

        self.melon_type = melon_type
        self.shape_rating = float(shape_rating)
        self.color_rating = float(color_rating)
        self.field_num = int(field_num)
        self.harvested_by = harvested_by

        self.sellable = self.is_sellable(self.shape_rating, self.color_rating, self.field_num)

    def is_sellable(self, shape_rating, color_rating, field_num):
        if (shape_rating > 5) and (color_rating > 5) and (field_num != 3):
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    print(melons_by_id)

    # melon1 = Melon(yellow_watermelon, 8, 7, 2, "Sheila")
    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, "Sheila")
    melon2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    
    melon4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")

    melon5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")

    melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")

    melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    return [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    # Fill in the rest 
    for melon in make_melons(make_melon_types()):
        can_sell = "CAN BE SOLD" if melon.sellable else "NOT SELLABLE"
        print(f"Harvested by {melon.harvested_by} from Field {melon.field_num} - {can_sell}\n")


get_sellability_report(make_melons(make_melon_types()))