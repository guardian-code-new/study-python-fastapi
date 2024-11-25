# test_list = [1, 2, 3, 4, 5, 6]
#
# for num in test_list:
#     print(num ** 2)
# delete

# test_list = [1, 2, 3, 4, 5]
#
# while len(test_list) < 10:
#     test_list.append(3)
#     print(test_list)
# delete

# test_list = ["test", "python", "code"]
#
# for s in test_list:
#     print(s, "--<")
#     if s == "test":
#         print(s)
#     elif s == "python":
#         print(s)
#     else:
#         print(s)
# delete

a = 0
add_list = []

while len(add_list) < 10:
    add_list.append(a)
    a += 1
    if len(add_list) == 5:
        print("You are at middle of list")
