from ocds_master_tables.models import (
    Address,
    Budget,
    ContactPoint,
    Entity,
    Identifier,
    Period,
    Projet,
    Value,
)
from ocds_planning.models import Planning
from ocds_release.models import Record, Release, Target
from ocds_tender.models import Tender
from openpyxl import worksheet

# def compare_and_update(incoming_data, db_data, model):
#     if not isinstance(incoming_data, model) or not isinstance(db_data, model):
#         raise Exception('Data instances must be instance of %s' % model)
#     for (field_name, value) in incoming_data.__dict__.items():
#         if not (field_name == '_state' or field_name == 'id'):
#             setattr(db_data, field_name, value)
#     db_data.save()

def set_related_fields(db_instance, related_fields: list):
    """
    fields : List of tuple (field_name, incoming_object)
    """
    for field in related_fields:
        if not getattr(db_instance, field[0]):
            setattr(db_instance, field[0], field[1])
        else:
            to_delete = getattr(db_instance, field[0])
            setattr(db_instance, field[0], field[1])
            db_instance.save()
            to_delete.delete()
    db_instance.save()

def create_records(ws: worksheet):
    key_map = {
        "ocid": 0,
        "target": 1,
        "address_country": 2,
        "address_region": 3,
        "address_locality": 4,
        "address_postalcode": 5,
        "address_longitude": 6,
        "address_latitude": 7
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        incoming_address = Address.objects.create(
            country_name=flat_object[key_map["address_country"]],
            region=flat_object[key_map["address_region"]],
            locality=flat_object[key_map["address_locality"]],
            postal_code=flat_object[key_map["address_postalcode"]],
            locality_longitude=flat_object[key_map["address_longitude"]],
            locality_latitude=flat_object[key_map["address_latitude"]]
        )
        incoming_target = Target.objects.create(name=flat_object[key_map["target"]])
        try:
            record = Record.objects.get(ocid=flat_object[key_map["ocid"]])
            related_fields = [
                ('implementation_address', incoming_address),
                ('target', incoming_target),
            ]
            set_related_fields(record, related_fields)
        except Record.DoesNotExist:
            record = Record(
                ocid=flat_object[key_map["ocid"]],
                implementation_address=incoming_address,
                target=incoming_target
            )
        try:
            record.compiled_release
        except:
            release = Release.objects.create(
                ref_record=record,
                tag=["planning"]
            )
            release.save()
        record.save()

def create_parties(ws: worksheet):
    key_map = {
        "party_id": 0,
        "record_ocid": 1,
        "name": 2,
        "id_schema": 3,
        "id_legal_name": 4,
        "id_uri": 5,
        "address_country": 6,
        "address_region": 7,
        "address_locality": 8,
        "address_postalcode": 9,
        "address_longitude": 10,
        "address_latitude": 11,
        "contact_name": 12,
        "contact_mail": 13,
        "contact_phone": 14,
        "contact_fax": 15,
        "contact_url": 16
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            release = Record.objects.get(ocid=flat_object[key_map["record_ocid"]]).compiled_release
        except:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        incoming_address = Address.objects.create(
            country_name=flat_object[key_map["address_country"]],
            region=flat_object[key_map["address_region"]],
            locality=flat_object[key_map["address_locality"]],
            postal_code=flat_object[key_map["address_postalcode"]],
            locality_longitude=flat_object[key_map["address_longitude"]],
            locality_latitude=flat_object[key_map["address_latitude"]]
        )
        incoming_identifier = Identifier.objects.create(
            scheme=flat_object[key_map["id_schema"]],
            legal_name=flat_object[key_map["id_legal_name"]],
            uri=flat_object[key_map["id_uri"]]
        )
        incoming_contact = ContactPoint.objects.create(
            name=flat_object[key_map["contact_name"]],
            email=flat_object[key_map["contact_mail"]],
            telephone=flat_object[key_map["contact_phone"]],
            fax_number=flat_object[key_map["contact_fax"]],
            url=flat_object[key_map["contact_url"]],
        )
        try:
            entity = Entity.objects.get(pk=flat_object[key_map["party_id"]])
            related_fields = [
                ('address', incoming_address),
                ('identifier', incoming_identifier),
                ('contact_point', incoming_contact),
            ]
            set_related_fields(entity, related_fields)
        except Entity.DoesNotExist:
            entity = Entity(
                pk=flat_object[key_map["party_id"]],
                address=incoming_address,
                identifier=incoming_identifier,
                contact_point=incoming_contact
            )
        entity.name = flat_object[key_map["name"]]
        entity.save()
        release.parties.add(entity)

def create_plannings(ws : worksheet):
    key_map = {
        "record_ocid": 0,
        "planning_id": 1,
        "title": 2,
        "description": 3,
        "rationale": 4,
        "budget_source": 5,
        "budget_amount": 6,
        "budget_currency": 7,
        "budget_uri": 8
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            release = Record.objects.get(ocid=flat_object[key_map["record_ocid"]]).compiled_release
        except:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        incoming_amount = Value.objects.create(
            amount=flat_object[key_map["budget_amount"]],
            currency=flat_object[key_map["budget_currency"]]
        )
        incoming_project = Projet.objects.create(
            titre_projet=flat_object[key_map["title"]],
            description=flat_object[key_map["description"]]
        )
        incoming_budget = Budget.objects.create(
            source=flat_object[key_map["budget_source"]],
            uri=flat_object[key_map["budget_uri"]],
            projet=incoming_project,
            amount=incoming_amount,
            description=flat_object[key_map["rationale"]]
        )
        try:
            planning = Planning.objects.get(pk=flat_object[key_map["planning_id"]])
            related_fields = [
                ('budget', incoming_budget)
            ]
            set_related_fields(planning, related_fields)
        except Planning.DoesNotExist:
            planning = Planning(
                pk=flat_object[key_map["planning_id"]],
                budget=incoming_budget
            )
        planning.raison = flat_object[key_map["rationale"]]
        planning.save()
        release.planning = planning
        release.save()

def create_tenders(ws: worksheet):
    key_map = {
        "record_ocid": 0,
        "tender_id": 1,
        "buyer": 2,
        "procuring_entity": 3,
        "title": 4,
        "description": 5,
        "status": 6,
        "procurement_method": 7,
        "procurement_method_rationale": 8,
        "award_criteria": 9,
        "award_criteria_details": 10,
        "submission_method": 11,
        "submission_method_details": 12,
        "min_value_amount": 13,
        "min_value_currency": 14,
        "value_amount": 15,
        "value_currency": 16,
        "tender_period_start": 17,
        "tender_period_end": 18,
        "enquiry_period_start": 19,
        "enquiry_period_end": 20,
        "award_period_start": 21,
        "award_period_end": 22,
        "eligibility_criteria": 23,
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            release = Record.objects.get(ocid=flat_object[key_map["record_ocid"]]).compiled_release
        except:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        try:
            buyer_entity = Entity.objects.get(pk=flat_object[key_map["buyer"]])
            print(type(buyer_entity))
        except:
            print("Buyer with id : %s does not exist" % flat_object[key_map["buyer"]])
            continue
        try:
            procuring_entity = Entity.objects.get(pk=flat_object[key_map["procuring_entity"]])
        except:
            print("Entity with id : %s does not exist" % flat_object[key_map["procuring_entity"]])
            continue

        incoming_min_value = Value.objects.create(
            amount=flat_object[key_map["min_value_amount"]],
            currency=flat_object[key_map["min_value_currency"]]
        )
        incoming_value = Value.objects.create(
            amount=flat_object[key_map["value_amount"]],
            currency=flat_object[key_map["value_currency"]]
        )
        incoming_tender_period = Period.objects.create(
            start_date=flat_object[key_map["tender_period_start"]],
            end_date=flat_object[key_map["tender_period_end"]]
        )
        incoming_enquiry_period = Period.objects.create(
            start_date=flat_object[key_map["enquiry_period_start"]],
            end_date=flat_object[key_map["enquiry_period_end"]]
        )
        incoming_award_period = Period.objects.create(
            start_date=flat_object[key_map["award_period_start"]],
            end_date=flat_object[key_map["award_period_end"]]
        )

        try:
            tender = Tender.objects.get(pk=flat_object[key_map["tender_id"]])
            related_fields = [
                ('min_value', incoming_min_value),
                ('value', incoming_value),
                ('tender_period', incoming_tender_period),
                ('enquiry_period', incoming_enquiry_period),
                ('award_period', incoming_award_period),
            ]
            set_related_fields(tender, related_fields)
        except Tender.DoesNotExist:
            tender = Tender(
                pk=flat_object[key_map["tender_id"]],
                min_value=incoming_min_value,
                value=incoming_value,
                tender_period=incoming_tender_period,
                enquiry_period=incoming_enquiry_period,
                award_period=incoming_award_period
            )
        tender.buyer=buyer_entity
        tender.title=flat_object[key_map["title"]]
        tender.description=flat_object[key_map["description"]]
        tender.status=flat_object[key_map["status"]]
        tender.procurement_method=flat_object[key_map["procurement_method"]]
        tender.procurement_method_rationale=flat_object[key_map["procurement_method_rationale"]]
        tender.award_criteria=flat_object[key_map["award_criteria"]]
        tender.award_criteria_details=flat_object[key_map["award_criteria_details"]]
        tender.submission_method=flat_object[key_map["submission_method"]]
        tender.submission_method_details=flat_object[key_map["submission_method_details"]]
        tender.eligibility_criteria=flat_object[key_map["eligibility_criteria"]]
        tender.procuring_entity=procuring_entity
        tender.save()

        release.tender = tender
        release.buyer = buyer_entity
        release.update_buyer_role()
        release.save()


def import_xls(file):



    def create_tenderer(worksheet):
        pass

    def create_award(worksheet):
        pass

    def create_contract(worksheet):
        pass

    def create_implementation(worksheet):
        pass

    def create_supplier(worksheet):
        pass

    def create_transaction(worksheet):
        pass

    def create_document(worksheet):
        pass

    def create_item(worksheet):
        pass

    def create_milestone(worksheet):
        pass
