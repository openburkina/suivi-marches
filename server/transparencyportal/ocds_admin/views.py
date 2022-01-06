from threading import Thread

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
            try:
                import_data(file)
                messages.success(request, message="Importation des données effectuée avec succès")
            except:
                messages.error(request, message="Une erreur est survenue lors de l'importation")
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
    t_records = Thread(target=create_records, args=(records,))
    t_parties = Thread(target=create_parties, args=(parties,))
    t_plannings = Thread(target=create_plannings, args=(plannings,))
    t_tenders = Thread(target=create_tenders, args=(tenders,))
    t_tenderers = Thread(target=create_tenderers, args=(tenderers,))
    t_awards = Thread(target=create_awards, args=(awards,))
    t_suppliers = Thread(target=create_suppliers, args=(suppliers,))
    t_transactions = Thread(target=create_transactions, args=(transactions,))
    t_items = Thread(target=create_items, args=(items,))
    t_milestones = Thread(target=create_milestones, args=(milestones,))
    t_documents = Thread(target=create_documents, args=(documents,))

    t_records.start()
    t_records.join()
    t_parties.start()
    t_parties.join()

    t_plannings.start()
    t_tenders.start()
    t_awards.start()

    t_tenders.join()
    t_tenderers.start()
    t_awards.join()
    t_suppliers.start()

    t_plannings.join()
    t_transactions.start()
    t_items.start()
    t_milestones.start()

    t_milestones.join()
    t_documents.start()

    return output_message
