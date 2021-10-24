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
    sqlCommand = """select f.FixtureID, f.FixtureDate, 
	ht.TeamName as HomeTeamName, ht.Teamid as HomeTeamId,
	htc.ClubName as HomeTeamClubName,htc.homeground as Place,
    awt.TeamName as AwayTeamName, awt.Teamid as AwayTeamId,
	atc.ClubName as AwayTeamClubName 
    from Fixtures as f
    left join Teams as ht on f.HomeTeam = ht.TeamID
    left join Teams as awt on f.AwayTeam = awt.TeamID
    left join Clubs as htc on ht.ClubID = htc.ClubID
    left join Clubs as atc on awt.ClubID = atc.ClubID""".replace('\n',' ')
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result