# sendfeedback.py assignment
#   assumes nbgrader default file/folder layout inside of sections
#   should be run from tools/ folder

# configuration
import os
class_semester = 'cs101-fa16'
main_path = '/class/cs101/grading'
if not os.path.isdir(main_path):
    print('Path %s not found or not accessible---check permissions.'%exchange_path)

import argparse
parser = argparse.ArgumentParser(description='Send nbgrader feedback HTML files to students.')
parser.add_argument('section', metavar='section', type=str, nargs=1,
                    help='the section')
parser.add_argument('assignment', metavar='assignment', type=str, nargs=1,
                    help='the current assignment')

args = parser.parse_args()
asst = args.assignment[0]
sxn  = args.section[0]

# loop over each section
sxns = ['AYA', 'AYB', 'AYC', 'AYD', 'AYE', 'AYF', 'AYG', 'AYH', 'AYI', 'AYJ', 'AYK', 'AYL', 'AYM', 'AYN', 'AYO', 'AYP', 'AYQ', 'AYR']
if sxn not in sxns:
    raise Exception('Section %s not found.'%sxn)
tas = {}
tas['AYA'] = 'rghosh9'
tas['AYB'] = 'whassan3'
tas['AYC'] = 'rghosh9'
tas['AYD'] = 'atreya2'
tas['AYE'] = 'nsharm11'
tas['AYF'] = 'nsharm11'
tas['AYG'] = 'cliu68'
tas['AYH'] = 'lunanli3'
tas['AYI'] = 'hcheng17'
tas['AYJ'] = 'lunanli3'
tas['AYK'] = 'pampari2'
tas['AYL'] = 'whassan3'
tas['AYM'] = 'atreya2'
tas['AYN'] = 'cliu68'
tas['AYO'] = 'pampari2'
tas['AYP'] = 'bhattad2'
tas['AYQ'] = 'hcheng17'
tas['AYR'] = 'bhattad2'

import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

from random import randint
from time import sleep

# start SMTP server
s = smtplib.SMTP('localhost')

#for sxn in sxns:
sxn_path = os.path.join(main_path, sxn, 'feedback')
# get a list of students who were graded
students = os.listdir(sxn_path)
for student in students:
    student_path = os.path.join(sxn_path, student, asst)
    msg = MIMEMultipart()
    msg['Subject'] = '%s %s:  %s'%(class_semester, asst, student)
    msg['From'] = '%s@illinois.edu'%tas[sxn]
    msg['To'] = '%s@illinois.edu'%(student)
    #msg['Cc'] = '%s@illinois.edu'%(tas[sxn])

    msg.attach(MIMEText('%s %s:  %s'%(class_semester, asst, student)))
    msg.attach(MIMEText('Here is your feedback report for %s.  Please contact me if you have questions.'%asst))

    print('Sending email for %s'%student)

    # grab any html files in feedback/ and attach to email
    print('Attaching files:')
    htmls = glob.glob(os.path.join(student_path, '*.html'))
    for html in htmls:
        print('\t', html)
        with open(html, 'r', encoding='utf-8') as html_stream:
            msg.attach(MIMEApplication(html_stream.read(), Content_Disposition='attachment; filename="%s"'%basename(html), Name=basename(html)))

    # send email to student email address
    print(msg.items())
    sleep(randint(5,20))  # prevent being mistaken as DOS-style attack by randomly varying interval
    s.sendmail('%s@illinois.edu'%student, ['%s@illinois.edu'%student], msg.as_string())

# close SMTP server
s.quit()
