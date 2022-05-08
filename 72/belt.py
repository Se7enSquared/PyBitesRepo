scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    score_zip = zip(scores, belts)
    max_belt =  None
    for belt in list(score_zip):
        if user_score >= int(belt[0]):
            max_belt = belt[1]
            continue
    return max_belt