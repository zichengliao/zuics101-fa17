#   CS 101

##  Course Administration

-   [Course Website, `go.illinois.edu/cs101`](go.illinois.edu/cs101)

-   [Piazza forum](https://piazza.com/class/ipzxix9y8ou155)

-   [CodeLab (`hw01`–`hw06`)](http://www.turingscraft.com/go.html)

-   [Illinois Compass (gradebook)](https://compass2g.illinois.edu/)

### Contact Information

-   `cs101admin@cs.illinois.edu` should be distributed to students and used for necessary email-based communications.

### Responsibilities

-   Neal Davis, instructor:  lectures, labs, midterms, homework, courseware and infrastructure

-   Chelsea Song, course assistant:  operations and scheduling, student exceptions

-   Teaching assistants:  hosting and grading labs, holding office hours, proctoring and grading exams, answering student questions on Piazza forum, other duties as assigned, BEING PREPARED TO ANSWER STUDENT QUESTIONS

-   Course aides:  supporting TAs in lab responsibilities

### Facilities

Foellinger Auditorium:  lectures

2229 Siebel:  Neal Davis' office

2105 Siebel:  Chelsea Song's office

L416 DCL:  student labs

L424 DCL:  TA office

0222 Siebel:  office hours as posted


##  Labs

Students should complete their labs in their own section.  **All exceptions must be approved by Chelsea.**  The deadline for submission is the end of class.  (The real deadline is five minutes after the hour, when a script collects and autogrades assignments.  This is a hard deadline.)

As much of the lab workflow as possible has been automated.  Labs will typically consist of two components:

-   Jupyter notebooks

-   Printed worksheets

Students need to run the following command the first time they log in:

    /class/cs101/startup

This interactive script will ask for the student's section so that they are able to access the correct repository for fetching and submitting assignments.  (This step is not necessary for guest account users.)

CAs will need to modify the `nbgrader_config.py` file in their `cs101-fa16` directory.  Specifically, they need to change the section `AYX` to `OH` on the last line.  This gives them access to the office hours repository where I'll distribute course materials for them to check ahead of time.

Students then access notebooks via the command line by typing `jupyter-notebook`.  Submitted assignments will be automatically retrieved at the hour ending a lab session, so students should submit promptly.  [Walk through this process.]

Labs will be made available to TAs one week beforehand.  You should review and understand the labs, as well as report any difficulties or errors as soon as possible for correction prior to release to students.  Collect hard copies of worksheets from the instructor beforehand.

### Grading

Notebooks are autograded (using `nbgrader`), although worksheets need to be graded by hand.  The instructor will distribute notebook grades to the TAs responsible so that TAs get to know the performance of their individual students and sections.  TAs should take the worksheets with them at the end of their section for grading and return them to students at the beginning of the next lab session.

Although the system will complete autograding (as currently planned), each TA is responsible for extracting and posting grades for his or her section.  The gradebook is a SQLite file located at `/class/cs101/grading/AYX/gradebook.db`, where `AYX` is the section.  More guidance regarding obtaining and processing grades will be made available.

**Grading should be completed and posted online by the subsequent Friday (one week).**  TAs should return notebook feedback to students on the subsequent Friday as well.

**Emergency procedures if labs are unavailable**:

-   Scenario #1:  Labs are locked.  Call EngrIT at 217-333-1313.

-   Scenario #2:  Computer infrastructure is down (home directories unavailable, etc.).  Call EngrIT and notify ND.  Do not dismiss students for at least 15 minutes.

-   Scenario #3:  Labs are unavailable in Jupyter (EWS reset the `atq` script or it otherwise failed).  Slack or text ND immediately at 217-666-1040.  Use `/class/cs101/grading/release AYX lab0X` to release the lab as necessary.

### Resources

TAs have the following resources available to them:

-   A lab help queue, online at [go.illinois.edu/cs101-labq](go.illinois.edu/cs101-labq).  The password to clear this queue or remove single students after they have been helped is `101score`.  If the server goes down, it should restart automatically within a minute unless EWS itself is under preventative maintenance or an outage.

-   Guest accounts `cs101-01` through `cs101-05`.  These will be cleared regularly, so encourage students to save work they wish to keep to their own device or upload the work to Box.  Students will additionally have to run `/class/cs101/startup` for the current section.  The password is `PlsChgMe` and should *not* be told to students.

-   Computers may be logged out by pressing `Ctrl`+`Alt`+`Backspace` if students leave without logging off.


##  Office Hours

Office hours are focused on helping students think critically through problems—homework, approved labs, and general questions.

### Resources

TAs and CAs have the following resources available to them:

-   `set_office_hours netid`  Bash script which sets the student's `nbgrader_config.py` file to pull from the office hours repository, `OH`.  Run this in the student's account before he or she opens Jupyter.

-   `unset_office_hours netid`  Bash script which reverts the student's `nbgrader_config.py` file to pull from their normal section's repository.  Run this from your own account after a student submits their approved office-hour exception work.  Then notify me of the student's NetID so I can collect the assignment for grading.

-   An office hours queue, online at [go.illinois.edu/cs101-ohq](go.illinois.edu/cs101-ohq).  The password to clear this queue or remove single students after they have been helped is `101score`.  If the server goes down, it should restart automatically within a minute unless EWS itself is under preventative maintenance or an outage.

##  Responsibilities of CAs

-   Attend your lab section and support the TA in answering and coordinating student questions.  Do NOT assume TA responsibilities such as lecturing or opening up the lab.

-   Assist with office hours.
