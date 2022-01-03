from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from openpyxl import load_workbook

from .forms import UploadFileForm
from .utils import (
    create_parties,
    create_plannings,
    create_records,
    create_tenderers,
    create_tenders,
    create_awards,
    create_suppliers,
    create_transactions,
    create_items,
    create_milestones,
    create_documents
)

def index(request):
    return render(request, 'ocds_admin/index.html')

class UploadFileView(View):
    def get(self, request):
        return render(request, 'ocds_admin/upload_file.html', {'form': UploadFileForm()})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file'].file
            import_data(file)
            messages.success(request, message="Importation des données effectuée avec succès")
        else:
            messages.warning(request, message="Vérifiez que le fichier est bien de type xlsx")
        return render(request, 'ocds_admin/upload_file.html', {'form': form})

def import_data(filename):
    wb = load_workbook(filename)
    output_message = ""
    records = wb.worksheets[1]
    parties = wb.worksheets[2]
    plannings = wb.worksheets[3]
    tenders = wb.worksheets[4]
    tenderers = wb.worksheets[5]
    awards = wb.worksheets[6]
    suppliers = wb.worksheets[7]
    transactions = wb.worksheets[8]
    documents = wb.worksheets[9]
    items = wb.worksheets[10]
    milestones = wb.worksheets[11]
    create_records(records)
    create_parties(parties)
    create_plannings(plannings)
    create_tenders(tenders)
    create_tenderers(tenderers)
    create_awards(awards)
    create_suppliers(suppliers)
    create_transactions(transactions)
    create_items(items)
    create_milestones(milestones)
    create_documents(documents)
    return output_message
