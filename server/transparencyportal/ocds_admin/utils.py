from openpyxl import worksheet
from ocds_master_tables.models import Address, Identifier, ContactPoint, Budget, Value, Projet
from ocds_release.models import Record, Release, Target, ReleaseParty
from ocds_planning.models import Planning

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
        address, address_created = Address.objects.update_or_create(
            country_name=flat_object[key_map["address_country"]],
            region=flat_object[key_map["address_region"]],
            locality=flat_object[key_map["address_locality"]],
            postal_code=flat_object[key_map["address_postalcode"]],
            locality_longitude=flat_object[key_map["address_longitude"]],
            locality_latitude=flat_object[key_map["address_latitude"]]
        )
        address.save()
        target, target_created = Target.objects.update_or_create(
            name=flat_object[key_map["target"]]
        )
        target.save()
        record, record_created = Record.objects.update_or_create(
            ocid=flat_object[key_map["ocid"]],
            target=target,
            implementation_address=address
        )
        record.save()
        try:
            record.compiled_release
        except:
            release = Release.objects.create(
                ref_record=record,
                tag=["planning"]
            )
            release.save()

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
        address, address_created = Address.objects.update_or_create(
            country_name=flat_object[key_map["address_country"]],
            region=flat_object[key_map["address_region"]],
            locality=flat_object[key_map["address_locality"]],
            postal_code=flat_object[key_map["address_postalcode"]],
            locality_longitude=flat_object[key_map["address_longitude"]],
            locality_latitude=flat_object[key_map["address_latitude"]]
        )
        address.save()
        identifier, identifier_created = Identifier.objects.update_or_create(
            scheme=flat_object[key_map["id_schema"]],
            legal_name=flat_object[key_map["id_legal_name"]],
            uri=flat_object[key_map["id_uri"]]
        )
        identifier.save()
        contact, contact_created = ContactPoint.objects.update_or_create(
            name=flat_object[key_map["contact_name"]],
            email=flat_object[key_map["contact_mail"]],
            telephone=flat_object[key_map["contact_phone"]],
            fax_number=flat_object[key_map["contact_fax"]],
            url=flat_object[key_map["contact_url"]],
        )
        contact.save()
        party, party_created = ReleaseParty.objects.update_or_create(
            pk=flat_object[key_map["party_id"]],
            ref_release=release,
            name=flat_object[key_map["name"]],
            identifier=identifier,
            address=address,
            contact_point=contact
        )
        party.save()

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
        amount = Value.objects.create(
            amount=flat_object[key_map["budget_amount"]],
            currency=flat_object[key_map["budget_currency"]]
        )
        amount.save()
        project = Projet.objects.create(
            titre_projet=flat_object[key_map["title"]],
            description=flat_object[key_map["description"]]
        )
        project.save()
        budget = Budget.objects.create(
            source=flat_object[key_map["budget_source"]],
            description=flat_object[key_map["rationale"]],
            amount=amount,
            projet=project,
            uri=flat_object[key_map["budget_uri"]]
        )
        budget.save()
        planning, planning_created = Planning.objects.update_or_create(
            pk=flat_object[key_map["planning_id"]],
            raison=flat_object[key_map["rationale"]],
            budget=budget
        )
        planning.save()
        release.planning = planning
        release.save()




def import_xls(file):


    def create_tender(worksheet):
        pass

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
