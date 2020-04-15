'''
    Code for the Problem Statement 2
'''
def find_min_cost(city_from, city_to, total_cost, minimum, index, cost_table):

    if not city_to:
        if total_cost < minimum:
            minimum = total_cost
        return minimum
    for i in range(len(city_to)):
        temp_city_to = city_to[:]
        current_city = city_to[i]
        del temp_city_to[i]
        current_cost = total_cost + cost_table[city_from[index]][current_city]
        minimum = find_min_cost(city_from, temp_city_to, current_cost, minimum, index+1, cost_table)
    return minimum


COST_TABLE = {
    'Jaipur':{
        'Delhi':2500,
        'Kerala':4000,
        'Mumbai':3500
    },
    'Pune':{
        'Delhi':4000,
        'Kerala':6000,
        'Mumbai':3500
    },
    'Bangalore':{
        'Delhi':2000,
        'Kerala':4000,
        'Mumbai':2500
    }
}

if __name__ == "__main__":
    CITY_FROM = ['Jaipur', 'Pune', 'Bangalore']
    CITY_TO = ['Delhi', 'Kerala', 'Mumbai']
    TOTAL_COST = 0
    MIN = 9999999
    INDEX = 0

    if len(CITY_FROM) == len(CITY_TO):
        MIN = find_min_cost(CITY_FROM, CITY_TO, TOTAL_COST, MIN, INDEX, COST_TABLE)
        print('Minimum cost is:', MIN)
    else:
        print("Invalid Input")