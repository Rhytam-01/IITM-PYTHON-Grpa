def top_k_teams(batsmen: list, k: int) -> list:
    '''
    Given a list of dictionaries with batsman names, runs, and team names,
    create a list with the top k teams in terms of total runs, 
    starting from the highest to the lowest runs.
    
    Arguments:
    batsmen: list of dict - list containing dictionaries with keys 'name', 'runs', and 'team'
    k: int - number of top teams to return

    Return:
    list - top k teams in terms of total runs
    '''
    # Create a dictionary to store total runs per team
    team_runs = {}

    # Accumulate runs for each team
    for batsman in batsmen:
        team = batsman['team']
        runs = batsman['runs']
        
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs
    
    # Sort the teams by total runs in descending order
    sorted_teams = sorted(team_runs.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top k teams
    top_teams = [team for team, _ in sorted_teams[:k]]
    
    return top_teams
