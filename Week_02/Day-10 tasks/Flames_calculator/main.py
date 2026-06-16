name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")

list1 = list(name1)
list2 = list(name2)

# Remove common characters
for ch in name1:
    if ch in list2:
        list1.remove(ch)
        list2.remove(ch)

count = len(list1) + len(list2)

flames = ["F", "L", "A", "M", "E", "S"]

while len(flames) > 1:
    index = (count - 1) % len(flames)

    # remove letter and continue from next position
    flames = flames[index+1:] + flames[:index]

result = flames[0]

mapping = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings"
}

print("Result:", mapping[result])