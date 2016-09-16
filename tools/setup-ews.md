# set up universal python venv for cs101
cd /class/cs101/etc
mkdir -p /class/cs101/etc/venv/cs101-fa16
cd venv
module load python3
pyvenv cs101-fa16
source /class/cs101/etc/venv/cs101-fa16/bin/activate /class/cs101/etc/venv/cs101-fa16/
    pip install jupyter ipython nbgrader
    pip install numpy scipy matplotlib pandas seaborn sympy nose

    # set up nbgrader, etc. (incl. permissions)
    mkdir -p /class/cs101/etc/venv/cs101-fa16/etc/jupyter
    #cp jupyter_notebook_config.py

    nbgrader extension install --nbextensions=/class/cs101/etc/venv/cs101-fa16/etc/jupyter --symlink --debug
    nbgrader extension activate assignment_list
    nbgrader extension activate assignment_list --ExtensionApp.log_level='DEBUG'

    pip install https://github.com/Anaconda-Server/nbbrowserpdf/archive/master.zip
    python -m nbbrowserpdf.install --enable --nbextensions=/class/cs101/etc/venv/cs101-fa16/etc/jupyter

    pip install jupyter-themer
    jupyter-themer -t serif -c zenburn # neo

    #pip install notebook=4.1 -I  # nbgrader incompatible w/ 4.2 as of April 2016
    ln -s etc/jupyter/assignment_list/ share/jupyter/nbextensions/assignment_list
    ln -s etc/jupyter/create_assignment/ share/jupyter/nbextensions/create_assignment
source deactivate

# fix permissions after all editing is done
chmod -R 755 /class/cs101/etc/venv

# set up sxn-specific exchange dirs
# /class/cs101/tmp/exchange/AYX/cs101-fa16/{inbound, outbound}
mkdir -p AY{A..R}/cs101-fa16/outbound
mkdir -p AY{A..R}/cs101-fa16/inbound
for dir in AY{A..R}
do
    chgrp -R cs101 $dir
    chmod -R 775 $dir
    chmod -R 755 $dir/cs101-fa16
    chmod -R 755 $dir/cs101-fa16/outbound
    chmod -R 733 $dir/cs101-fa16/inbound
done

# set up sxn-specific base repo
cd /class/cs101/etc/sxns
chgrp cs101ta *
git clone git@bitbucket.org:davis68/cs101-fa16.git
for dir in AY{A..R}
do
    cp -r cs101-fa16/* $dir
done
rm -rf cs101-fa16/
# set up nbgrader_config.py
for dir in AY{A..R}
do
    cd $dir
    touch nbgrader_config.py
    echo "c = get_config()" >> nbgrader_config.py
    echo "c.NbGrader.course_id = 'cs101-fa16'" >> nbgrader_config.py
    echo "c.TransferApp.exchange_directory = '/class/cs101/tmp/exchange/$dir'" >> nbgrader_config.py
    cd ..
done
chgrp -R cs101ta AY{A..R}

for dir in AY{A..R}
do
  cd $dir
  mv cs101-fa16/* .
  rm -rf cs101-fa16
  cd ..
done

# pull-all.sh
for dir in AY{A..R}
do
    cd $dir
    git pull
    cd ..
done

# release AYA lab01
cd $1
nbgrader assign $2 --IncludeHeaderFooter.header=source/header.ipynb --IncludeHeaderFooter.footer=source/footer.ipynb --ClearSolutions.enabled=False --force
nbgrader release $2 --force
chmod 755 -R /class/cs101/tmp/exchange/$1/cs101-fa16/outbound/
chgrp cs101 -R /class/cs101/tmp/exchange/$1/cs101-fa16/outbound/
cd -

# collect AYA lab01
cd $1
nbgrader collect $2 --update
cd -

# autograde AYA lab01
cd $1
nbgrader autograde $2
cd -

my process:
bash pull-all.sh
bash assign-release.sh CA lab10

bash assign-release.sh AYH lab9
bash assign-release.sh AYI lab9
bash assign-release.sh AYJ lab9
bash assign-release.sh AYG lab9


I have set up distributions by section.  This means that you are now responsible for making sure that students can access the lab at the beginning of your section.
Your basic process:
`cd /class/cs101/etc/sxns`
`bash assign-release.sh AYA lab1`

EVERY STUDENT NEEDS TO RUN:
`reset_grader AYX`
which is an alias now defined in their `/class/cs101/etc/bashrc` file.  This sets their section to
This only needs to happen once.  I will leave a notice up to this effect throughout the week, but will then remove.  Students who miss this week will still need to do this next week then.

Once students are done at the end of class, you need to run:
`bash collect-deploy.sh AYA lab1`

This may lead to some edge-case handling with swapped sections and make-up labs.  Keep me in the loop on those so I can set things up if necessary.

# bashrc:
# check the sxn of the student and replace nbgrader_config.py with a new one by sxn
#now:
cp /class/cs101/etc/venv/cs101-fa16/etc/jupyter/nbgrader_config.py . 2>/dev/null
chmod -w nbgrader_config.py
#next:
python /class/cs101/etc/sxns/setup_nbgrader.py


# now test with ewsguest and set up actual repo; set up setup101 and bashrc also
- set up repo
    - basic files
    - students in gradebook
    - assignments in gradebook
    - add guest accounts
- set up exchange directory, etc.
- set up bashrc
- test ewsguest
- clear ewsguest

# release labs---set up gradebook first
import datetime
def base(sxn):
    if sxn in [       'AYA', 'AYB', 'AYC']:
        d = datetime.datetime(year=2016, month=8, day=22)
    if sxn in ['AYD', 'AYE', 'AYF', 'AYG']:
        d = datetime.datetime(year=2016, month=8, day=23)
    if sxn in [       'AYH', 'AYI', 'AYJ']:
        d = datetime.datetime(year=2016, month=8, day=24)
    if sxn in ['AYK', 'AYL', 'AYM', 'AYN']:
        d = datetime.datetime(year=2016, month=8, day=25)
    if sxn in ['AYO', 'AYP', 'AYQ', 'AYR']:
        d = datetime.datetime(year=2016, month=8, day=26)
    if sxn in [       'AYD',        'AYK', 'AYO']:
        h = datetime.timedelta(hours= 9)
    if sxn in ['AYA', 'AYE', 'AYH', 'AYL', 'AYP']:
        h = datetime.timedelta(hours=11)
    if sxn in ['AYB', 'AYF', 'AYI', 'AYM', 'AYQ']:
        h = datetime.timedelta(hours=13)
    if sxn in ['AYC', 'AYG', 'AYJ', 'AYN', 'AYR']:
        h = datetime.timedelta(hours=15)
    return d+h

from string import ascii_uppercase as alphabet
sxns = []
for letter in alphabet:
    sxns.append('AY%s'%letter)
    if letter == 'R':
        break

from nbgrader.api import Gradebook
gb = Gradebook('sqlite:///gradebook.db')
for sxn in sxns:
    for assn in range(1,14):
        asst = 'lab%02d'%assn
        base_time = base(sxn)
        mod = 0
        if assn>2:
            mod = 1  # labour day
        if assn>12:
            mod = 2  # thanksgiving break
        due = base_time + datetime.timedelta(days=(assn-1+mod)*7, hours=2, minutes=5)
        print(sxn, asst, due)
        #gb.add_assignment(asst, duedate=due.isoformat())

## above to generate all---this to set for a directory:
import datetime
def base(sxn):
    if sxn in [       'AYA', 'AYB', 'AYC']:
        d = datetime.datetime(year=2016, month=8, day=22)
    if sxn in ['AYD', 'AYE', 'AYF', 'AYG']:
        d = datetime.datetime(year=2016, month=8, day=23)
    if sxn in [       'AYH', 'AYI', 'AYJ']:
        d = datetime.datetime(year=2016, month=8, day=24)
    if sxn in ['AYK', 'AYL', 'AYM', 'AYN']:
        d = datetime.datetime(year=2016, month=8, day=25)
    if sxn in ['AYO', 'AYP', 'AYQ', 'AYR']:
        d = datetime.datetime(year=2016, month=8, day=26)
    if sxn in [       'AYD',        'AYK', 'AYO']:
        h = datetime.timedelta(hours= 9)
    if sxn in ['AYA', 'AYE', 'AYH', 'AYL', 'AYP']:
        h = datetime.timedelta(hours=11)
    if sxn in ['AYB', 'AYF', 'AYI', 'AYM', 'AYQ']:
        h = datetime.timedelta(hours=13)
    if sxn in ['AYC', 'AYG', 'AYJ', 'AYN', 'AYR']:
        h = datetime.timedelta(hours=15)
    return d+h

from nbgrader.api import Gradebook
gb = Gradebook('sqlite:///gradebook.db')
import os
sxn = os.getcwd().split('/')[-1]
for assn in range(1,14):
    asst = 'lab%02d'%assn
    base_time = base(sxn)
    mod = 0
    if assn>2:
        mod = 1  # labour day
    if assn>12:
        mod = 2  # thanksgiving break
    due = base_time + datetime.timedelta(days=(assn-1+mod)*7, hours=2, minutes=5)
    print(sxn, asst, due)
    gb.add_assignment(asst, duedate=due.isoformat())
exit

## use collect-at to gather everything in after 15 minutes:
for sxn in AY{A..R}
do
  cd $sxn
  ./collect-at
  cd -
done
atq | sort -n

## okay, now for the auto-deploy:
#!/bin/bash

lab="lab01"
time="10:45am Aug 22"  #next time, not the current one

git pull
nbgrader assign $lab --IncludeHeaderFooter.header=source/header.ipynb --IncludeHeaderFooter.footer=source/footer.ipynb --ClearSolutions.enabled=False --force
nbgrader release $lab --force
at -f ./collect-at $time
chmod -R 755 /class/cs101/tmp/exchange/$sxn/cs101-fa16/outbound

for sxn in AY{A..R}
do
  cd $sxn
  ./release-at
  cd -
done
atq | sort -n


##


ssh -Y -l davis68 remlnx.ews.illinois.edu
# add lab to gradebook.db if necessary---create a script?
nbgrader assign lab8 --IncludeHeaderFooter.header=source/header.ipynb --IncludeHeaderFooter.footer=source/footer.ipynb --ClearSolutions.enabled=False --force
nbgrader release lab8 --force
chmod 755 -R /class/cs101/tmp/exchange/cs101-fa16/outbound/
chgrp cs101 -R /class/cs101/tmp/exchange/cs101-fa16/outbound/

# nbgrader collect --ExtensionInstallApp.student_id=<Unicode>
nbgrader collect lab1 --update
nbgrader collect lab2 --update
nbgrader collect lab3 --update
nbgrader collect lab4 --update
nbgrader collect lab5 --update
nbgrader collect lab6 --update
nbgrader collect lab7 --update

bash 1_setup_course.sh  # one time only
python3 2_deploy_grading.py lab1  # every time
bash 3_deploy_gb.sh lab1  # one time only
bash assign.sh lab1  # every time
nbgrader autograde lab1
nbgrader formgrade
#nbgrader feedback
python3 4_send_feedback.py lab1

export JUPYTER_CONFIG_DIR=/class/cs101/etc/venv/cs101-fa16/etc/jupyter
JUPYTER_CONFIG_DIR=/usr/etc/jupyter jupyter notebook

touch /class/cs101/etc/venv/cs101-fa16/etc/jupyter/migrated
chmod 644 /class/cs101/etc/venv/cs101-fa16/etc/jupyter/migrated
cp ~/.jupyter/jupyter_notebook_config.json /class/cs101/etc/venv/cs101-fa16/etc/jupyter/
chmod 644 /class/cs101/etc/venv/cs101-fa16/etc/jupyter/jupyter_notebook_config.json
cp -r ~/.jupyter/nbconfig /class/cs01/etc/venv/cs101-fa16/etc/jupyter
chmod 755 /class/cs101/etc/venv/cs101-fa16/etc/jupyter/nbconfig
chmod 666 /class/cs101/etc/venv/cs101-fa16/etc/jupyter/nbconfig/*.json

# Release process:
# fix metadata to Python 3
chmod 777 /class/cs101/tmp
chmod 777 /class/cs101/tmp/exchange
chmod 777 /class/cs101/tmp/exchange/cs101-fa16
chmod 777 /class/cs101/tmp/exchange/cs101-fa16/outbound
chmod 755 /class/cs101/tmp/exchange/cs101-fa16/outbound/lab1
chmod 755 /class/cs101/tmp/exchange/cs101-fa16/outbound/lab1/files
chgrp cs101 -R /class/cs101/tmp/exchange/cs101-fa16/outbound
#nbgrader list --json  # should succeed for guest user

# Bash
pip install bash_kernel
python -m bash_kernel.install

# IRuby
module load ruby/2.3.0
gem install rbczmq --install-dir=/class/cs101/etc/venv/cse/lib/ruby
gem install iruby --install-dir=/class/cs101/etc/venv/cse/lib/ruby
chmod -R 755 /class/cs101/etc/venv/cse

# have to set up database but also have to tell nbgrader for some reason now
for sxn in AY{A..R}
do
echo "c.NbGrader.db_assignments = [dict(name='lab01'),dict(name='lab02'),dict(name='lab03'),dict(name='lab04'),dict(name='lab05'),dict(name='lab06'),dict(name='lab07'),dict(name='lab08'),dict(name='lab09'),dict(name='lab10'),dict(name='lab11'),dict(name='lab12'),dict(name='lab13')]" >> $sxn/nbgrader_config.py
done
for sxn in AY{A..R}
do
echo $(cat nbgrader_config-names.txt) #>> $sxn/nbgrader_config.py
done

