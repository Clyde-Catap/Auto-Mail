
new_list = []

with open("../Mail Merge Project Start/input/Names/invited_names.txt")as file:
    namu = file.readlines()
    for g in namu:
        w = g.strip("'\n'")
        new_list.append(w)


with open("../Mail Merge Project Start/input/letters/starting_letter.txt")as file:
    contents = file.read()

    for gg in new_list:
        x = contents.replace("[name]", f"{gg}")
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/{gg}_letter.txt", mode="w") as file:
            file.write(x)


