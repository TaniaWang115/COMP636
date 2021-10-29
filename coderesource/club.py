import db

def GetAllClub(clubid):
    sqlCommand= "SELECT * from Clubs where clubid = '{}';".format(clubid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetClubList(clubid):
    sqlCommand= "SELECT clubId,clubName from Clubs where clubid = '{}';".format(clubid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result
