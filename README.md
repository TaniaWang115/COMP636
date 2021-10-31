# COMP636 Report
## route & functions
Route | Function| Description
------------ | -------------| -------------
/ | home()| Active member selects their name from the drop-down list
/member | member()|Shows latest three news announcements,the upcoming fixtures for the team the member plays for, user's detail
/members | members() | show all the members in this club
/members/active | membersactive()| change the status    
/member/details | memberdetails()  | show the member's detail
/member/update | memberUpdate() | update the member's detail
/member/status | memberStatus(）| list the active members
/member/add | addMember()  | add a new member
/member/team | memberaddteam() | assign a member to a team
/news | allnews() | list all the new which belongs to the club
/news/add  | addnews()| add a new news
/news/details | newsdetails()   | news details
/teams  | allteams() | list all the teams in this club
/teams/add  | addteams() | add a new team into this club
/fixtures | fixtures() | list all the club's fixture 
/fixtures/add   | addFixtures()  | add a new fixture
/grades  | grades()  | list all the grade eligibility
## assumptions and design decision
For teammember:
> For team members, who can only view and modify their basic information including name, date of birth, email, phone number, and residential address and so on. 
> At the same time, check the fixtures belonging to the team, as well as the news of your own club.
> if using there page to show these, will increase the work
> so here I display all the information on one page, when to the update will share the update page.

For admin:
> Because there are four major parts involved, I set the different parts to different navs, so that different pages can be reached through different navs.
> 
> When it comes to displaying all users, a single button is used to display all currently active users. However, other operations are displayed at the end of each line.
> 
> When assigning a team to a user, because each user can only assign one group, I assume that if the admin wants to reassign a team to the user, this is also feasible, 
>  so my approach is to list all the teams in the current club to be assigned by the admin, and then update The database is fine.
>  
> In the assign fixture, because of the grade limitation, assuming that the admin can see the team of other clubs, my solution is to let the admin choose a different grade,
> andthen select the team through the grade.
> 
> When printing grade ebiligation, the initial value is set to 2021/1/1 for the convenience of users’ query  

      
