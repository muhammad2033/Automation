import pywhatkit 
phone_number = input ("enter the phone number!")
pywhatkit.sendwhatmsg(phone_number,"test", 15 , 59)

# pywhatkit.sendwhatmsg(phone_number,"test the code is correct", 3, 37, 15, True,2)

# for group 

group_id = input (" enter group id: ")
pywhatkit.sendwhatmsg_to_group(group_id, "  test the code is correct", 15, 59)

pywhatkit.sendwhatmsg_to_groups()