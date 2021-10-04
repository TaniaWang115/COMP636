import db

def GetAllTeams():
    sqlCommand= "select teamid,clubname,teamname from Teams join Clubs on Clubs.clubid = Teams.clubid;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def AddTeamInClub(teamId, clubId):
    sqlCommand = "update Teams set clubId =%s where teamID= %s;",(clubId,str(teamId),)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetTeamGrade(teamId):
    sqlCommand= "SELECT teamgrade from Teams where teamId=%s;",(str(teamId),)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result