import db

def GetAllGrade():
    sqlCommand= "select * from Grades;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetAllGradeEligability():
    sqlCommand= """select Members.memberid,Members.memberfirstname, Members.memberlastname, teamname, clubname,Teams.teamid, Members.birthdate,Grades.gradename,Grades.GradeMinimumAge,Grades.GradeMaximumAge from Members 
                left join Teams on Members.teamid = Teams.teamid
                left join Clubs on Clubs.clubid = Teams.clubid 
                left join Grades on Grades.gradeId= Teams.teamgrade
                where DATEDIFF('2021-1-1', Members.birthdate)/365 < Grades.GradeMaximumAge and Grades.GradeMinimumAge < DATEDIFF('2021-1-1', Members.birthdate)/365;
                """.replace('\n',' ')
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetAllGradeEligabilityByTeamId(teamId):
    sqlCommand= """select Members.memberid,Members.memberfirstname, Members.memberlastname, teamname, clubname,Teams.teamid, Members.birthdate,Grades.gradename,Grades.GradeMinimumAge,Grades.GradeMaximumAge from Members 
                left join Teams on Members.teamid = Teams.teamid
                left join Clubs on Clubs.clubid = Teams.clubid 
                left join Grades on Grades.gradeId= Teams.teamgrade
                where DATEDIFF('2021-1-1', Members.birthdate)/365 < Grades.GradeMaximumAge and Grades.GradeMinimumAge < DATEDIFF('2021-1-1', Members.birthdate)/365;
                """.replace('\n',' ')
    sqlCommand += (" and teamId = %d", teamId)
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