from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# {{{ Handles registration of reports
class ReportMeta(type(forms.Form)):
    _reports = {}

    def __new__(mcls, cname, bases, dct, *, name=None, template=None, **kw):
        if name is not None:
            dct['name'] = name
            dct['slug'] = slugify(name)
            dct['template'] = template
        return super().__new__(mcls, cname, bases, dct, **kw)

    def __init__(cls, cname, bases, dct, *, name=None, template=None, **kw):
        super().__init__(cname, bases, dct, **kw)
        if name is not None:
            assert dct['name'] == name
            ReportMeta._reports[dct['slug']] = cls

    def iterreports(cls):
        yield from ReportMeta._reports.values()

    def getreport(cls, slug):
        return ReportMeta._reports.get(slug)

class Report(forms.Form, metaclass=ReportMeta):
    name = None
    slug = None
    template = None
    def report(self):
        """
        Returns vars to hand to the template
        """
        raise NotImplementedError

    def get_field(self, name, default=None):
        """
        Utility method to get the value of a field, if available, default otherwise
        """
        if self.is_bound and self.is_valid() and name in self.cleaned_data:
            return self.cleaned_data[name] or default
        else:
            return default

# }}}

##################
# Actual Reports #
##################
import datetime
from clients.models import Client, Audiologist

class AudiologistReport(Report, name='Audiologist List', template='audiologist.html'):
    year = forms.IntegerField(label='Year', min_value=2000, max_value=2050, required=False)
    month = forms.IntegerField(label='Month', min_value=1, max_value=12, required=False)

    def clean(self):
        if hasattr(self, 'year') ^ hasattr(self, 'month'): # Must have Both or Neither 
            raise ValidationError("Must give both Month and Year, or neither.")

    def report(self):
        today = datetime.date.today()
        year = self.get_field('year', today.year)
        month = self.get_field('month', today.month)

        # FIXME: Should do this in a JOIN
        clients = Client.objects.filter(
            audiologist_referral_date__year=year,
            audiologist_referral_date__month=month
        ).order_by('last_name', 'first_name')

        auds = Audiologist.objects

        cross = {}
        for c in clients:
            if c.audiologist not in cross:
                cross[c.audiologist] = set()
            cross[c.audiologist].add(c)

        data = [(a, sorted(cross.get(a, []))) for a in Audiologist.objects.order_by('name')]

        return {
            'auds': data
        }
