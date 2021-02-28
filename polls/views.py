from django.http import HttpResponse
from django.db import connection
from psycopg2._psycopg import cursor


def index(request):
    return HttpResponse("Uvodná stránka kde nič nieje")


def time(request):
    cursor.execute("SELECT date_trunc('second', current_timestamp -pg_postmaster_start_time()) as uptime")
    time = cursor.fetchone()
    return str(time[0])