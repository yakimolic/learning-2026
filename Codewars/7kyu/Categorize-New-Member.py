def open_or_senior(data):
    categories=[]
    for age, rang in data:
        if age >= 55 and rang > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories
