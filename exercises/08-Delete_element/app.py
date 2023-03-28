people = ['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']

# Your code go here:


def deletePerson(person_name):
    # Your code go here:
    new_people = []
    for i in people:
        if i != person_name:
            new_people.append(i)
    return new_people

# Otra forma valida de resolver este problema
# def deletePerson(person_name):
#     new_people = list(filter(lambda item : item != person_name, people))
#     return new_people

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
