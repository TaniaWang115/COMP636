import db

def GetAllClub():
    sqlCommand= "SELECT * from Clubs;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetClubList():
    sqlCommand= "SELECT clubId,clubName from Clubs;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result
