#!/usr/bin/env python3
import csv
import re
from operator import itemgetter

def open_file_lines(file_name)-> list[str]:
    with open(file_name, "r") as file:
        lines = file.readlines()    
    return lines

def save_csv(file_path, data):
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for line in data:
            writer.writerow(line)
    return True


def parse_errors(lines):
    errors = {}
    user_stats = {}
    for line in lines:
        match = re.search(r"ticky: ([A-Z]*) (.*) \((.*)\)", line)
        code , msg, user = match[1], match[2], match[3]
        if code == "ERROR":
            errors[msg] = errors.get(msg, 0) + 1
            user_stats[user] = user_stats.get(user, {})
            user_stats[user][code] = user_stats[user].get(code, 0) + 1
        if code == "INFO":
            user_stats[user] = user_stats.get(user, {})
            user_stats[user][code] = user_stats[user].get(code, 0) + 1 
    values = itemgetter(1)
    keys = itemgetter(0)
    errors = sorted(errors.items(), key=values, reverse=True)
    errors.insert(0,("Error", "Count"))
    user_stats = sorted(user_stats.items(), key=keys)
    user_stats = [
        (
            item[0], item[1]["INFO"], item[1]["ERROR"]
        ) for item in user_stats if "ERROR" in item[1] and "INFO" in item[1]
    ]
    user_stats.insert(0, ("Username", "INFO", "ERROR"))
    save_csv(file_path="Course-2/log-parsing-project/reports/errors.csv", data=errors)
    save_csv(file_path="Course-2/log-parsing-project/reports/user_stats.csv", data=user_stats)
    return

if __name__ == "__main__":
    lines = open_file_lines("Course-2/log-parsing-project/syslog.log")
    parse_errors(lines)    

