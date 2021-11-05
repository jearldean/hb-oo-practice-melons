############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon type."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
    
    def add_pairing(self, pairing: str):
        """Add a food pairing to the instance's pairings list."""
    
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon_type1 = MelonType(code="musk",first_harvest=1998,color="green", 
        is_seedless=True,is_bestseller=True,name="Muskmelon")
    melon_type2 = MelonType(code="cas",first_harvest=2003,color="orange", 
        is_seedless=False,is_bestseller=False,name="Casaba")
    melon_type3 = MelonType(code="cren",first_harvest=1996,color="green", 
        is_seedless=False,is_bestseller=False,name="Crenshaw")
    melon_type4 = MelonType(code="yw",first_harvest=2013,color="yellow", 
        is_seedless=True,is_bestseller=True,name="Yellow Watermelon")

    melon_type1.add_pairing('mint')
    melon_type2.add_pairing('mint')
    melon_type2.add_pairing('strawberry')
    melon_type3.add_pairing('prosciutto')
    melon_type4.add_pairing('ice cream')

    all_melon_types.append(melon_type1)
    all_melon_types.append(melon_type2)
    all_melon_types.append(melon_type3)
    all_melon_types.append(melon_type4)

    return all_melon_types


def print_pairing_info(melon_types: list):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        separator = "\n- "
        pairs = separator.join(melon.pairings)
        print(f"{melon.name} pairs with {separator}{pairs}\n")
        

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types_dict = {}

    for melon_type in melon_types:
        interior_dict = {}
        interior_dict['pairings'] = melon_type.pairings
        interior_dict['first_harvest'] = melon_type.first_harvest
        interior_dict['color'] = melon_type.color
        interior_dict['is_seedless'] = melon_type.is_seedless
        interior_dict['is_bestseller'] = melon_type.is_bestseller
        interior_dict['name'] = melon_type.name
        melon_types_dict[melon_type.code] = interior_dict

    return melon_types_dict






############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, melon_id, melon_type, shape, color, field, worker
    ):
        """Initialize a melon."""

        self.melon_id = melon_id
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.worker = worker

    def is_sellable(a_melon):
        if a_melon.shape > 5 and a_melon.color > 5 and a_melon.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_type_dict = make_melon_type_lookup(all_melon_types)

    melons = []
    melons.append(Melon(melon_id=1, melon_type=melon_type_dict["yw"], shape=8, color=7, field=2, worker="Sheila"))
    melons.append(Melon(melon_id=2, melon_type=melon_type_dict["yw"], shape=3, color=4, field=2, worker="Sheila"))
    melons.append(Melon(melon_id=3, melon_type=melon_type_dict["yw"], shape=9, color=8, field=3, worker="Sheila"))
    melons.append(Melon(melon_id=4, melon_type=melon_type_dict["cas"], shape=10, color=6, field=35, worker="Sheila"))
    melons.append(Melon(melon_id=5, melon_type=melon_type_dict["cren"], shape=8, color=9, field=35, worker="Michael"))
    melons.append(Melon(melon_id=6, melon_type=melon_type_dict["cren"], shape=8, color=2, field=35, worker="Michael"))
    melons.append(Melon(melon_id=7, melon_type=melon_type_dict["cren"], shape=2, color=3, field=4, worker="Michael"))
    melons.append(Melon(melon_id=8, melon_type=melon_type_dict["musk"], shape=6, color=7, field=4, worker="Michael"))
    melons.append(Melon(melon_id=9, melon_type=melon_type_dict["yw"], shape=7, color=10, field=3, worker="Sheila"))

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Harvested by Sheila from Field 2 (CAN BE SOLD)
    for each_melon_instance in melons:
        worker_clause = f"Harvested by {each_melon_instance.worker}"
        field_clause = f"from Field {each_melon_instance.field}"
        sellable = Melon.is_sellable(each_melon_instance)
        sellable_clause = "(CAN BE SOLD)" if sellable else "(NOT SELLABLE)"
        print(worker_clause, field_clause, sellable_clause)


all_melon_types = make_melon_types()
melons = make_melons(all_melon_types)
get_sellability_report(melons)
