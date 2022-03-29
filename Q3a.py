moduleCode  = input("Enter a module code: ") # Input module code
switch = { # Use dictionary to simulate switch in Python

    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "Object-Oriented Programming",
    "CSC1010": "Computer Networks"
}
# Print out module, given module code. Else print "Invalid module code"
print(switch.get(moduleCode, "Invalid module code")) 