PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    new_names = names.readlines()


with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for i in new_names:
        stripped_name = i.strip()
        new_letter = letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)








