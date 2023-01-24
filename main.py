#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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


