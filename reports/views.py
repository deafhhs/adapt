from django.shortcuts import render
from .reports import Report

def index_view(request):
    # List possible reports
    return render(request, 'reports/index.html', {
        'reports': sorted(Report.iterreports(), key=lambda r: r.name),
    })

def report_view(request, slug):
    # Find and instantiate an individual report
    rprt = Report.getreport(slug)(request.GET)

    name = rprt.name
    tmpl = rprt.template
    data = rprt.report()

    # TODO: Render tmpl in the standard report frame with the data
    return render(request, 'reports/report.html', {
        'data': data,
    })
