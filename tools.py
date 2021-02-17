import data_storage as ds
import time


def score_reader(file_name):
    """
    """
    # tracking if this row is odd or even
    i = 0
    # list of score and its date
    scores = 0
    dates = ""
    # tracking score and date
    s_and_d = []
    for row in open(file_name):
        if i % 2 == 0:
            scores = int(row.rstrip("\n"))
        else:
            dates = row
            s_and_d.append([scores, dates])

        i += 1
    return s_and_d


def score_writer(score, file_name):
    """
    """
    # tracking if the row is odd or even
    i = 0
    # list for records
    records = []
    # record from current game
    current_time = time.ctime()
    current_record = [score, current_time + "\n"]
    # append record to records
    records.append(current_record)
    recorded_score = 0
    # read file, extract data, append to records
    for row in open(file_name):
        if i%2 == 0:
            recorded_score = int(row)
        else:
            recorded_time = row
            saved_record = [recorded_score, recorded_time]
            records.append(saved_record)

        i += 1

    # sort records in DECENDING SEQUENCE
    records1 = sorted(records, reverse = True)
    print(records1)
    """i = 0
    while i < len(records1)- 2:
        if records1[i][0] == records1[i + 1][0]:
            a = records1[i]
            records1[i] = records1[i + 1]
            records1[i + 1] = a
        i += 1"""
    processed_records = records1[:-1]


    # open the file,  cover it and write score EXPECT THE LAST ONE
    with open(file_name, "w") as f:
        for record in processed_records:
            for i in record:
                print(i)
                if type(i) == int:
                    f.write(str(i))
                    f.write("\n")
                else:
                    f.write(i)
    # return boolean depending on if the score is the LAST ONE
    if processed_records[-1] == current_record:
        return False
    else:
        return True

# testing

#print(score_reader("score.txt"))
#score_writer(1000, "score.txt")
