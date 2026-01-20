import csv


def load_csv():
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return rows


def str_int():
    rows = load_csv()
    for row in rows:
        row["score"] = int(row["score"])
        row["minutes_studied"] = int(row["minutes_studied"])
    return rows

def find_all():
    rows = str_int()
    for row in rows:
        print(row["score"])

def find_the_max():
    rows = str_int()
    stor = []

    for row in rows:
        stor.append(row["score"])
    print(max(stor))


def find_the_min():
    rows = str_int()
    stor = []

    for row in rows:
        stor.append(row["score"])
    print(min(stor))

def find_the_avg():
    rows = str_int()
    stor = []

    for row in rows:
        stor.append(row["score"])
    avg = sum(stor)/len(stor)
    print(avg)
    return avg
def mark_evalution():
    rows = str_int()

    for row in rows:
        if row["score"] >= 80:
            row["Mark_Comment"] = "Excellent"
        elif row["score"] >= 70:
            row["Mark_Comment"] = "Very Good"
        elif row["score"] >= 60:
            row["Mark_Comment"] = "Good"
        elif row["score"] >= 50:
            row["Mark_Comment"] = "Average"
        elif row["score"] >= 40:
            row["Mark_Comment"] = "At Risk"
        elif row["score"] < 40:
            row["Mark_Comment"] = "High Risk"

    return rows
def save_enriched_csv(output_filename="data_enriched.csv"):
    rows = mark_evalution()

    fieldnames = ["student_id", "subject", "score", "minutes_studied", "Mark_Comment"]

    with open(output_filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved: {output_filename}")


save_enriched_csv()