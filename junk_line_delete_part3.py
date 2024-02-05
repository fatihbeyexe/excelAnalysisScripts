def delete_lines_containing_text(file_path, text_to_delete):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    updated_lines = [line for line in lines if text_to_delete not in line]
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

variable_name=""
file = open("part3_cleaned_powershell.txt","r")
new_file = open ("part4_remove_replace_lines.txt","a")

for line in file:
    new_file = open ("part4_remove_replace_lines.txt","a")
    if "-replace" in line:
        variable_name=line.split("=")[0]
        new_file.close()
        delete_lines_containing_text("part4_remove_replace_lines.txt",variable_name)
    else:
        new_file.write(line)
     
file.close()
new_file.close()
