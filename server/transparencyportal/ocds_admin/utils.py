from django.db.models.deletion import ProtectedError
from ocds_master_tables.models import (
    Address,
    Budget,
    Classification,
    ContactPoint,
    Entity,
    Identifier,
    Milestone,
    Period,
    Projet,
    Unit,
    Value,
)
from ocds_planning.models import Planning
from ocds_release.models import Record, Release, Target
from ocds_tender.models import Tender
from ocds_awards.models import Award
from ocds_contracts.models import Contract
from ocds_implementation.models import Implementation, Transaction

from openpyxl import worksheet

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
            try:
                to_delete.delete()
            except ProtectedError:
                print("Object : %s cannot be deleted. It is referenced elsewhere." % to_delete)
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
            record = Record.objects.create(
                ocid=flat_object[key_map["ocid"]],
                implementation_address=incoming_address,
                target=incoming_target
            )
        try:
            record.compiled_release
        except Release.DoesNotExist:
            Release.objects.create(
                ref_record=record,
                tag=["planning"]
            )

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
        except Record.DoesNotExist:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        except Release.DoesNotExist:
            print("Record object with OCID : %s does not have a release" % flat_object[key_map["record_ocid"]])
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
        except Record.DoesNotExist:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        except Release.DoesNotExist:
            print("Record object with OCID : %s does not have a release" % flat_object[key_map["record_ocid"]])
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
            buyer_entity = Entity.objects.get(pk=flat_object[key_map["buyer"]])
        except Record.DoesNotExist:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["record_ocid"]])
            continue
        except Release.DoesNotExist:
            print("Record object with OCID : %s does not have a release" % flat_object[key_map["record_ocid"]])
            continue
        except Entity.DoesNotExist:
            print("Buyer with id : %s does not exist" % flat_object[key_map["buyer"]])
            continue
        try:
            procuring_entity = Entity.objects.get(pk=flat_object[key_map["procuring_entity"]])
        except Entity.DoesNotExist:
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

def create_tenderers(ws: worksheet):
    key_map = {
        "tender_id": 0,
        "tenderer_id": 1
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            tender = Tender.objects.get(pk=flat_object[key_map["tender_id"]])
            tender_release = tender.release
            incoming_tenderer = Entity.objects.get(pk=flat_object[key_map["tenderer_id"]])
        except Tender.DoesNotExist:
            print("Tender object with ID : %s does not exist" % flat_object[key_map["tender_id"]])
            continue
        except Release.DoesNotExist:
            print("Release object with ID : %s does not refer to a release" % flat_object[key_map["tender_id"]])
            continue
        except Entity.DoesNotExist:
            print("Entity object with ID : %s does not exist" % flat_object[key_map["tenderer_id"]])
            continue
        tender.tenderers.add(incoming_tenderer)
        tender_release.parties.add(incoming_tenderer)
        tender_release.add_role(incoming_tenderer, 'tenderer')

def create_awards(ws: worksheet):
    key_map = {
        "record_ocid": 0,
        "id": 1,
        "title": 2,
        "description": 3,
        "status": 4,
        "date": 5,
        "value_amount": 6,
        "value_currency": 7,
        "contract_title": 8,
        "contract_description": 9,
        "contract_status": 10,
        "contract_date": 11,
        "contract_period_start": 12,
        "contract_period_end": 13
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        incoming_value = Value.objects.create(
            amount=flat_object[key_map["value_amount"]],
            currency=flat_object[key_map["value_currency"]]
        )
        incoming_contract_period = Period.objects.create(
            start_date=flat_object[key_map["contract_period_start"]],
            end_date=flat_object[key_map["contract_period_end"]]
        )
        try:
            release = Record.objects.get(ocid=flat_object[key_map["record_ocid"]]).compiled_release
        except Record.DoesNotExist:
            print("Record object with OCID : %s does not exist" % flat_object[key_map["tender_id"]])
            continue
        except Release.DoesNotExist:
            print("Record object with OCID : %s does not have a release" % flat_object[key_map["tender_id"]])
            continue
        try:
            award = Award.objects.get(pk=flat_object[key_map["id"]])
            related_fields = [
                ('value', incoming_value),
                ('contract_period', incoming_contract_period)
            ]
            set_related_fields(award, related_fields)
        except Award.DoesNotExist:
            award = Award.objects.create(
                pk=flat_object[key_map["id"]],
                value=incoming_value,
                contract_period=incoming_contract_period
            )
        try:
            contract = award.contract
            contract.value = award.value
            contract.period = award.contract_period
        except Contract.DoesNotExist:
            contract = Contract.objects.create(
                ref_award=award,
                period=incoming_contract_period,
                value=incoming_value
            )
        try:
            implementation = contract.implementation
        except Implementation.DoesNotExist:
            implementation = Implementation(
                contract = contract
            )
        award.title = flat_object[key_map["title"]]
        award.description = flat_object[key_map["description"]]
        award.status = flat_object[key_map["status"]]
        award.date = flat_object[key_map["date"]]
        award.release = release
        award.save()
        contract.title = flat_object[key_map["contract_title"]]
        contract.description = flat_object[key_map["contract_description"]]
        contract.status = flat_object[key_map["contract_status"]]
        contract.date_signed = flat_object[key_map["contract_date"]]
        contract.save()
        implementation.save()

def create_suppliers(ws: worksheet):
    key_map = {
        "award_id": 0,
        "supplier_id": 1
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            award = Award.objects.get(pk=flat_object[key_map["award_id"]])
            award_release = award.release
            incoming_supplier = Entity.objects.get(pk=flat_object[key_map["supplier_id"]])
        except Award.DoesNotExist:
            print("Award object with ID : %s does not exist" % flat_object[key_map["award_id"]])
            continue
        except Release.DoesNotExist:
            print("Award object with ID : %s does not refer to a release" % flat_object[key_map["award_id"]])
            continue
        except Entity.DoesNotExist:
            print("Entity object with ID : %s does not exist" % flat_object[key_map["supplier_id"]])
            continue
        award.suppliers.add(incoming_supplier)
        award_release.parties.add(incoming_supplier)
        award_release.add_role(incoming_supplier, 'supplier')

def create_transactions(ws : worksheet):
    key_map = {
        "award_id": 0,
        "transaction_id": 1,
        "source": 2,
        "uri": 3,
        "date": 4,
        "value_amount": 5,
        "value_currency": 6,
        "payer_id": 7,
        "payee_id": 8
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            implementation = Award.objects.get(pk=flat_object[key_map["award_id"]]).contract.implementation
            payer = Entity.objects.get(pk=flat_object[key_map["payer_id"]])
            payee = Entity.objects.get(pk=flat_object[key_map["payee_id"]])
        except Award.DoesNotExist:
            print("Award object with ID : %s does not exist" % flat_object[key_map["tender_id"]])
            continue
        except Entity.DoesNotExist:
            print("Entity does not exist")
            continue
        incoming_value = Value.objects.create(
            amount=flat_object[key_map["value_amount"]],
            currency=flat_object[key_map["value_currency"]]
        )
        try:
            transaction = Transaction.objects.get(pk=flat_object[key_map["transaction_id"]])
            related_fields = [
                ('value', incoming_value)
            ]
            set_related_fields(transaction, related_fields)
        except Transaction.DoesNotExist:
            transaction = Transaction(
                pk=flat_object[key_map["transaction_id"]],
                value=incoming_value
            )
        transaction.implementation = implementation
        transaction.source = flat_object[key_map["source"]]
        transaction.uri = flat_object[key_map["uri"]]
        transaction.date = flat_object[key_map["date"]]
        transaction.payer = payer
        transaction.payee = payee
        transaction.save()

def create_items(ws : worksheet):
    key_map = {
        "item_id": 0,
        "step_name": 1,
        "ref_step": 2,
        "description": 3,
        "quantity": 4,
        "unit_name": 5,
        "unit_value_amount": 6,
        "unit_value_currency": 7,
        "classification_scheme": 8,
        "classification_description": 9,
        "classification_uri": 10
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            step_name = flat_object[key_map["step_name"]]
            if step_name == 'tender':
                ref_object = Tender.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'award':
                ref_object = Award.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'contract':
                ref_object = Contract.objects.get(pk=flat_object[key_map["ref_step"]])
        except:
            print("%s object with ID : %s does not exist" % (flat_object[key_map["step_name"]], flat_object[key_map["ref_step"]]))
            continue
        items = ref_object.items
        incoming_value = Value.objects.create(
            amount=flat_object[key_map["unit_value_amount"]],
            currency=flat_object[key_map["unit_value_currency"]]
        )
        incoming_unit = Unit.objects.create(
            name=flat_object[key_map["unit_name"]],
            value=incoming_value
        )
        incoming_classification = Classification.objects.create(
            scheme=flat_object[key_map["classification_scheme"]],
            description=flat_object[key_map["classification_description"]],
            uri=flat_object[key_map["classification_uri"]]
        )
        try:
            item = items.get(pk=flat_object[key_map["item_id"]])
            related_fields = [
                ('classification', incoming_classification),
                ('unit', incoming_unit),
            ]
            set_related_fields(item, related_fields)
            item.quantity = flat_object[key_map["quantity"]]
            item.description = flat_object[key_map["description"]]
            item.save()
        except:
            item = items.create(
                pk=flat_object[key_map["item_id"]],
                quantity = flat_object[key_map["quantity"]],
                description = flat_object[key_map["description"]],
                classification=incoming_classification,
                unit=incoming_unit
            )

def create_milestones(ws : worksheet):
    key_map = {
        "milestone_id": 0,
        "step_name": 1,
        "ref_step": 2,
        "title": 3,
        "description": 4,
        "due_date": 5,
        "date_modified": 6,
        "status": 7
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            step_name = flat_object[key_map["step_name"]]
            if step_name == 'planning':
                ref_object = Planning.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'tender':
                ref_object = Tender.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'contract':
                ref_object = Contract.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'implementation':
                ref_object = Implementation.objects.get(pk=flat_object[key_map["ref_step"]])
        except:
            print("%s object with ID : %s does not exist" % (flat_object[key_map["step_name"]], flat_object[key_map["ref_step"]]))
            continue
        milestones = ref_object.milestones
        try:
            milestone = milestones.get(pk=flat_object[key_map["milestone_id"]])
            milestone.title = flat_object[key_map["title"]]
            milestone.description = flat_object[key_map["description"]]
            milestone.due_date = flat_object[key_map["due_date"]]
            milestone.date_modified = flat_object[key_map["date_modified"]]
            milestone.status = flat_object[key_map["status"]]
            milestone.save()
        except:
            milestone = milestones.create(
                pk=flat_object[key_map["milestone_id"]],
                title = flat_object[key_map["title"]],
                description = flat_object[key_map["description"]],
                due_date = flat_object[key_map["due_date"]],
                date_modified = flat_object[key_map["date_modified"]],
                status = flat_object[key_map["status"]]
            )

def create_documents(ws: worksheet):
    key_map = {
        "document_id": 0,
        "step_name": 1,
        "ref_step": 2,
        "type": 3,
        "title": 4,
        "description": 5,
        "url": 6,
        "date_published": 7,
        "date_modified": 8,
        "format": 9,
        "language": 10
    }
    for flat_object in ws.iter_rows(min_row=4, values_only=True):
        if not flat_object[0]:
            continue
        try:
            step_name = flat_object[key_map["step_name"]]
            if step_name == 'planning':
                ref_object = Planning.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'tender':
                ref_object = Tender.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'award':
                ref_object = Award.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'contract':
                ref_object = Contract.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'implementation':
                ref_object = Implementation.objects.get(pk=flat_object[key_map["ref_step"]])
            if step_name == 'milestone':
                ref_object = Milestone.objects.get(pk=flat_object[key_map["ref_step"]])
        except:
            print("%s object with ID : %s does not exist" % (flat_object[key_map["step_name"]], flat_object[key_map["ref_step"]]))
            continue
        documents = ref_object.documents
        try:
            document = documents.get(pk=flat_object[key_map["document_id"]])
            document.document_type = flat_object[key_map["type"]]
            document.title = flat_object[key_map["title"]]
            document.description = flat_object[key_map["description"]]
            document.url = flat_object[key_map["url"]]
            document.date_published = flat_object[key_map["date_published"]]
            document.date_modified = flat_object[key_map["date_modified"]]
            document.document_format = flat_object[key_map["format"]]
            document.language = flat_object[key_map["language"]]
            document.save()
        except:
            document = documents.create(
                pk = flat_object[key_map["document_id"]],
                document_type = flat_object[key_map["type"]],
                title = flat_object[key_map["title"]],
                description = flat_object[key_map["description"]],
                url = flat_object[key_map["url"]],
                date_published = flat_object[key_map["date_published"]],
                date_modified = flat_object[key_map["date_modified"]],
                document_format = flat_object[key_map["format"]],
                language = flat_object[key_map["language"]]
            )
