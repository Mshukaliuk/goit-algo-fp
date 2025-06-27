items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

class  Item :
    def  __init__ ( self, product, cost, calories ):
        self.product = product
        self.cost = cost
        self.calories = calories
        self.ratio = calories/cost # -> max


# Greedy approach
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    list_of_objects= []
    
    for item, details in items.items():
        object_product = Item(item, details.get("cost"), details.get("calories"))
        list_of_objects.append(object_product)
    
    list_of_objects.sort(key= lambda x: x.ratio, reverse= True )
        
    for i in list_of_objects:
        if remaining_budget >= i.cost:
            chosen_items.append(i.product)
            total_calories = total_calories + i.calories
            remaining_budget = remaining_budget - i.cost
    
    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    list_of_objects= []
    
    for item, details in items.items():
        object_product = Item(item, details.get("cost"), details.get("calories"))
        list_of_objects.append(object_product)
    
    list_of_objects.sort(key= lambda x: x.ratio, reverse= True )
        

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]
    
    for i in range(len(items) + 1):
        for w in range (budget + 1):
            if i == 0 or w == 0 :
                    dp_table [i][w] = 0 
            elif list_of_objects[i - 1 ].cost <= w:
                    dp_table [i][w] = max(list_of_objects[i - 1 ].calories + dp_table[i - 1 ][w - list_of_objects[i - 1 ].cost], dp_table[i - 1 ][w])
            else :
                    dp_table[i][w] = dp_table[i - 1 ][w]
    
    chosen_items = []
    temp_budget = budget
    i = len(list_of_objects)

    while i > 0 and temp_budget > 0:
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            chosen_items.append(list_of_objects[i - 1].product)
            temp_budget -= list_of_objects[i - 1].cost
        i -= 1
    
    print(chosen_items)

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("greedy_result", greedy_result,"\n", "dp_result", dp_result)