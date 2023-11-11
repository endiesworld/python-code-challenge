from collections import OrderedDict

def main():
    sport_team = [("Royals", (18, 12)), ("Rockers", (24,6)), ("Cardinals", (20,10)),
                  ("Dragorns",(22, 8)), ("Kings", (15, 15)), ("Chargers", (20,10)), 
                  ("Jets", (16, 14)), ("Warriors", (25,5))
                  ]                                   
    
    # sort the teams by number of wins revere True means sort in Descending order
    sorted_teams = sorted(sport_team, key=lambda team: team[1][0], reverse=True)  
    
    # sort the teams by number of wins
    sorted_teams_2 = sorted(sport_team, key=lambda team: team[1][0], reverse=False)  
    # print(f"Sorted Team with reverse True {sorted_teams_2}")
    
    print("***************** Sorted Teams ****************")
    print(sorted_teams)
        
    teams = OrderedDict(sorted_teams)
    print("************** OrderedDict team *******************")
    print(teams)
    
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd':4}
    
    my_dict_2 = {'a': 1, 'b': 2, 'c':3, 'd':4}
    
    my_list = [1,2,3,4]
    my_list_2 = [1,2,3,4]
    
    print(f" distionary_1 == distionary_2: {my_dict == my_dict_2}")
    print(f" my_list_1 == my_list_2: {my_list == my_list_2}")

if __name__ == '__main__':
    main()