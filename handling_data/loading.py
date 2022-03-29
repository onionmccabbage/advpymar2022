# we need to read in the JSON from an external file
import json

def main():
    # open the json text file and read in the data
    # fin = open('todos.json', 'rt') # if it's in the current folder
    fin = open('handling_data/todos.json', 'rt') # if it's in some other folder
    all_j = fin.read() # we now have some JSON
    all_l = json.loads(all_j) # 'loads' is load-string
    # show a few members of the data
    print(type(all_l))
    for i in range(0,11):
        print( all_l[i] )
    # we could choose to iterate over this data structure, commiting the members to a database

if __name__ == '__main__':
    main()