guest_list = ['Chen Yi', 'Na Yina', 'Liu Bo']

message1 = "Morning abstract star! " + guest_list[0] + ", welcome to the hell."
message2 = "Morning abstract star! " + guest_list[1] + ", welcome to the hell."
message3 = "Morning abstract star! " + guest_list[2] + ", welcome to the hell."

print(message1)
print(message2)
print(message3)
print(guest_list[0] + " can't attend because of merriage.")

del guest_list[0]
guest_list.insert(0,"Xiu Cai")
print(guest_list)

print("I found a bigger tabel, we can invite more celebarities.")
guest_list.insert(0,"Mr. Milk Shake")
guest_list.insert(1,"Adam Scott")
guest_list.append("Britt Lower")
print(guest_list)

message1 = "Morning abstract star! " + guest_list[0] + ", welcome to the hell."
message2 = "Morning abstract star! " + guest_list[1] + ", welcome to the hell."
message3 = "Morning abstract star! " + guest_list[2] + ", welcome to the hell."
message4 = "Morning abstract star! " + guest_list[3] + ", welcome to the hell."
message5 = "Morning abstract star! " + guest_list[4] + ", welcome to the hell."
message6 = "Morning abstract star! " + guest_list[5] + ", welcome to the hell."
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

print("Sorry to say I don't have enough money to buy tables, so we can only invite 2 guests.")
poped_guest_list = guest_list.pop()
print ("I'm so sorry, " + poped_guest_list + ", please get out of the hell.")
poped_guest_list = guest_list.pop()
print ("I'm so sorry, " + poped_guest_list + ", please get out of the hell.")
poped_guest_list = guest_list.pop()
print ("I'm so sorry, " + poped_guest_list + ", please get out of the hell.")
poped_guest_list = guest_list.pop()
print ("I'm so sorry, " + poped_guest_list + ", please get out of the hell.")
print(guest_list)

Lucky_guy1 = guest_list[0]
Lucky_guy2 = guest_list[1]
print("Hi, " + Lucky_guy1 +", you are lucky enough to have lunch with us in the hell.")
print("Hi, " + Lucky_guy2 +", you are lucky enough to have lunch with us in the hell.")
print(guest_list)

del guest_list[0]
del guest_list[-1]
print(guest_list)

print(len(guest_list))



