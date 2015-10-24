from django.shortcuts import render
from .reports import Report
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    # List possible reports
    return render(request, 'reports/index.html', {
        'reports': sorted(Report.iterreports(), key=lambda r: r.name),
    })

@login_required
def report_view(request, slug):
    # Find and instantiate an individual report
    rprt = Report.getreport(slug)(request.GET)

    tmpl = rprt.template
    data = rprt.report()

    data['report'] = rprt
    return render(request, 'reports/{}'.format(tmpl), data)
