import db

def GetAllGrade():
    sqlCommand= "select * from Grades;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result