import math

with open("2409_input") as file:
    line = file.readline().strip()

print(len(line))

files = line[::2]
spaces = line[1::2]

print(len(files))
print(len(spaces))

total = 0

total = sum([int(file) for file in files])

disk_space = math.ceil(total / 2)

index_front = 0
index_back = len(files)
file_back = None

position = 0
checksum = 0

while files:

    # load a file from front
    file_front, files = int(files[0]), files[1:]

    checksum_ = index_front * ((file_front * position) + math.comb(file_front, 2))
    checksum += checksum_

    # print(index_front, checksum_)

    index_front += 1
    position += file_front

    space, spaces = int(spaces[0]), spaces[1:]

    while space:
        if file_back is None:
            files, file_back = files[:-1], int(files[-1])
            index_back -= 1

        if space >= file_back:
            # file fits in space
            checksum_ = index_back * ((file_back * position) + math.comb(file_back, 2))
            checksum += checksum_

            position += file_back
            space -= file_back
            file_back = None
        else:
            # file does not fit in space
            checksum_ = index_back * ((space * position) + math.comb(space, 2))
            checksum += checksum_

            file_back -= space
            position += space
            space = 0

        # print(index_back, checksum_)


checksum_ = index_back * ((file_back * position) + math.comb(file_back, 2))
checksum += checksum_

print(checksum)

# 1928


with open("2409_input") as file:
    line = file.readline().strip()

# line = "2333133121414131402"

from dataclasses import dataclass
from typing import Optional

@dataclass
class File:
    index: int
    position: int
    file_size: int
    space: int
    prev_file: Optional['File'] = None
    next_file: Optional['File'] = None
    touched: bool = False

first_file = None
last_file = None

for ff in range(math.ceil(len(line) / 2)):
    try:
        file_size, space = map(int, list(line[2 * ff : 2 * ff + 2]))
    except:
        file_size, space = int(line[2 * ff]), 0

    if not first_file:
        file = File(ff, 0, file_size, space)
        
        first_file = file
        last_file = file
    else:
        file = File(ff, last_file.position + last_file.file_size + last_file.space, file_size, space, last_file)
        last_file.next_file = file
        last_file = file
    

file = last_file

while file:
    print(file.index)
    
    prev_file = file.prev_file
    
    if not file.touched:
        
        # attempt to move file
        file_ = first_file
        
        while file_ is not file:
            if file_.space < file.file_size:
                file_ = file_.next_file
                continue
            
            # file fits in space
            
            next_file = file.next_file
            
            # add file to former prev file space
            prev_file.space += file.file_size + file.space
            
            # link former prev and next files
            prev_file.next_file = file.next_file
            
            if file.next_file:
                next_file.prev_file = prev_file
            else:
                last_file = prev_file
                
            # now move the file


            file.next_file = file_.next_file
            file.prev_file = file_
            file.position = file_.position + file_.file_size
            file.space = file_.space - file.file_size
            
            file_.space = 0
            file_.next_file.prev_file = file
            file_.next_file = file
            
            break
        
            
        file.touched = True
                
    file = prev_file

print("#" * 10)

checksum = 0

file = first_file

while file:
    # print(file.file_size, file.space, sep="", end="")
    
    checksum_ = file.index * ((file.file_size * file.position) + math.comb(file.file_size, 2))
    checksum += checksum_
    
    #  checksum_ = index_back * ((file_back * position) + math.comb(file_back, 2))
    
    file = file.next_file
    
print(checksum)
