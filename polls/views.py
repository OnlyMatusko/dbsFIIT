from django.http import HttpResponse
import json
from django.db import connection
from psycopg2._psycopg import cursor


def index(request):
    return HttpResponse("Uvodná stránka kde nič nieje")

def time(request):
    cursor.execute("SELECT date_trunc('second', current_timestamp -pg_postmaster_start_time()) as uptime")
    time = cursor.fetchone()
    return HttpResponse(json.dump(time), content_type='application/json')