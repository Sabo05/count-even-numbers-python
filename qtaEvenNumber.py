def qtaEvenNumber(x, y) -> int: 
    cont = int(0)
    for i in range(x, y + 1): 
        if i % 2 == 0: 
            print(i)
            cont += 1
    return cont

print('Total even Number: ', qtaEvenNumber(3,25))

# Code to cont how many even number and print them in a range determinated by the user  
