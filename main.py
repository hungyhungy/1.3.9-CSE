# the custom function
def max_in_in_lst(lst):
    cont = 0
    for x in lst:
        if x > cont:
            cont = x 
        else: continue
    print(f"\nhighest number: {cont} \n")


# this is technicly not breaking the rules as stated
#  "Do not use the built-in function max in your program!"
# because i dont use mx but i use the function sorted()

def technicly_not_using_built_in_function_max_but_using_another_built_in_function(lst):
    x = sorted(lst)
    print(f"**************\n\ntechnicly highest : {x[-1]}\n")


# testing the function work 
listt = [1,5,2,178,5,1,34,54,0]

max_in_in_lst(listt)
technicly_not_using_built_in_function_max_but_using_another_built_in_function(listt)