#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open ("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_the_names = names.readlines()

# only_names = []
# for name in list_of_the_names:
#     name_with_out_new_line = name.strip("\n")
#     only_names.append(name_with_out_new_line)


with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    text = letter.read()
    for name in list_of_the_names:
        file_name = name.strip()
        new_text = text.replace("[name]", file_name)
        with open(f"Output/ReadyToSend/letter_for_{file_name}.txt", mode="w") as file:
            file.write(new_text)



