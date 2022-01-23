def is_even(number):
    if number%2==0:
        return True
    else:
        return False    

even_num={}
starting=0
while starting<=100:

    if is_even(starting):
        is_even.append(starting)
        #print(f"EVEN {starting}")
    else:
        print(f"ODD {starting}")
    starting=starting+1

print("Finished")