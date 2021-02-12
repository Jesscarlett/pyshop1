from django.http import HttpResponse
from django.shortcuts import render
from .models import Sheet
from tablib import Dataset
from .admin import SheetResource


#     item = random.choice(items)


def index(request):
    items = Sheet.objects.all()
    return render(request, 'index_sheets.html', {'items': items})

# import and export


def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        sheet_resource = SheetResource()
        dataset = Dataset()
        new_sheets = request.FILES['importData']

        if file_format == 'csv':
            imported_data = dataset.load(new_sheets.read().decode('utf-8'), format='csv')
            result = sheet_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(new_sheets.read().decode('utf-8'), format='json')
            result = sheet_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            sheet_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')


def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        sheet_resource = SheetResource()
        dataset = sheet_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

    return render(request, 'export.html')