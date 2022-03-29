module  = input("Enter a module code: ") # Input module code
switch = { # Use switch

    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "Object-Oriented Programming",
    "CSC1010": "Computer Networks"
}
print(switch[module]) # Print out module, given module code