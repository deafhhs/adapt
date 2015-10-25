import csv
from datetime import datetime

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from clients.models import Settings as AdaptSettings
from clients.models import Client


def set_registration_row(reg_client):
    adapt_settings = AdaptSettings.objects.first()
    is_below_poverty = True if reg_client.total_income < \
                               adapt_settings.income_level_1 else False
    is_below_low_income = True if reg_client.total_income < \
                                  adapt_settings.income_level_2 else False
    fields = [
        ('month', datetime.now().strftime('%B %Y'),),
        ('ssn', '',),
        ('vendorid', adapt_settings.AAA_VendorID,),
        ('region', adapt_settings.AAA_Region,),
        ('intake_date', reg_client.intake_date.strftime('%m/%d/%Y'),),
        ('client_last_name', reg_client.last_name,),
        ('first_name', reg_client.first_name,),
        ('mid_init', '',),
        ('client_address', reg_client.address,),
        ('city', reg_client.city,),
        ('state', reg_client.state,),
        ('zip_code', reg_client.zip_code,),
        ('county', adapt_settings.AAA_County,),
        ('township', '',),
        ('phone', export_phone_format(reg_client.phone),),
        ('date_of_birth', reg_client.date_of_birth.strftime('%m/%d/%Y'),),
        ('gender', reg_client.gender,),
        ('lives_alone', bool_to_yes_no(reg_client.lives_alone),),
        ('income_status', bool_to_yes_no(is_below_low_income),),
        ('below_poverty', bool_to_yes_no(is_below_poverty),),
        ('race', reg_client.race,),
        ('multi_racial', bool_to_yes_no(reg_client.multiracial),),
        ('mrwhite', bool_to_yes_no(reg_client.multiracial_white),),
        ('mrblack', bool_to_yes_no(reg_client.multiracial_black),),
        ('mrasian', bool_to_yes_no(reg_client.multiracial_asian),),
        ('mramind', bool_to_yes_no(reg_client.multiracial_amind),),
        ('hispanic', bool_to_yes_no(reg_client.is_hispanic),),
        ('high_nutritional_risk', "No",),
        ('veteran', bool_to_yes_no(reg_client.is_veteran),),
        ('arthritis', '',),
        ('cancer', '',),
        ('diabetes', '',),
        ('heart_disease', '',),
        ('hypertension', '',),
        ('meds_arthritis', '',),
        ('meds_cancer', '',),
        ('meds_diabetes', '',),
        ('meds_heartdisease', '',),
        ('meds_hypertension', '',),
        ('bathing', '',),
        ('bed', '',),
        ('bladder', '',),
        ('bowel', '',),
        ('dressing', '',),
        ('eating_and_feeding', '',),
        ('mobility_level', '',),
        ('stair_climbing', '',),
        ('toileting', '',),
        ('transferring', '',),
        ('walking', '',),
        ('wheeling', '',),
        ('cooking', '',),
        ('laundry', '',),
        ('finances', '',),
        ('heating_hm', '',),
        ('heavy_cleaning', '',),
        ('keep_appt', '',),
        ('light_cleaning', '',),
        ('reheat_meals', '',),
        ('shopping', '',),
        ('medication', '',),
        ('using_phn', '',),
        ('usingprivtrans', '',),
        ('usingpubtrans', '',),
        ('adult_day_care', 'No',),
        ('assmt_cm', 'No',),
        ('assmt_hs', 'No',),
        ('assisted_living', 'No',),
        ('bathing_assistance', 'No',),
        ('congmeals', 'No',),
        ('counseling', 'No',),
        ('dental_exam', 'No',),
        ('dentures', 'No',),
        ('emergency_need', 'No',),
        ('englishseclang', 'No',),
        ('equipment_purchase', 'No',),
        ('fair_housing_services', 'No',),
        ('follow_up', 'No',),
        ('follow_up_diagnostic', 'No',),
        ('foreclosure_intervention_counseling', 'No',),
        ('friendly_visitor', 'No',),
        ('guardianship', 'No',),
        ('health_education', 'No',),
        ('health_education_community', 'No',),
        ('hearingaidassist', bool_to_yes_no(reg_client.hearing_aid_assistance),),
        ('hearing_services___group', 'No',),
        ('hearing_services___individual', bool_to_yes_no(reg_client.hearing_assistance),),
        ('home_chore', 'No',),
        ('home_financial_services', 'No',),
        ('home_modifications_assmt', 'No',),
        ('home_repair_airconditioner', 'No',),
        ('home_repair_major', 'No',),
        ('home_repair_minor', 'No',),
        ('iandr_telephone_211', 'No',),
        ('independent_living', 'No',),
        ('independent_living_individual_coaching', 'No',),
        ('legal_services', 'No',),
        ('literacycomp', 'No',),
        ('ltc_ombud', 'No',),
        ('med_management', 'No',),
        ('monthlymonitoring', 'No',),
        ('outreach_and_assistance', 'No',),
        ('pers', 'No',),
        ('predatory_lending_prevention', 'No',),
        ('reassmt_cm', 'No',),
        ('reassmt_hs', 'No',),
        ('senior_companions', 'No',),
        ('seniorpantry', 'No',),
        ('seniorprojectfresh', 'No',),
        ('stepping_stones', 'No',),
        ('transportation_assisted', 'No',),
        ('transportation_public', 'No',),
        ('vision', 'No',),
        ('vision_rehabilitation', 'No',),
        ('weatherization', 'No',),
        ('ppc', 'No',),
        ('phone_reassurance', 'No',),
        ('adaptive_equipment', bool_to_yes_no(reg_client.adaptive_equipment),),
        ('cglastname', '',),
        ('cgfirstname', '',),
        ('cgss', '',),
        ('cgdob', '',),
        ('cgcounty', '',),
        ('cgaddress', '',),
        ('cgcity', '',),
        ('cgstate', 'MI',),
        ('cgzip', '',),
        ('cgphone', '',),
        ('cgrace', '',),
        ('cggender', '',),
        ('cghispanic', '',),
        ('cgmultiracial', '',),
        ('cglivesalone', '',),
        ('cgpoverty', '',),
        ('cgadl', '',),
        ('crcognitiveimpair', '',),
        ('cgreferralsrc', '',),
        ('cgrelationshipspouse', '',),
        ('cgrelation_dtr', '',),
        ('cgrelation_son', '',),
        ('cgrelation_dtrlaw', '',),
        ('cgrelation_sonlaw', '',),
        ('cgrelation_parent', '',),
        ('cgrelation_grparent', '',),
        ('cgrelaiton_othrel', '',),
        ('cgrelation_nonrelative', '',),
        ('caregivingduration', '',),
        ('carerectraveltime', '',),
        ('cgfreqofcare', '',),
        ('cghandoncare', '',),
        ('cghandoncarefreqtime', '',),
        ('cghanoncarefreqper', '',),
        ('cgemploystatus', '',),
        ('cghealth', '',),
        ('cgothfamily', '',),
        ('cgofrecipients', '',),
        ('cgprimcarerecipients', '',),
        ('cgdependentund19', '',),
        ('cgdependentovr19', '',),
        ('cgdependentovr59', '',),
    ]
    return fields


def set_units_row():
    fields = [
        ('recordtype', "I",),
        ('vendorid', "TODO",), # TODO (singleton)
        ('vendorsite', "TODO",), # TODO (singleton)
        ('regionid', "TODO",), # TODO (singleton)
        ('service_period', "TODO"), # TODO (Use last day of service period (Date MM/DD/YYYY)
        ('ssn', "TODO",), # TODO (client, AAAWM provided ID)
        ('adc_units', '0.00',),
        ('assessment_cmunits', '0.00',),
        ('assessment_hsunits', '0.00',),
        ('bathingassistunits', '0.00',),
        ('counselingunits', '0.00',),
        ('friendlyvisitorunits', '0.00',),
        ('guardianshipunits', '0.00',),
        ('hearingsrvindunits', "TODO",), # TODO (client)
        ('independentlivingunits', '0.00',),
        ('medmanagementunits', '0.00',),
        ('monthlymonitoringunits', '0.00',),
        ('persunits', '0.00',),
        ('reassessment_cmunits', '0.00',),
        ('reassessment_hsunits', '0.00',),
        ('seniorcompanionunits', '0.00',),
        ('seniorpantryunits', '0.00',),
        ('seniorprojectfreshunits', '0.00',),
        ('steppingstonesunits', '0.00',),
        ('visionrehapunits', '0.00',),
    ]
    return fields


def generate_standard_filename(export_type):
    """
    Generates the registration or units filename expected by the upload process.
    export_type will normally be 'REG' or 'UNITS'
    Example: "KCSM DHHS REG Oct2008.txt"
    """
    funding_source = "KCSM"
    provider_name = "DHHS"
    month_and_year = datetime.now().strftime('%b%Y')
    return '-'.join([funding_source, provider_name,
                    export_type, month_and_year]) + '.txt'


def bool_to_yes_no(val):
    return "Yes" if val else "No"

def export_phone_format(phonenumber):
    if phonenumber:
        parts = phonenumber.split('-')
        return '('+parts[0]+')'+parts[1]+'-'+parts[2]
    return ''


@login_required
def registrations(request):
    # Export of all pending registrations as CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + \
                                      generate_standard_filename("REG") + '"'
    reg_clients = Client.objects.all().filter(quota_client=False)\
                                      .filter(napis_id__isnull=True)\
                                      .filter(date_of_death__isnull=True) # TODO add county filter
    data = []
    for client in reg_clients:
        data.append(set_registration_row(client))
    writer = csv.writer(response)
    for row in data:
        writer.writerow([field[1] for field in row])

    return response


@login_required
def units(request):
    # Export of all pending registrations as CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + \
                                      generate_standard_filename("UNITS") + '"'
    data = [set_units_row(),]
    writer = csv.writer(response)
    for row in data:
        writer.writerow([field[1] for field in row])

    return response

class IndexView(TemplateView):
    def get_context_data(self, **kwargs):
        from django.contrib.admin import site
        context = super().get_context_data(**kwargs)
        context.update({
            'site_title': site.site_title,
            'site_header': site.site_header,
            'site_url': site.site_url,
            'has_permission': True,
        })
        return context
