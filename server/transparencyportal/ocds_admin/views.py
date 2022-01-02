from django.http.response import HttpResponse
from django.shortcuts import render
from openpyxl import load_workbook

from .utils import (
    create_parties,
    create_plannings,
    create_records,
    create_tenderers,
    create_tenders,
    create_awards,
    create_suppliers,
    create_transactions
)


def import_data_view(request):
    wb = load_workbook("/app/transparencyportal/upload/imports/local_test.xlsx")
    # records = wb.worksheets[1]
    # parties = wb.worksheets[2]
    # plannings = wb.worksheets[3]
    # tenders = wb.worksheets[4]
    # tenderers = wb.worksheets[5]
    # awards = wb.worksheets[6]
    # suppliers = wb.worksheets[7]
    transactions = wb.worksheets[8]
    # create_records(records)
    # create_parties(parties)
    # create_plannings(plannings)
    # create_tenders(tenders)
    # create_tenderers(tenderers)
    # create_awards(awards)
    # create_suppliers(suppliers)
    create_transactions(transactions)
    return HttpResponse("Import done")
