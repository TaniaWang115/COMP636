from sys import argv
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import uuid
import account
import news
import team
import club
import fixture
import grade
isAdmin = 0
memberid = " "
clubid = None

app = Flask(__name__)


def genID():
    return uuid.uuid4().fields[1]

@app.route("/")
def home():
    select_result= account.GetAllMemberNames()
    return render_template('home.html',dbresult=select_result)

@app.route('/member', methods=['GET'])
def member():
    id = request.args.get('memberid')
    select_result = account.GetMemberById(id)
    
    teamId = select_result[5]
    print(teamId)
    if(teamId== None): #teamid = null
        fixturesList = None
    else:
        fixturesList = fixture.GetFixtureById(teamId)
    newsList = news.GetNewsByMemberId(id)
    print(select_result)
    return render_template('member.html',customerdetail = select_result,newslist = newsList,fixturelist = fixturesList)
    

@app.route('/members', methods=['GET'])
def members():
    global isAdmin
    global clubid
    if (request.args.get('admin') == '1'):
        isAdmin = 1
    if clubid ==None:
        clubid = request.args.get('clubid')
    select_result = account.GetAllMembers(False,clubid)
    print(select_result)
    return render_template('members.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/members/active', methods=['GET'])
def membersactive():
    global isAdmin
    global clubid
    select_result = account.GetAllMembers(True,clubid)
    print(select_result)
    return render_template('members.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/member/details', methods=['GET'])
def memberdetails():
    id = request.args.get('memberid')
    select_result = account.GetMemberDetail(id)
    print(select_result)
    return render_template('memberdetails.html',customerdetails = select_result)

@app.route('/member/update', methods=['GET','POST'])
def memberUpdate():
    global isAdmin
    if request.method == 'POST':
        admin = request.args.get('admin')
        id = request.form.get('id')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        account.UpdateMemberDetail(id,firstname,lastname,email,phone,address1,address2,city,birthdate)
        if isAdmin ==0:
            return redirect("/member?memberid={}&admin=0".format(id))
        else:
            return redirect("/members")
    else:
        id = request.args.get('memberid')
        select_result = account.GetMemberDetail(id)
        print(select_result)
        
        return render_template('memberupdate.html',customerdetails = select_result, adminaccess = isAdmin)

@app.route('/member/status', methods=['GET','POST'])
def memberStatus():
    if request.method == 'GET':
        return redirect('/members')
    else:
        id = request.form.get('memberid')
        if (request.form.get('status') == '1'):
            status = 0
        else:
            status = 1
        account.ChangeMembershipStatus(id,status)
        print(request.form)
        return redirect('/members')

#add a new member
@app.route('/member/add', methods=['GET','POST'])
def addMember():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        clubno = request.form.get('clubid')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate,clubno)
        return redirect("/members")
    else:
        global clubid
        select_result = club.GetClubList(clubid)
        print(select_result)
        return render_template('memberadd.html',clublist = select_result)

@app.route('/member/team', methods=['GET','POST'])
def memberaddteam(): 
    if request.method == 'POST':
        memberid = request.form.get('memberid')
        clubNo = request.form.get('clubid')
        teamid = request.form.get('teamid') 
        account.AssignMemberToTeam(memberid,teamid,clubNo)
        return redirect('/members')
    else:
        global clubid
        id = request.args.get('memberid')
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        select_result = team.GetAllTeams(clubid)
        return render_template('memberteam.html', memberId = id, memberName=str(firstname)+" "+str(lastname),dbresult = select_result)


@app.route('/news', methods=['GET'])
def allnews():
    global clubid
    select_result = news.GetNews(clubid)
    return render_template('news.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/news/add', methods=['GET','POST']) 
def addnews(): 
    if request.method == 'GET':
        global clubid
        select_result = club.GetClubList(clubid)
        return render_template('newsadd.html', clublist = select_result) 
    else:
        clubid = request.form.get('clubid')
        header = request.form.get('header')
        newsbyline = request.form.get('newsbyline')
        context =  request.form.get('context')
        news.AddNews(clubid,header,newsbyline, context)
        return redirect("/news")
        

@app.route('/news/details', methods=['GET','POST'])
def newsdetails():
    clubId = request.args.get('clubid')
    if request.method == 'Get':
        select_result = news.GetFristNewsById(clubId)
        return render_template('news.html',dbresult = select_result)
    if request.method == 'POST':
        select_result = news.GetFristNewsById(clubId)
        return render_template('news.html',dbresult = select_result)

@app.route('/teams', methods=['GET'])
def allteams():
    global clubid
    select_result = team.GetAllTeams(clubid)
    return render_template('teams.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/teams/add', methods=['GET','POST'])
def addteams():
    if request.method == 'GET':
        global clubid
        select_result = club.GetClubList(clubid)
        print(select_result)
        grade_result = grade.GetAllGrade()
        return render_template('teamadd.html',clublist = select_result,gradelist=grade_result)
    else:
        teamname = request.form.get('teamname')
        clubid = request.form.get('clubid')
        gradeid = request.form.get('gradeid')
        team.AddTeam(teamname,clubid,gradeid)
        return redirect("/teams")

@app.route('/fixtures', methods=['GET'])
def fixtures():
    global clubid
    select_result = fixture.GetFixtureByClub(clubid)
    return render_template('fixtures.html',dbresult = select_result,adminaccess = isAdmin)  

@app.route('/fixtures/add', methods=['GET','POST'])
def addFixtures():
    if request.method == 'GET':
        gradeId = request.args.get('gradeid')
        if gradeId == None:
            select_result = team.GetAllTeamForFixture()
            grade_result = grade.GetAllGrade()
            print(select_result)
            return render_template('fixtureadd.html',teamlist = select_result, gradelist = grade_result,gradeid= None)
        else:
            select_result = team.GetAllTeamsByGradeId(gradeId)
            grade_result =grade.GetAllGrade()
            print(select_result)
            return render_template('fixtureadd.html',teamlist = select_result, gradelist = grade_result, gradeid=gradeId)
    else:
        hometeamid = request.form.get('hometeamid')
        awayteamid = request.form.get('awayteamid')
        date = request.form.get('date') +" "+ request.form.get('time')+":00"
        fixture.AssignFixture(hometeamid,awayteamid,date)
        return redirect("/fixtures")   

@app.route('/grades', methods=['GET'])
def grades():
    global clubid
    team_result = team.GetAllTeams(clubid)
    date = request.args.get('date')
    if date ==None:
        date='2021-01-01'
        select_result = grade.GetAllGradeEligability(clubid)
    else:
        select_result = grade.GetAllGradeEligabilityBydate(clubid,date)
    print(select_result)
    
    return render_template('grade.html',gradelist = select_result, teamlist=team_result, selectdate=date)