from django.http import HttpResponse
import json
from django.db import connection
from psycopg2._psycopg import cursor


def index(request):
    return HttpResponse("Uvodná stránka kde nič nieje")

def time(request):
    query = "SELECT date_trunc('second', current_timestamp - pg_postmaster_start_time()) as uptime;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        time = cursor.fetchone()
        current_time = { "pgsql": { "uptime": str(time[0]) } }
    return HttpResponse(current_time, content_type='application/json')