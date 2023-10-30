def climbingLeaderboard(ranked, player):
    # Write your code here
    # Write your code here
    score_rank = {ranked[0]: 1}
    position = 1
    re_ranked = [ranked[0]]
    result = []
    for score in ranked:
        if score in score_rank:
            continue
        position += 1 
        score_rank[score] = position
        re_ranked.append(score)
    

    for score in player:
        if score in score_rank:
            position = score_rank[score]
            result.append(position)
            continue
        
        while((position > 0) and (re_ranked[position-1] < score)):
            position -= 1
        result.append(position + 1)
    return result
        

a = [100, 90, 90, 80, 75, 60]
b = [50 ,65 ,77 ,90 ,102]

a_1 = [100,100,50,40,40,20,10]
b_1 = [5,25,50,120]
climbingLeaderboard(a, b)