state = "Locked"

while True:
    print(f"Current state: {state}")

    if state == "Locked":
        print("Your phone is locked.")
        print("Options: 'password' (unlock), 'hack' (hack the phone)")
        action = input("Choose what you want to do: ").strip().lower()

        if action == "password":
            state = "Unlocked"
        elif action == "hack":
            state = "Alarm"
        else:
            print("Not an option, the phone is still locked!")

    elif state == "Unlocked":
        print("Your phone is unlocked.")
        print("Options: 'Off' (phone lock), 'steal' (open bank account)")
        action = input("Choose what you want to do: ").strip().lower()

        if action == "off":
            state = "Locked"
        elif action == "steal":
            state = "bank"
        else:
            print("Not an option, the phone remains open!")
    elif state == "Alarm":
        print("ALARM TRIGGERED! DEACTIVATE OR PHONE WILL SELF-DESTRUCT!!!")
        print("Options: 'deactivate' (shut down phone), 'ignore' (self-destruct)")
        action = input("Choose what you want to do: ").strip().lower()

        if action == "deactivate":
            state = "Locked"
        elif action == "ignore":
            state = "self-destruct"
        else:
            print("Not an option, the phone alarm is going off! Make a choice quickly!")

    if state == "self-destruct":
        print("The phone is going to blow up! Take cover!")
        print("3")
        print("2")
        print("1")
        print("💥💥💥💥💥")
        print("Just kidding. The phone isn't programmed to blow up but the cops are coming.")
        print("Have fun in jail! 🚓🚓🚓")
        break
    if state == "bank":
        print("Bank account open. Face ID required.")
        print("Options: 'face id' (try), 'hack' (alarm)")
        action = input("Choose what you want to do: ").strip().lower()

        if action == "face id":
            print("Face ID not recognized. Locking phone.")
            state = "Locked"
        elif action == "hack":
            state = "Alarm"