from django.http import HttpResponse
from django.db import connection
from psycopg2._psycopg import cursor


def index(request):
    return HttpResponse("homepage")


def time(request):
    cursor.execute("SELECT date_trunc('second', current_timestamp -pg_postmaster_start_time()) as uptime")
    time = cursor.fetchone()
    time[0]