def process(data):
    # Show readings where temperature change is more than 5 degrees
    return [row for row in data if abs(row[3] - row[4]) > 5]