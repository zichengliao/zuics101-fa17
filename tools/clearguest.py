"""
clearguest.py

Clear personal contents in a guest account.  Backup the information in a secure location.

Compatible with nbgrader for CS 101.
"""

course = 'cs101'
term   = 'fa16'

"""
import argparse
parser = argparse.ArgumentParser(description='Target guest account to clear.')
parser.add_argument('account', metavar='account', type=str, nargs=1,
                   help='the target guest account to be cleared')
                   args = parser.parse_args()
                   """

                   from os import environ
                   try:
                       backup_dir = environ['GUEST_BACKUP_DIR']
                       except KeyError:
                           backup_dir = '/class/%s/tmp/exchange/%s-%s/guests'%(course,course,term)


                           # nbgrader has a standard directory structure that we'll rely on, assuming that
                           # the course is located in the $HOME/course-term directory.

                           # Move the user data recursively to the backup directory.
                           from os.path import join
                           guest_material = join(environ['HOME'], '%s-%s'%(course,term))

                           from shutil import move
                           move(guest_material, backup_dir)
                           from datetime import datetime
                           move(join(backup_dir, '%s-%s'%(course,term)), join(backup_dir, '%s-%s-%s'%(course,term,datetime.utcnow().strftime('%Y-%m-%d %X') )))

