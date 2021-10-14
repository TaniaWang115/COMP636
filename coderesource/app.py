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
isAdmin = "0"
memberid = " "


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
    select_result = account.GetMemberDetail(id)
    teamId = select_result[10]
    print(teamId)
    if(teamId== ""): #teamid = null
        fixtureslist = None
    else:
        fixturesList = fixture.GetFixtureById(teamId)
    newsList = news.GetNewsByMemberId(id)
    
    print(select_result)
    return render_template('member.html',customerdetail = select_result,newslist = newsList,fixturelist = fixturesList)
    

@app.route('/members', methods=['GET'])
def members():
    global isAdmin
    if (request.args.get('admin') == '1'):
        isAdmin = "1"
    select_result = account.GetAllMembers(False)
    print(select_result)
    return render_template('members.html',dbresult = select_result,adminaccess = isAdmin)


@app.route('/member/update', methods=['GET','POST'])
def memberUpdate():
    if request.method == 'POST':
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
        return redirect("/member?memberid={}".format(id))
    else:
        id = request.args.get('memberid')
        select_result = account.GetMemberDetail(id)
        print(select_result)
        return render_template('memberupdate.html',customerdetails = select_result)

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
        clubid = request.form.get('clubid')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate,clubid)
        return redirect("/members")
    else:
        select_result = club.GetClubList()
        print(select_result)
        return render_template('memberadd.html',clublist = select_result)

@app.route('/member/team', methods=['GET','POST'])
def memberaddteam(): 
    if request.method == 'POST':
        memberid = request.form.get('memberid')
        clubid = request.form.get('clubid')
        teamid = request.form.get('teamid') 
        account.AssignMemberToTeam(memberid,teamid,clubid)
        return redirect('/members')
    else:
        id = request.args.get('memberid')
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        select_result = team.GetAllTeams()
        return render_template('memberteam.html', memberId = id, memberName=str(firstname)+" "+str(lastname),dbresult = select_result)


@app.route('/news', methods=['GET'])
def allnews():
    select_result = news.GetNews()
    return render_template('news.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/news/add', methods=['GET','POST']) 
def addnews(): 
    if request.method == 'GET':
        select_result = club.GetClubList()
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
    select_result = team.GetAllTeams()
    return render_template('teams.html',dbresult = select_result,adminaccess = isAdmin)

@app.route('/teams/add', methods=['GET','POST'])
def addteams():
    if request.method == 'GET':
        select_result = club.GetClubList()
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
    select_result = fixture.GetFixture()
    return render_template('fixtures.html',dbresult = select_result,adminaccess = isAdmin)  

@app.route('/fixtures/add', methods=['GET','POST'])
def addFixtures():
    if request.method == 'GET':
        select_result = team.GetAllTeams()
        print(select_result)
        return render_template('fixtureadd.html',teamlist = select_result)
    else:
        hometeamid = request.form.get('hometeamid')
        awayteamid = request.form.get('awayteamid')
        date = request.form.get('date') +" "+ request.form.get('time')+":00"
        fixture.AssignFixture(hometeamid,awayteamid,date)
        return redirect("/fixtures")   

@app.route('/grades', methods=['GET'])
def grades():
    select_result = team.GetAllTeams()
    print(select_result)
    return render_template('fixtureadd.html',teamlist = select_result)