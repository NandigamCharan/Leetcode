
def dec_to_bin(dec_num):
    x = int(dec_num)
    if x < 1 or x > 5000:
        return "invalid number"
    b = bin(x)
    return b[2:]


def count(s):
    c = 0
    for i in s:
        if i in holes:
            c += holes[i]
    return c

holes = {
    "A" : 1,
    "B" : 2,
    "D" : 1,
    "O" : 1,
    "P" : 1,
    "Q" : 1,
    "R" : 1
}
# T = count(input())
# H = count(input())
# if T < H:
#     print("Henry wins the game")
# elif T > H:
#     print("Tony wins the game")
# else:
#     print("Equal points")





def validate(s):
    if " " in s:
        return 1
    return 0

def isaWiningWord(s):
    front = set()
    back = set()
    i = 0
    j = len(s) - 1
    while j > i:
        front.add(s[i])
        back.add(s[j])
        i += 1
        j -= 1
    return front == back

s = "meritiemr"
print(isaWiningWord(s))