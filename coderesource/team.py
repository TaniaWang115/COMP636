import db

def GetAllTeams():
    sqlCommand= "select teamid,teamname, clubname,Teams.clubid, Grades.gradename, Grades.gradeid from Teams join Clubs on Clubs.clubid = Teams.clubid join Grades on Grades.gradeId= Teams.teamgrade;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def AddTeam(teamname, clubId,gradeid):
    sqlCommand = "insert into Teams (teamname, clubid,gradeid) values ('{}','{}','{});".format(teamname,clubId)
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