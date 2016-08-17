#   CS 101 Course Administration

-   [Course Website](go.illinois.edu/cs101)

-   [Piazza forum](https://piazza.com/class/ipzxix9y8ou155)

-   [CodeLab (`hw01`–`hw06`)](http://www.turingscraft.com/go.html)

-   [Illinois Compass (gradebook)](https://compass2g.illinois.edu/)


### Contact Information

-   Slack channel [`cs101-fa16`](https://cs101-fa16.slack.com) is preferred for course-related discussions.

-   `cs101admin@cs.illinois.edu` should be distributed to students and used for necessary email-based communications.


### Responsibilities

Neal Davis, instructor:  lectures, labs, homework, courseware and infrastructure

Chelsea Song, course assistant:  operations and scheduling, student exceptions

Teaching assistants:  operating labs, grading, holding office hours, proctoring exams, answering student questions on Piazza forum, duties as assigned

Course aides:  supporting TAs in lab responsibilities


### Facilities

L416 DCL:  student labs

L424 DCL:  TA office (ND has physical key; we'll work out procedure for use)

TBD:  office hours starting week 6 of class


##  Labs

Students should complete their labs in their own section.  **All exceptions must be approved by Chelsea.**

As much of the lab workflow as possible has been automated.  Labs will typically consist of two components:

-   Jupyter notebooks

-   Printed worksheets

Students will need to run the following command the first time they log in:

    /class/cs101/setup

This interactive script will ask for the student's section so that they are able to access the correct repository for fetching and submitting assignments.  (This step is not necessary for guest account users.)

Students then access notebooks via the command line by typing `jupyter-notebook`.  Submitted assignments will be automatically retrieved at the hour ending a lab session, so students should submit promptly.

Labs will be made available to TAs one week beforehand.  You should review and understand the labs, as well as report any difficulties or errors as soon as possible for correction prior to release to students.  Collect hard copies of worksheets from the instructor beforehand.

### Grading

Notebooks are autograded (using `nbgrader`), although worksheets need to be graded by hand.  The instructor will distribute notebook grading to responsible TAs so that TAs get to know the performance of their individual students and sections.  TAs should take the worksheets with them at the end of their section for grading.

**Grading should be completed and posted online by the subsequent Friday (one week).**  TAs should return notebook feedback to students on the subsequent Friday as well.

### Timeline

| Event | Relative Date |
| ----- | ------------- |
| Lab to TAs | one week before release, Monday (-7) |
| Lab released | Monday (+0) |
| Lab closed | Friday (+4) |
| Autograding complete | few days after closing, Wednesday (+9) |
| Hand grading complete | few days after closing, Wednesday (+9) |
| Grades posted | one week after closing, Friday (+11) |
| Feedback returned to students | one week after closing, Friday (+11) |

### Resources

TAs have the following resources available to them:

-   A lab help queue, online at [go.illinois.edu/cs101-labq](go.illinois.edu/cs101-labq).  The password to clear this queue or remove single students after they have been helped is `101score`.  If the server goes down, it should restart automatically within a minute unless EWS itself is under preventative maintenance or an outage.


##  Office Hours

Office hours are focused on helping students think critically through problems—homework, approved labs, and general questions.

### Resources

TAs have the following resources available to them:

-   `set_office_hours netid`  Bash script which sets the student's `nbgrader_config.py` file to pull from the office hours repository, `OH`.  Run this from your own account before a student loads Jupyter.

-   `unset_office_hours netid`  Bash script which reverts the student's `nbgrader_config.py` file to pull from their normal section's repository.  Run this from your own account after a student submits their approved office-hour exception work.

-   Guest accounts `cs101-01` through `cs101-05`.  These are cleared regularly, so encourage students to save work they wish to keep to their own device or upload the work to Box.

-   An office hours queue, online at [go.illinois.edu/cs101-ohq](go.illinois.edu/cs101-ohq).  The password to clear this queue or remove single students after they have been helped is `101score`.  If the server goes down, it should restart automatically within a minute unless EWS itself is under preventative maintenance or an outage.

##  Forum

TAs will be assigned hours of responsibility for responding to student questions on Piazza.
