

from system import System
from random import randint

length = 9
start_int = 100
end_int = start_int + length

square_size = end_int - start_int + 1 # haven't tested this!
systems = []
space_grid = []

def create_space():
    #counter = 1

    gridx = []
    for i in range(square_size):
        gridy = []
        for j in range(square_size):
            temp = randint(1,100)
            if temp > 73:
                system1 = System(str(i)+','+str(j))
                systems.append(system1)
                gridy.append(str(i)+','+str(j))#gridy.append(True)#gridy.append('*')
            else:
                gridy.append('   ')#gridy.append('*')
            #gridy.append(str(counter))
            #counter = counter + 1
        gridx.append(gridy)
    return gridx



def create_system():
    return  create_space()
    #system1 = System(str(randint(0,99999)))
    #system1.show_system()

def count_systems(x):
        counter = 0
        for i in range(square_size):
            for j in range(square_size):
                if x[i][j] != '   ':
                    counter = counter + 1
        print('\n\n\nthere are ' + str(counter) + ' systems')
        return counter


def show_system(x):
    for each in x:
        print(each, sep='\n')


def write_system(x):
    system_id = '[(' + str(start_int) +','+ str(start_int) + '),(' + str(end_int) +','+ str(end_int) + ')]'
    print('writing system ' + system_id)
    file_name = 'system_' + str(start_int) +'-'+ str(end_int) + '.txt'
    outfile = open(file_name, 'wt')
    for each in x:
        print(each, file=outfile)
    #print(, file=outfile)
    outfile.close()
    print('finished writing to ' + file_name + '.\n')




def main():
    print('\n\n\nbehold, the universe...\n\n\n\n')
    space_grid = create_system()
    if square_size < 11:
        show_system(space_grid)

    rand_system = randint(0,count_systems(space_grid)-1) # needs to be space grid, to count empty sectors
    print('\nshowing system ' + systems[rand_system]._name + ':\n')
    systems[rand_system].show_system_info()
    systems[rand_system].show_system_map()

    write_system(space_grid)



if __name__ == '__main__': main()
