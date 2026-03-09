__author__= "730748019"

def invert(input: dict[str,str]) -> dict[str, str]:
    """returns a new dictionary with the keys and values inverted"""
    
    inverted: dict[str,str]

    for key in input:
        value: str = input[key]

        if value in inverted:
            raise KeyError("Duplicate value cannot be inverted")
        
        inverted[value] = key

        return inverted
    

def favorite_color(colors: dict[str, str]) -> str:
    """Return the most voted on color in the dictionary"""

    count: dict[str, str] = {}
    
    for name in colors:
        color: str = colors[name]
        
        if color in count:
            count[color] += 1

        else:
            count[color] = 1

    most_common: str = ""
    #Creates an empty string where the most common color will be
    highest: int = 0
    #Stores the largest count of colors seen in the dictionary so far

    for color in count:
        if count[color] > highest:
            highest = count[color]
            most_common = color
        #Checks if the current color appears more times than the current highest
    return most_common

def count(list: str) -> dict[str, int]:
    """Counts the number of times an item is in the list"""
    result: dict[str,int] = {}
    #creates an empty dictionary
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
        #this loops through the list, if the item already exists it adds 1 to the value, if it doesnt it assigns 1 to the value
    return result

def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary that groups words by their starting letter"""
    result: dict[str, list[str]] = {}

    for word in words:
        first_letter: str = word[0].lower()
        #Gets the first letter of the word and converts it to lowercase
        if not first_letter.isalpha():
        #Checks if the input is a letter
            continue
        if first_letter in result:
            result[first_letter].append(word)
            #If the letter already has a list it adds it to the list
        else:
            result[first_letter] = [word]
        
    return result

def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance log with a student's attendance for a given day"""
    if day in log:
        log[day].append(student)
    #If the day exists update the attendance for that day using append
    else:
        log[day] = [student]
    #If the day doesn't exist then create a new list 
