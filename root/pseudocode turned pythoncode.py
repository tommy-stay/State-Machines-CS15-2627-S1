feelings = {"tired", "hungry", "full", "awake"}

state = "coding"

while True:
    if state == "coding":
        print("You are coding!")
        while True:
            feeling = input("How are you feeling? ").strip().lower()
            if feeling in feelings:
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                else:
                    state = "coding"
                break

    elif state == "eating":
        print("You are eating!")
        while True:
            feeling = input("How are you feeling? ").strip().lower()
            if feeling in feelings:
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "full":
                    state = "coding"
                else:
                    state = "sleeping"
                break

    elif state == "sleeping":
        print("You are sleeping!")
        while True:
            feeling = input("How are you feeling? ").strip().lower()
            if feeling in feelings:
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "awake":
                    state = "coding"
                else:
                    state = "sleeping"
                break