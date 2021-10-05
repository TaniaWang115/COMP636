import db

def GetAllTeams():
    sqlCommand= "select teamid,clubname,teamname from Teams join Clubs on Clubs.clubid = Teams.clubid;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def AddTeamInClub(teamname, clubId):
    sqlCommand = "insert into Teams (teamname, clubid) values ('{}','{}');".format(teamname,clubId)
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