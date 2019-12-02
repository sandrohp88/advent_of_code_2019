# load data
file_handler = open('input.txt')
total_fuel_required = 0


def fuel_counter_upper(mass):
    if mass <= 7:
        return 0
    current_fuel_needed = mass // 3 - 2
    # return accumulator
    return fuel_counter_upper(current_fuel_needed) + current_fuel_needed


for row in file_handler:
    current_module_mass = int(row)
    total_fuel_required += fuel_counter_upper(current_module_mass)
print(total_fuel_required)
