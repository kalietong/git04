import sys
from collections import Counter
first_last = {
        "Aditya":"Pooruli",
        "Advait":"Chowdhary",
        "Alexander":"Cheng",
        "Allan":"Zhang",
        "Anish":"Chakrabarty",
        "Ankith":"Bachhu",
        "Anna": "Liu",
        "Anuraag":"Murugesan",
        "Anya":"Sengupta",
        "April":"Murillo",
        "Arhan":"Chaudhary",
        "Arjo":"Goswami",
        "Audrey":"Russell",
        "Ava":"Shah",
        "Avner":"Chen",
        "Avnish":"Kovi",
        "Ayric":"Tong",
        "Ayush":"Sharma",
        "Ben":"Sirivallop",
        "Bhavjit":"Bhangu",
        "Brianna":"Nguyen",
        "Chloe":"Lin",
        "Chohaechan":"Lee",
        "Christopher":"Grethen",
        "Daniel":"Cao",
        "Darcy":"Chew",
        "Davin":"Stewart",
        "Denise":"Fernandez",
        "Desmond":"Tran",
        "Dilsher":"Dhaliwal",
        "Dino":"Wun",
        "Felix":"Chang",
        "Forrest":"Mora",
        "Genesis":"Hautau",
        "Grace":"Feng",
        "Heath":"Myers",
        "Ilyanna":"Stewart",
        "Irshad":"Ali",
        "Ishaan":"Kale",
        "Jonah":"Gallagher",
        "Judah":"Hsu",
        "Judah":"Kim",
        "Julia":"Chan",
        "Kabir":"Samsi",
        "Kaitlyne":"Nguyen",
        "Kalie":"Tong",
        "Kashif":"Majid",
        "Kavish":"Kartha",
        "Killian":"Seller",
        "Krish":"Ananth",
        "Kuber":"Sathiya",
        "Liam":"Burch",
        "Lily":"Russell",
        "Lin-Woo":"Kim",
        "Lucas":"Stevenson",
        "Lucas":"Costa",
        "Luis":"Hernandez",
        "Lurii":"Tatishchev",
        "Maria":"Rufova",
        "Mario":"Hernandez",
        "Mario":"Pinzon",
        "Masoma":"Majid",
        "Miguel":"Hernandez",
        "Mihir":"Kale",
        "Milana":"Gorobchenko",
        "Nate":"Sirivallop",
        "Noah":"Hsu",
        "Olivia":"Koo",
        "Parker":"Shepard",
        "Parul":"Veda",
        "Priyanka":"Tadepalli",
        "Rohan":"Parikh",
        "Ronen":"Rosenberg",
        "Ryan":"Selvarajan",
        "Ryan":"Situ",
        "Saloni":"Sharma",
        "Samika":"Yedur",
        "Samvar":"Yedur",
        "Sanjana":"Rathore",
        "Siddharth":"Chavan",
        "Simaal":"Belgaumi", 
        "Sneha":"Chakrabarty",
        "Tiven":"Pangtono",
        "Trisha":"Guha",
        "Trisha":"Godara",
        "Vibhav":"Darsha",
        "Vincent":"Gao",
        "Violeta":"Druga",
        "Viraj":"Ghose",
        "Vivian":"Liu",
        "Vyas":"Koduvayur",
        "William":"Lau",
        "Yamini":"Malli",
        "Ying-Chen":"Chen",
        "Zachary":"Bashkin"
        }

desired_keys = []
#val = first_last.values()

#for key, value in first_last.items():
    #if key.count(value)>1:
    #if value.count(value)>1:
       # print(first_last.items(value))
        #desired_keys.append(key)
print("**Shared first names**")
#print(desired_keys)

print("**Shared last names**")

last = Counter(first_last.values())
for key in last:
    if Counter(first_last.values)>1:
        desired_keys.append(key)

print(desired_keys)


