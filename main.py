def planets(p):
    planet = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    for i in range (0, 8):
        if p == planet[i]:
            return i + 1
    return p + " is not a planet"

print(planets("hello"))