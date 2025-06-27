import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Симуляція кидків
    sums = []
    probabilities = {x:0 for x in range(2,13)}
    print(probabilities)
    #{2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for _ in range(num_rolls):
        dice1 = random.randint( 1 , 6)
        dice2 = random.randint( 1 , 6)
        sum = dice1 + dice2
        sums.append(sum)
    
    for s in sums:
        probabilities[s]+=1
    
    print(probabilities)
    #{2: 3, 3: 5, 4: 9, 5: 10, 6: 3, 7: 22, 8: 16, 9: 14, 10: 9, 11: 4, 12: 5}
    
    
    probabilities_counted = {}
    
    for k,v in probabilities.items():
        new_v = v/num_rolls
        probabilities_counted.update({k:new_v})
    #print("mmm", probabilities_counted)
    return probabilities_counted 
    #{2: 0.03, 3: 0.05, 4: 0.09, 5: 0.1, 6: 0.03, 7: 0.22, 8: 0.16, 9: 0.14, 10: 0.09, 11: 0.04, 12: 0.05}
    

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)