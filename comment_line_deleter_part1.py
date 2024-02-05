file = open("part1_from_paste.txt","r")
new_file = open ("part2_comment_line_deleted.txt","a")

for line in file:
    variable=""
    if "#" in line[0]:
        pass
    else:
        new_file.write(line)
     
file.close()
new_file.close()