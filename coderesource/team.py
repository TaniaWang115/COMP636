import db

def GetAllTeams(clubid):
    sqlCommand= "select teamid,teamname, clubname,Teams.clubid, Grades.gradename, Grades.gradeid , Clubs.homeground from Teams join Clubs on Clubs.clubid = Teams.clubid join Grades on Grades.gradeId= Teams.teamgrade where Clubs.clubid={};".format(clubid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetAllTeamForFixture():
    sqlCommand= "select teamid,teamname, clubname,Teams.clubid, Grades.gradename, Grades.gradeid , Clubs.homeground from Teams join Clubs on Clubs.clubid = Teams.clubid join Grades on Grades.gradeId= Teams.teamgrade "
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetAllTeamsByGradeId(gradeid):
    sqlCommand= "select teamid,teamname, clubname,Teams.clubid, Grades.gradename, Grades.gradeid , Clubs.homeground from Teams join Clubs on Clubs.clubid = Teams.clubid join Grades on Grades.gradeId= Teams.teamgrade where gradeid='{}' ".format(gradeid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def AddTeam(teamname, clubId,gradeid):
    sqlCommand = "insert into Teams (teamname, clubid,teamgrade) values ('{}','{}','{}');".format(teamname,clubId,gradeid)
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