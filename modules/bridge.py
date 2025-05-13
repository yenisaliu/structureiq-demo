def process(data):
    # Show only readings above threshold
    return [row for row in data if row[2] > 75]  # assuming row[2] is stress