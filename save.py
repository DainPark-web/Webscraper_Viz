import csv

def save_file(jobs):
    file = open("jbos.csv", mode="w")
    writer = csv.writer(file)

    writer.writerow(["Company", "Location", "Com2"])
    for job in jobs:
        writer.writerow(job.values())
    return 