import re

def count_word_occurrences_regex(file_path, target_word):
    word_count = 0
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(re.findall(r'\b' + re.escape(target_word) + r'\b', content))
    return word_count




file = open("part2_comment_line_deleted.txt","r")
new_file = open ("part3_cleaned_powershell.txt","a")

for line in file:
    variable=""
    variable=line.split("=")[0].replace("$","").strip()
    if count_word_occurrences_regex("part2_comment_line_deleted-dup.txt", variable) > 1:
        new_file.write(line)
     
file.close()
new_file.close()