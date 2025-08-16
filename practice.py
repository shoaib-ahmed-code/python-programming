traffic_light = input("Enter light color: ")

if traffic_light.lower() == "green":
    print("You can go now")
elif traffic_light.lower() == "red":
    print("You must stop immediately")
elif traffic_light.lower() == "yellow":
    print("Get ready to stop")
else:
    print("There is no traffic signal")