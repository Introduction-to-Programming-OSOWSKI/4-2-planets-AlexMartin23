def planets(p):
    planets = ["murcury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    for i in range (0, 8):
        if p == planets[i]:
            return i + 1
    return p + " is not a planet"

print(planets("hello"))