import db

#Only teams that are of the same grade can play against each other
def AssignFixture(hometeam, awayteam,date):
    sqlCommand = "insert into Fixtures (FixtureDate, Hometeam,AwayTeam) values('{}', '{}','{}');".format(date,hometeam,awayteam)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetFixtureById(teamId):
    sqlCommand = "select f.FixtureID, f.FixtureDate, ht.TeamName as HomeTeamName, ht.Teamid as HomeTeamId,htc.ClubName as HomeTeamClubName,htc.homeground as Place,awt.TeamName as AwayTeamName, awt.Teamid as AwayTeamId,atc.ClubName as AwayTeamClubName from Fixtures as f left join Teams as ht on f.HomeTeam = ht.TeamID left join Teams as awt on f.AwayTeam = awt.TeamID left join Clubs as htc on ht.ClubID = htc.ClubID left join Clubs as atc on awt.ClubID = atc.ClubID where f.Hometeam = '{}' or f.awayteam='{}'".format(teamId, teamId)
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

def GetFixtureByClub(clubid):
    sqlCommand = "select f.FixtureID, f.FixtureDate, ht.TeamName as HomeTeamName, ht.Teamid as HomeTeamId,htc.ClubName as HomeTeamClubName,htc.homeground as Place,awt.TeamName as AwayTeamName, awt.Teamid as AwayTeamId,atc.ClubName as AwayTeamClubName from Fixtures as f left join Teams as ht on f.HomeTeam = ht.TeamID left join Teams as awt on f.AwayTeam = awt.TeamID left join Clubs as htc on ht.ClubID = htc.ClubID left join Clubs as atc on awt.ClubID = atc.ClubID where htc.clubid='{}' or  awt.ClubID ='{}'".format(clubid, clubid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result