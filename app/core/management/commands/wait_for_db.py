import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

"""
Django command to wait for the database to be available.
"""

"""
The objective here is to fix possible racing conditions between
Django and the db, in case the db initializes after the Django app
because the app depends on the db to not crash.
"""

"""
The command will run in docker-compose file, before the migrations
and the start of the server.
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
