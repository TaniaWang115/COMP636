import db

#Only teams that are of the same grade can play against each other
def AssignFixture(hometeam, awayteam,date):
    sqlCommand = "insert into Fixtures (FextureDate, Hometeam,AwayTeam) values(%s, %s,%s);",(date,hometeam,awayteam,)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetFixture(teamId):
    sqlCommand = "select * Fixtures where teamId=%s);",(teamId,)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result