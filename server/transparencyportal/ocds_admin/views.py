from django.http.response import HttpResponse
from openpyxl import load_workbook

from django.shortcuts import render

from .utils import create_parties, create_records, create_plannings

def import_data_view(request):
    wb = load_workbook("/app/transparencyportal/upload/imports/local_test.xlsx")
    records = wb.worksheets[1]
    parties = wb.worksheets[2]
    plannings = wb.worksheets[3]
    create_records(records)
    create_parties(parties)
    create_plannings(plannings)
    return HttpResponse("Import done")
