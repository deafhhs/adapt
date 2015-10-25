import csv
import datetime

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def set_registration_row():
    fields = [
        ('month', "TODO",), # TODO (July 2015)
        ('ssn', '',),
        ('vendorid', "TODO",), # TODO (singleton)
        ('region', "TODO",), # TODO (singleton)
        ('intake_date', "TODO",), # TODO (client)
        ('client_last_name', "TODO",), # TODO (client)
        ('first_name', "TODO",), # TODO (client)
        ('mid_init', '',),
        ('client_address', "TODO",), # TODO (client)
        ('city', "TODO",), # TODO (client)
        ('state', "TODO",), # TODO (client)
        ('zip_code', "TODO",), # TODO (client)
        ('county', "TODO",), # TODO (singleton)
        ('township', '',),
        ('phone', "TODO",), # TODO (client)
        ('date_of_birth', "TODO",), # TODO (client)
        ('gender', "TODO",), # TODO (client)
        ('lives_alone', "TODO",), # TODO (client)
        ('income_status', "TODO",), # TODO (client)
        ('below_poverty', "TODO",), # TODO (client)
        ('race', "TODO",), # TODO (client)
        ('multi_racial', "TODO",), # TODO (client)
        ('mrwhite', "TODO",), # TODO (client)
        ('mrblack', "TODO",), # TODO (client)
        ('mrasian', "TODO",), # TODO (client)
        ('mramind', "TODO",), # TODO (client)
        ('hispanic', "TODO",), # TODO (client)
        ('high_nutritional_risk', "TODO",), # TODO (client)
        ('veteran', "TODO",), # TODO (client)
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
        ('hearingaidassist', "TODO",), # TODO (client)
        ('hearing_services___group', 'No',),
        ('hearing_services___individual', "TODO",), # TODO (client)
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
        ('adaptive_equipment', 'TODO',), # TODO (client)
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
    month_and_year = datetime.datetime.now().strftime('%b%Y')
    return '-'.join([funding_source, provider_name,
                    export_type, month_and_year]) + '.txt'


@login_required
def registrations(request):
    # Export of all pending registrations as CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + \
                                      generate_standard_filename("REG") + '"'

    data = [set_registration_row(),]
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