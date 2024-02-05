import sys
from io import StringIO
new_stdout = StringIO()


def capture_exec_output(code):
    original_stdout = sys.stdout
    try:
        new_stdout = StringIO()
        sys.stdout = new_stdout
        exec(code)
        output_string = new_stdout.getvalue()
        return output_string
    finally:
        sys.stdout = original_stdout
        
new_file = open("part5_finalPayload.txt","a")
with open("part4_remove_replace_lines.txt","r") as file:
    lines=file.readlines() 
    
for i in range(len(lines)):
    if ";" in lines[i] and "for" not in lines[i]:
        lines[i]=lines[i].replace(";","\n")
with open("temp.txt","w") as temp_file:
    temp_file.writelines(lines)


cleaned_file=open("temp.txt","r")
for line in cleaned_file:
    if line.endswith("')\n") :
        if line.startswith(" "):
            line = line[1:]
        variable_name=line.split("=")[0]
        variable_name_without_dollar_sign="variable"+variable_name[1:]
        line1="variable"+line[1:].strip()+";print("+variable_name_without_dollar_sign+")"
        hex_vals = capture_exec_output(line1)
        new_file.write(str(variable_name) + "= \"" + str(hex_vals.replace("\n","")) +"\"\n")  
    else:
        new_file.write(line)
        
cleaned_file.close()
new_file.close()
    