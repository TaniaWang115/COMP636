import db

#Only teams that are of the same grade can play against each other
def AssignFixture(hometeam, awayteam,date):
    sqlCommand = "insert into Fixtures (FixtureDate, Hometeam,AwayTeam) values('{}', '{}','{}');".format(date,hometeam,awayteam)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetFixtureById(teamId):
    sqlCommand = "select fixtureid,fixtureDate, t1.teamname as HomeTeamName, t2.teamname as AwayTeamName, hometeam, awayteam from Fixtures inner join Teams t1 on homeTeam = t1.Teamid left join Teams t2 on awayTeam = t2.teamid where HomeTeam ='{}' or awayteam='{}' and FixtureDate>=CURDATE();".format(teamId,teamId)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetFixture():
    sqlCommand = "select fixtureid,fixtureDate, t1.teamname as HomeTeamName, t2.teamname as AwayTeamName, hometeam, awayteam from Fixtures inner join Teams t1 on homeTeam = t1.Teamid left join Teams t2 on awayTeam = t2.teamid;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result