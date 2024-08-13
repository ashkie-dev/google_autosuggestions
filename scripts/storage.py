import csv


def store_queries(userQuery, answers):
    # with open('.local/previous_queries.csv', 'w', newline='') as csvFile:
    with open('local/previous_queries.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([userQuery, ' || '.join(answers)])
