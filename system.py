
from random import randint
import time
from planet import Planet



class System:

    def __init__(self, name):# **kwargs):
        self._planets = []
        self._map = []
        self._time = time.ctime()
        self._name = name
        self.create_planets()

    def show_system_info(self):
        print('\n\n********************************\n  ')
        self.show_planets()#print(self._planets)
        print('\n\n********************************\n' + self._time )

    def get_coordinates(self, grid):
        local_x = randint(1,9)
        local_y = randint(1,9)
        temp_coords = str(local_x) + ',' + str(local_y)
        if temp_coords in grid:
            temp_coords = self.get_coordinates(grid)
        return temp_coords

    def create_planets(self):
        number_of_planets = randint(1,9)
        local_coords = []
        local_coords.append('5,5') # add the sun
        for i in range(1,number_of_planets + 1):
            pos = self.get_coordinates(local_coords)
            local_coords.append(pos)
            planet_name = self._name + '-' + str(i)
            planet = Planet(planet_name, pos)
            self._planets.append(planet)
        #print('planets created, number of planets = ' + str(number_of_planets))




    def show_planets(self):
        livable_planets = []
        verbose = True
        for i in self._planets:
            if i._habitable:
                livable_planets.append(i._name + ' is habitable (' + i._position + ')')
            if verbose:
                print('\n')
                i.show_name()
                print('*********')
                i.show_element(26)
                i.show_element(8)
                i.show_element(79)
                print('*********\n')


        for each in livable_planets:
            print(each, sep='\n')


    def show_system_map(self):

        for i in range(1,10):
            map_row = []
            for j in range(1,10):

                placeholder = str(i) + ',' + str(j)
                taken = False
                for each in self._planets:
                    if each._position == placeholder:
                        taken = True
                if taken:
                    map_row.append(placeholder)
                elif placeholder == '5,5':
                    map_row.append('SUN')
                else:
                    map_row.append('   ')
            self._map.append(map_row)
        for each in self._map:
            print(each, sep='\n')
