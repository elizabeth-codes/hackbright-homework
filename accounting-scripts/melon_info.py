"""Print out all the melons in our inventory."""

from melons import melons

# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')

# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

# def print_a_melons_info(filename):
#     melons.items()
#     for melon, melon_info in melons.items():
#         print(f'{melon}, {melon_info})

# print_a_melons_info("melons.py")


def print_one_melon(melon, melon_attributes):
    print(f"{melon}:{melon_attributes}")


for melon, melon_attributes in melons.items():
    print_one_melon(melon, melon_attributes)