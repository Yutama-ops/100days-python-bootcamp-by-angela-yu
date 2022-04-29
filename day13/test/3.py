def redis(operations):
    # Write your code here

    stack = []
    for i in operations:
        command = i.split()
        if command[0] == "push":
            stack.insert(0, int(command[1]))
            # add array
        elif command[0] == "inc":
            if 0 <= i < len(stack):
                stack[int(command[1])] = stack[int(command[1])] + int(command[2])

            # add value
        elif command[0] == "pop":
            stack.pop(0)
            # delete array
        if stack:
            print(stack[0])
        else:
            print("EMPTY")



operations = ["push 4", "push 5", "push 3", "inc 1 2", "push 9"]


print(redis(operations))
























# def redis(operations):
#     # Write your code here
#     stack = []
#     for i in operations:
#         command = i.split()
#         if command[0] == "push":
#             stack.insert(0, command[1])
#             return stack
#             # add array
#         elif command[0] == "inc":
#             if len(stack) > 0:
#                 stack[int(command[1])] += int(command[2])
#                 return stack
#             else:
#                 return stack
#             # add value
#         elif command[0] == "pop":
#             stack.pop(0)
#             return stack
#             # delete array
#         else:
#             stack.insert(0, "EMPTY")
#             return stack