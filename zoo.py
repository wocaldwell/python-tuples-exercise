zoo = ('grounhog', 'cat', 'horse', 'rabbit', 'cardinal', 'coyote', 'fox', 'deer')

(grounhog, cat, horse, rabbit, cardinal, coyote, fox, deer) = zoo

zoo_list = list(zoo)


zoo_list.extend(['chipmunk', 'aligator gar'])
print(zoo_list)

zoo = tuple(zoo_list)

print(zoo)
