
from random import randint
import linecache
import csv
import heapq, random





class Planet:

    def __init__(self, name, pos):
        self._elements = []
        self._name = name
        self._habitable = self.is_Habitable()
        self._size = self.planet_size()
        self.create_elements(self._size)
        self._position = pos


    def show_name(self):
        print(self._name)
        print('*********')
        print('Is habitable = ' + str(self._habitable))
        print('Planet Size = ' + self._size)
        print('Position = (' + self._position + ')')
        print('*********')
        self.most_elements(3)

    def show_elements(self):
        infile = open('elements.txt', 'rt')
        for line in infile:
            print(line)

    def show_element_percent(self, x):
        e = list(open('elements.txt', 'rt'))
        csvReader = list(csv.reader(e, delimiter='\t'))
        print(csvReader[x][1] + ' = ' +str((self._elements[x]/sum(self._elements))*100))

    def show_element(self, x):
        e = list(open('elements.txt', 'rt'))
        csvReader = list(csv.reader(e, delimiter='\t'))
        print(csvReader[x][1] + ' = ' +str(self._elements[x]))#print(csvReader[x][2] for symbols

    def show_element_amount(self, x):
        for name, amount in self._elements.items():
            if name == x:
                print(str(amount))


    def create_elements(self, size):
        multiplier = 1
        if size == 'small':
            multiplier = 10
        elif size == 'medium':
            multiplier = 1000
        else:
            multiplier = 100000
        for i in range(0,119):
            level = randint(1,2)
            if level == 1:
                value = randint(1,10 * multiplier)
                self._elements.append(value)
            elif level == 2:
                value = randint(1,100 * multiplier)
                self._elements.append(value)
            elif level == 3:
                value = randint(1,1000 * multiplier)
                self._elements.append(value)
            else:
                value = randint(1,10000 * multiplier)
                self._elements.append(value)


    def is_Habitable(self):
        supports_life = False
        chance = randint(1,100)
        if chance > 70:
            supports_life = True
        return supports_life

    def planet_size(self):
        size = 'asteroid'
        p_size = randint(1,3)
        if p_size == 1:
            size = 'small'
        elif p_size == 2:
            size = 'medium'
        else:
            size = 'large'
        return size

    def most_elements(self, x):
        print('the top ' + str(x) + ' elements:')
        top_elements = heapq.nlargest(x, (self._elements))
        for i in range(0,x):
            #print('#' + str(i+1) + ' most plentiful element:')
            self.show_element(int(self._elements.index(top_elements[i])))
