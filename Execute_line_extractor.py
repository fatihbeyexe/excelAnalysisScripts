counter=0
with open("obfuscated_code","r") as file:
    for line in file:
        if "Execute" in line:
            new_line=line.replace("Execute(","").replace(")&",")&\n").split("\n")
            file1=open("Execute"+str(counter)+".txt","a")
            for lines in new_line:
                part1=0
                part2=0
                #switch case
                if "+CL" in lines:
                    part1=int(lines.split("(")[1].split("+")[0])
                    part2=int(lines.split("&H")[1].split('"')[0],base=16)
                    file1.write(chr(part1+part2))
                    #print(chr(part1+part2))
                elif "-CL" in lines:
                    part1=int(lines.split("(")[1].split("-")[0])
                    part2=int(lines.split("&H")[1].split('"')[0],base=16)
                    file1.write(chr(part1-part2))
                    #print(chr(part1-part2))
                elif "*CL" in lines:
                    part1=int(lines.split("(")[1].split("*")[0])
                    part2=int(lines.split("&H")[1].split('"')[0],base=16)
                    file1.write(chr(part1*part2))
                    #print(chr(part1*part2))
                elif "/CL" in lines:
                    part1=int(lines.split("(")[1].split("/")[0])
                    part2=int(lines.split("&H")[1].split('"')[0],base=16)
                    file1.write(chr(part1//part2))
                    #print(chr(part1//part2))
                elif ")+" in lines:
                    part1=int(lines.split("&H")[1].split('"')[0],base=16)
                    part2=int(lines.split(")")[1])
                    file1.write(chr(part1+part2))
                    #print(chr(part1+part2))
                elif ")-" in lines:
                    part1=int(lines.split("&H")[1].split('"')[0],base=16)
                    part2=int(lines.split(")")[1])
                    file1.write(chr(part1-abs(part2)))
                    #print(chr(part1-abs(part2)))
                elif ")*" in lines:
                    part1=int(lines.split("&H")[1].split('"')[0],base=16)
                    part2=int(lines.split(")")[1])
                    file1.write(chr(part1*part2))
                    #print(chr(part1*part2))
                elif ")/" in lines:
                    part1=int(lines.split("&H")[1].split('"')[0],base=16)
                    part2=int(lines.split(")")[1])
                    file1.write(chr(part1//part2))
                    #print(chr(part1//part2))
            file1.close()
            counter+=1