#a list of tuples given that is students with their age sort it based on age
students=[("Aslaha",25),("Dinix",21),("Chessa",13)]
sorted_students=sorted(
    students,
    key=lambda x:x[1]

)
print(sorted_students)

