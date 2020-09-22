def opportunity(yds_gained):
    if yds_gained >= 5:
        return(True)
    else:
        return(False)

def highlight_yds(opportunity, yds_gained):
    if opportunity:
        return(yds_gained - 5)
    else:
        return(None)

def target_rate(player_targets, team_targets):
    return(player_targets/team_targets)

def garbage_time(period, team_score, opp_score):
    if period == 2:
        if abs(team_score - opp_score) > 38:
            return(True)
        else:
            return(False)
    elif period == 3:
        if abs(team_score - opp_score) > 28:
            return(True)
        else:
            return(False)
    elif period == 4:
        if abs(team_score - opp_score) > 22:
            return(True)
        else:
            return(False)
    else:
        return(False)

def line_yards(yds_gained):
    if yds_gained > 10:
        return(7.5)
    elif yds_gained > 5:
        return(4 + (yds_gained-4)/2)
    else:
        return(yds_gained)

def open_field_yds(yds_gained):
    if yds_gained <11:
        return(0)
    else:
        return(yds_gained - 10)

def second_level_yds(yds_gained):
    if yds_gained >= 10:
        return(5)
    elif yds_gained <= 5:
        return(0)
    else:
        return(yds_gained - 5)

def passing_down(yds_to_go, down):
    if down == 2:
        if yds_to_go >= 7:
            return(True)
        else:
            return(False)
    elif down > 2:
        if yds_to_go >= 5:
            return(True)
        else:
            return(False)
    else:
        return(False)

