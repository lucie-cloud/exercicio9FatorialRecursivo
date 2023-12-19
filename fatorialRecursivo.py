# Fatorial Recursivo

print('\n\t\t\t -- Fatorial Recursivo -- \n')

def fat_recursivo(n):
    if n > 1:
        fat = n * fat_recursivo(n - 1)
        return fat
    else:
        return 1


# teste Fatorial Recursivo
print(f'{6}! = {fat_recursivo(6)}')