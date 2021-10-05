import db

#get all member
def GetAllMemberNames():
    sqlCommand= "SELECT MemberID, MemberFirstName as FirstName, MemberLastName as LastName, adminaccess from Members;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetAllMembers(IsActive):
    if IsActive:
        sqlCommand= "select MemberID,memberfirstname, memberlastname, clubname, teamname from Members left join Clubs on Members.clubId = Clubs.clubid left join Teams on Teams.teamId = Members.teamid where Members.membershipstatus= 1"
    else:
        sqlCommand= "select MemberID,memberfirstname, memberlastname, clubname, teamname,  membershipstatus from Members left join Clubs on Members.clubId = Clubs.clubid left join Teams on Teams.teamId = Members.teamid "

    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetMemberDetail(memberID):
    sqlCommand = "select MemberId as id,  MemberFirstName, MemberLastName,Email, Phone, Address1, Address2, City, Birthdate from Members where MemberId={};".format(memberID)
    print(f"{sqlCommand}")
    select_result = db.DBOperatorFetchOne(sqlCommand)
    print(f"{select_result}")
    return select_result

def UpdateMemberDetail(memberID,firstname,lastname,email,phone,address1,address2,city):
    sqlCommand = "update Members set memberFirstName =%s, memberlastName =%s,email =%s, phone=%s, address1=%s,address2=%s,city=%s where memberId= %s;",(firstname,lastname,email,phone,address1,address2,city,str(memberID),)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def UpdateMemberStatus(memberID, status):
    sqlCommand = "update Members set membershipstatus =%s where memberId= %s;",(status,str(memberID),)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def DeleteMember(memberID):
    sqlCommand = "delete from Members  where memberId= {};".format(memberID)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate,clubid):
    sqlCommand = "insert into Members (memberfirstname, memberlastname,email, phone,address1,address2,city,birthdate,clubid) values('{}', '{}','{}', '{}', '{}','{}','{}','{}','{}');".format(firstname,lastname,email,phone,address1,address2,city,birthdate,clubid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def AssignMemberToClub(memberID, clubID):
    sqlCommand = "update Members set clubID ={} where memberId= {};".format(clubID,memberID)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def AssignMemberToTeam(memberID, teamID):
    sqlCommand = "update Members set TeamId ={} where memberId= {};".format(teamID,memberID)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result


def ChangeMembershipStatus(memberid,status):
    sqlCommand = "update Members set membershipstatus ={} where memberId= {};".format(status,memberid)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result