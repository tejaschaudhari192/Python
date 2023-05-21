import os
import time
import sys


def loadming(fr, msg):
    animation = [
        "[■□□□□□□□□□]",
        "[■■□□□□□□□□]",
        "[■■■□□□□□□□]",
        "[■■■■□□□□□□]",
        "[■■■■■□□□□□]",
        "[■■■■■■□□□□]",
        "[■■■■■■■□□□]",
        "[■■■■■■■■□□]",
        "[■■■■■■■■■□]",
        "[■■■■■■■■■■]",
    ]

    for i in range(10):
        time.sleep(fr)
        sys.stdout.write(f"\r{msg}..." + animation[i % len(animation)])
        sys.stdout.flush()
    print()


MAX_ING = 5

storage = []
num_ing = 0


def is_valid_date(day, month, year):
    if year < 2000 or year > 2023 or month < 1 or month > 12 or day < 1:
        return False

    max_days = 30 if month in [2, 4, 6, 9, 11] else 31
    return day <= max_days


# Execution Start from here
cycle = False
while True:
    if cycle:
        loadming(0.05, "Loading")
    else:
        loadming(0.075, "Loading")

    os.system("cls")
    print(
        """
==========================================================================
    𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 𝓻𝓮𝓼𝓽𝓪𝓾𝓻𝓪𝓷𝓽'𝓼 𝓲𝓷𝓿𝓮𝓷𝓽𝓸𝓻𝔂 𝓶𝓪𝓷𝓪𝓰𝓮𝓶𝓮𝓷𝓽 𝓼𝔂𝓼𝓽𝓮𝓶!
==========================================================================
      
      1. Add new ingredients to your inventory
      2. Remove existing ingredient
      3. View your inventory
      4. exit
      """
    )
    choice = int(input("Enter your Choice :"))
    os.system("cls")

    if choice == 1:
        loadming(0.0351, "Loading")

        while True:
            input_str = input(
                "\nEnter an ingredient name to add to storage (or 'b' to back): "
            )

            if input_str == "b":
                break

            if num_ing >= MAX_ING:
                print(
                    "Storage is full. Removing the oldest ingredient using \
                        the FIFO algorithm."
                )
                oldest_ing = storage[0]

                for i in range(1, MAX_ING):
                    if (
                        storage[i]["year"] < oldest_ing["year"]
                        or (
                            storage[i]["year"] == oldest_ing["year"]
                            and storage[i]["month"] < oldest_ing["month"]
                        )
                        or (
                            storage[i]["year"] == oldest_ing["year"]
                            and storage[i]["month"] == oldest_ing["month"]
                            and storage[i]["day"] < oldest_ing["day"]
                        )
                    ):
                        oldest_ing = storage[i]

                print(
                    f"\nRemoving {oldest_ing['name']} from storage \
                        (added on {oldest_ing['day']}/\
                            {oldest_ing['month']}/{oldest_ing['year']})\n"
                )
                loadming(0.05, "loading")
                print()
                storage = storage[1:]
                num_ing -= 1

            # To check availability
            available = False
            for i in storage:
                if input_str == i["name"]:
                    available = True
                    break

            if available == False:
                new_ing = {}
                new_ing["name"] = input_str

                while True:
                    input_str = input(
                        f"Enter the date when {new_ing['name']} \
                            was added to storage (DD/MM/YYYY): "
                    )
                    try:
                        day,month,year = map(int,input_str.split("/"))
                        if is_valid_date(day, month, year):
                            new_ing["day"] = day
                            new_ing["month"] = month
                            new_ing["year"] = year
                            break
                        else:
                            print("The date you entered is not valid.")
                    except ValueError:
                        print(
                            "Invalid date format, please enter \
                                date in format DD/MM/YYYY"
                        )

                storage.append(new_ing)
                num_ing += 1
            else:
                print("Ingredient was already in storage")

    if choice == 2:
        if num_ing < 1:
            print("Storage is Empty")
            break

        input_str = input(
            "\nEnter an ingredient name to remove from storage \
                (or 'b' to back): "
        )
        if input_str == "b":
            break
        else:
            available = False
            for i in storage:
                if input_str == i["name"]:
                    storage.remove(i)
                    available = True
                    break
            if available == True:
                print("\tIngredient removed")
                num_ing -= 1
            else:
                print("\tnot found")

    if choice == 3:
        loadming(0.05, "Loading")
        # print(storage)
        if num_ing != 0:
            print("\nStorage contents:")
            for ingredient in storage:

                print(
                    f"\t\"{ingredient['name']}\" added on \
                        {ingredient['day']}/{ingredient['month']}/\
                            {ingredient['year']}"
                )
        else:
            print("\nStorage Empty")

    if choice == 4:
        loadming(0.075, "Exiting")
        break

    x = input("\nEnter any key to continue...")
    cycle = True
