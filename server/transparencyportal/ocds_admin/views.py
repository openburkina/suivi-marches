from django.http.response import HttpResponse
from openpyxl import load_workbook

from django.shortcuts import render

from .utils import create_parties, create_records, create_plannings, create_tenders

def import_data_view(request):
    wb = load_workbook("/app/transparencyportal/upload/imports/local_test.xlsx")
    records = wb.worksheets[1]
    parties = wb.worksheets[2]
    plannings = wb.worksheets[3]
    tenders = wb.worksheets[4]
    # create_records(records)
    # create_parties(parties)
    # create_plannings(plannings)
    create_tenders(tenders)
    return HttpResponse("Import done")
