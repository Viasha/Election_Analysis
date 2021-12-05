print("Hello World")
num_candidated= 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True

Counties= ["Arapahoe","Denver", "Jefferson"]
print(Counties[2])
print(Counties[0])
len(Counties)
Counties[0:2]
Counties[0:1]
Counties[:2]
Counties.append("El Paso")
print(Counties)
Counties.insert(2, "El Paso")
print(Counties)
Counties.remove("El Paso")
print(Counties)
Counties.pop(3)
print(Counties)
Counties[2]= "El Paso"
print(Counties)
Counties_tuple= ("Arapahoe", "Denver", "Jefferson")
len(Counties_tuple)
Counties_tuple[1]
Counties_dict={}
Counties_dict["Arapahoe"]= 422829
print(Counties_dict)
Counties_dict["Denver"]= 463353
Counties_dict["Jefferson"]= 432438
print(Counties_dict)
len(Counties_dict)
print(Counties_dict.items())
print(Counties_dict.keys())
print(Counties_dict.values())
print(Counties_dict.get("Denver"))


voting_data=[]
voting_data.append({"county": "Arapahoe", "registered_voters":422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registerd_voters": 432438})
print(voting_data)
voting_data.append({"county": "El Paso", "registered_voters": 461149})

Counties= ["Arapahoe","Denver", "Jefferson"]
if Counties[1] == 'Denver':
    print(Counties[1])

if "El Paso" in Counties:
    print("El Paso is in the list of Counties.")
else:
    print("El Paso is not the list of Counties.")

if "Arapahoe" in Counties and "El Paso" in Counties:
    print("Arapahoe and El Paso are in the list of Counties.")
else:
    print("Arapahoe or El Paso is not in the list of Counties")

if "Arapahoe" in Counties or "El Paso" in Counties:
    print("Arapahoe or El Paso is in the list if Counties")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in Counties and "El Paso" not in Counties:
    print("Only Arapahoe is in the list of Counties.")
else: 
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

temperature= int(input("what is the temperature outside?"))

if temperature >80 :
    print("Turn on the AC")
else:
    print("Open the windows")

#What is the score?
score= int(input("What is your test score?"))
#Determine the grade.
if score >= 90:
    print("Your grade is an A")
elif score >=80 :
     print("Your grade is a B")
elif score >=70 :
     print("Your grade is a C")
elif score >=60 :
     print("Your grade is a D")
else:
    print("Your grade is an F")

x=0
while x<= 5:
    print(x)
    x=x+1

count=7
while count <1:
    print("Hello World")

for county in Counties:
    print(county)

numbers= [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(Counties)):
    print(Counties[i])
    
    
Counties_tuple= ("Arapahoe", "Denver", "Jefferson")

for county in Counties_dict:
    print(county)

for county in Counties_dict.keys():
    print(county)

for voters in Counties_dict.values():
    print(voters)

for county in Counties_dict:
    print(Counties_dict[county])

for county in Counties_dict:
    print(Counties_dict.get(county))

for key, value in Counties_dict.items():
    print(key,value)

for county, voters in Counties_dict.items():
    print(county,voters)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes= int(input("How many votes did you get in the election?"))
total_votes= int(input("What is the total votes in the election?"))
percentage_votes= (my_votes/ total_votes)*100
print(f"I received {my_votes / total_votes *100}% of the total votes.")

Counties_dict={"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in Counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes= int(input("How many votes did the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the election?"))
message_to_candidate=(
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")
print(message_to_candidate)

print(Counties_dict)
amount_voters=(
f"{Counties_dict.keys(1)} county has {Counties_dict.values(1)} registered voters.")


