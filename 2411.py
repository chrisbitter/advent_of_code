from tqdm import tqdm

with open("2411_input") as file:
    stones = file.readline().strip().split(" ")


# for blink in tqdm(range(25)):
#     new_stones = []

#     for stone in stones:
#         if stone == "0":
#             new_stones.append("1")
#         elif not len(stone) % 2:
#             new_stones.append(stone[: len(stone) // 2])
#             new_stones.append(str(int(stone[len(stone) // 2 :])))
#         else:
#             new_stones.append(str(int(stone) * 2024))

#     stones = new_stones

#     # print(stones)

# print(len(stones))

cache = {}


def split_stone(stone, remaining_blinks=0):
    if not remaining_blinks:
        return 1

    if (stone, remaining_blinks) in cache:
        return cache[(stone, remaining_blinks)]

    if stone == "0":
        result = split_stone("1", remaining_blinks - 1)
    elif not len(stone) % 2:
        stone1, stone2 = stone[: len(stone) // 2], stone[len(stone) // 2 :]
        stone2 = stone2[:-1].lstrip("0") + stone2[-1]

        result = split_stone(stone1, remaining_blinks - 1) + split_stone(
            stone2, remaining_blinks - 1
        )
    else:
        result = split_stone(str(int(stone) * 2024), remaining_blinks - 1)

    cache[(stone, remaining_blinks)] = result

    return result


result1 = sum([split_stone(stone, 25) for stone in stones])
print(result1)

result2 = sum([split_stone(stone, 75) for stone in stones])
print(result2)
