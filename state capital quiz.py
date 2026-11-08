# Author: Enrique Vigil
# Date: 11.07.26
# Assignment: Prog Assign_9 - Dictionaries

import random


def main():
    # dictionary: state names are keys and capitals are values
    capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"
    }

    # starts both answer counters at zero
    correct = 0
    incorrect = 0

    # shuffles a list of the states so each is asked once
    states = list(capitals.keys())
    random.shuffle(states)

    print("U.S. State Capitals Quiz")
    print("Please enter the capital, or type 'quit' to stop.\n")

    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()

        # quitting does not count as an incorrect answer
        if answer.lower() == "quit":
            break

        # ignores capitalization when checking the answer
        if answer.lower() == capitals[state].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The capital is {capitals[state]}.\n")
            incorrect += 1

    # displays the final totals
    print("\nQuiz Results")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")


# runs the program.
if __name__ == "__main__":
    main()
