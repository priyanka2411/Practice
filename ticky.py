#!/usr/bin/env python3
import re
import csv
import operator

errors = {}
users = {}
with open(sys_log.csv,'r') as fil:
    for line in fil:
        username = (re.search(r"\(([\w ]*)\) ", line)).group(1)
        msg = (re.search(r"(ERROR|INFO)", line)).group(1)
        if username not in users:
            user_count = {'INFO': 0, 'ERROR': 0}
            users[username] = user_count
        users[username][msg] += 1
        if msg == 'ERROR':
            err = (re.search(r"ERROR (.*) ", line)).group(1)
            if err not in errors:
                errors = 0
            errors[err] += 1
    fil.close()

user2 = []
error2 = []
for key in sorted(users.keys()):
    user2.append([key, users[key]["INFO"], users[key]["ERROR"]])
for key, value in sorted(errors.items(), key=lambda item: item[1], reverse=True):
    error2.append([key, value])

    user2.insert(0, ["Username", "INFO", "ERROR"])
    error2.insert(0, ["Error", "Count"])

    fe = open("error_message.csv", "w")
    fu = open("user_statistics.csv", "w")

    writer1 = csv.writer(fe)
    writer2 = csv.writer(fu)
    writer1.writerows(error2)
    writer2.writerows(user2)

    fe.close()
    fu.close()

