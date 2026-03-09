"""A program to help plan a cozy tea party!"""

__author__: str = "730748019"


def main_planner(guests: int) -> None:
    """Call and produce each output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """This will help us determine the number of teabags needed based on how many people there are"""
    return people * 2


def treats(people: int) -> int:
    """This determines the number of treats based on the number of people attending"""
    teas: int = tea_bags(people=people)
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
