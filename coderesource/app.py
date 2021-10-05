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
    print(select_result)
    return render_template('memberdetails.html',customerdetails = select_result)
    

@app.route('/members', methods=['GET'])
def members():
    select_result = account.GetAllMembers(False)
    print(select_result)
    return render_template('members.html',dbresult = select_result)


@app.route('/member/update', methods=['GET','POST'])
def memberUpdate():
    if request.method == 'POST':
        print(request.form)
        return render_template('dbresult.html',"dbresult","column_names")
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
    id = request.args.get('memberid')
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate)
        return render_template('dbresult.html',"dbresult","column_names")
    else:
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        select_result = club.GetAllClub()
        return render_template('memberteam.html', memberId = id, memberName=str(firstname)+" "+str(lastname),dbresult = select_result)


@app.route('/news', methods=['GET'])
def allnews():
    select_result = news.GetNews()
    return render_template('news.html',dbresult = select_result)

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
    return render_template('teams.html',dbresult = select_result)

@app.route('/teams/add', methods=['GET','POST'])
def addteams():
    if request.method == 'GET':
        select_result = club.GetClubList()
        print(select_result)
        return render_template('teamadd.html',clublist = select_result)
    else:
        teamname = request.form.get('teamname')
        clubid = request.form.get('clubid')
        
        team.AddTeamInClub(teamname,clubid)
        return redirect("/teams")

@app.route('/fixtures', methods=['GET'])
def fixtures():
    select_result = fixture.GetFixture()
    return render_template('fixtures.html',dbresult = select_result)  

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