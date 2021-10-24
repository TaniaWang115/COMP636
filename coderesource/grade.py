import db

def GetAllGrade():
    sqlCommand= "select * from Grades;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetGradeById(gradeid):
    sqlCommand= "select * from Grades where gradeid ='{}';".format(gradeid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result