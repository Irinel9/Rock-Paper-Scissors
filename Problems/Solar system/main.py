planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file_planets = open('planets.txt', 'w', encoding='utf-8')
for i in planets:
    file_planets.writelines(i + '\n')
file_planets.close()
