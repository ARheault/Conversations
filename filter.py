import os

users = []
topics = []
values = []
flag = False
conversations = []
for elem in os.listdir():
    if elem[-3:] == "txt":
        conversations.append(elem)

for conversation in conversations:
    textData = open(conversation, "r+")
    val = []
    for line in textData.readlines():
        val.append(line[:-1].split(":"))
    values.append(val)

for conversation in values:
    for val in conversation:
        for elem in users:
            if val[0] == elem[0]:
                flag = True
                elem.append(val[1])
                break
        if not flag:
            users.append(val)
        flag = False

# Build user directory if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), "Users")):
    os.mkdir(os.path.join(os.path.getcwd(), "Users"))

# Build topic directory if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), "Topics")):
    os.mkdir(os.path.join(os.path.getcwd(), "Topics"))

# Read into each user
for user in users:
    file = ""
    # If user exists already, lets append to their saved data
    if os.path.exists(os.path.join(os.getcwd(), "Users/" + user[0] + ".txt")):
        file = open("./Users/" + user[0] + ".txt", "a+")
    # Otherwise build a fild for them
    else:
        file = open("./Users/" + user[0] + ".txt", "w+")
    file.write("\n".join(user[1:]) + "\n")
    file.close()

# This is not done yet.
# Read into each topic
for topic in topics:
    file = ""
    # If topic exists already, lets append to their saved data
    if os.path.exists(os.path.join(os.getcwd(), "Topics/" + topic[0] + ".txt")):
        file = open("./Topics/" + topic[0] + ".txt", "a+")
    # Otherwise build a fild for them
    else:
        file = open("./Topics/" + topic[0] + ".txt", "w+")
    file.write("\n".join(topic[1:]) + "\n")
    file.close()
