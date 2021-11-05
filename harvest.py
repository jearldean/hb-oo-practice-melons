############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, names 
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.names = names
    
    def add_pairing(self, pairing: str):
        """Add a food pairing to the instance's pairings list."""
    
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    return all_melon_types


def print_pairing_info(melon_types: list):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        pairs = "\n- ".join(melon.pairings)
        print(f"{melon.names} pairs with \n- {pairs}\n")
        



        #yellow_melon.add_pairing('mint')
#print(yellow_melon.pairings)
    # Fill in the rest
#Output: 
#Muskmelon pairs with
#- mint

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    
# code, first_harvest, color, is_seedless, is_bestseller, names
melon4 = MelonType(code="yw",first_harvest=2013,color="yellow", is_seedless=True,is_bestseller=True,names="Yellow Watermelon")
#print(yellow_melon.color)
#print(yellow_melon.is_bestseller)
#yellow_melon.add_pairing('mint')
#print(yellow_melon.pairings)
#print(f"{yellow_melon.names} is good with {yellow_melon.pairings}")


melon1 = MelonType(code="musk",first_harvest=1998,color="green", is_seedless=True,is_bestseller=True,names="Muskmelon")
melon2 = MelonType(code="cas",first_harvest=2003,color="orange", is_seedless=False,is_bestseller=False,names="Casaba")
melon3 = MelonType(code="cren",first_harvest=1996,color="green", is_seedless=False,is_bestseller=False,names="Crenshaw")

melon1.add_pairing('mint')
melon2.add_pairing('mint')
melon2.add_pairing('strawberry')
melon3.add_pairing('prosciutto')
melon4.add_pairing('ice cream')

melon_types = []
melon_types.append(melon1)
melon_types.append(melon2)
melon_types.append(melon3)
melon_types.append(melon4)
print_pairing_info(melon_types)
#print(melon1.print_pairing_info)
