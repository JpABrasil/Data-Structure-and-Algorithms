def isPalindrome(x):
    list_x = list(str(x))
    reversed_x = list_x[::-1] #O primeiro : indica o início do fatiamento.O segundo : indica o final do fatiamento.O -1 como passo indica que você está percorrendo a sequência de trás para frente.Então, [::-1] significa "comece do final, vá até o início, passando por cada elemento de trás para frente".
    if list_x == reversed_x:
        return True
    else:
        return False
result = isPalindrome(121)
print(result)