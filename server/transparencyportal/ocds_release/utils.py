from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from ocds_master_tables.serializers import PeriodSerializer, EntitySerializer, IdentifierSerializer, AddressSerializer, ContactPointSerializer
from ocds_planning.serializers import PlanningSerializers
from ocds_tender.serializers import TenderSerializer
from ocds_awards.serializers import AwardSerializer
from ocds_contracts.serializers import ContractSerializer

from .constants import RELEASE_TAG_CHOICES, PARTY_ROLE

class PartySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    identifier = IdentifierSerializer()
    address = AddressSerializer()
    contact_point = ContactPointSerializer()
    role = serializers.MultipleChoiceField(choices=PARTY_ROLE)


class PublicationSerializer(serializers.Serializer):
    ocid = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    tag = serializers.MultipleChoiceField(choices=RELEASE_TAG_CHOICES)
    initiation_type = serializers.CharField(max_length=255)
    buyer = EntitySerializer()
    planning = PlanningSerializers()
    tender = TenderSerializer()
    awards = AwardSerializer(many=True)
    contracts = ContractSerializer(many=True)
    parties = PartySerializer(many=True)

def clean(release, tags):
    """
    Clean release object : set ocid, date and tag
    """
    release.update_date()
    release.set_ocid()
    release.tags = tags

def to_json_publication(release):
    """
    Convert release to publication-friendly json object
    """
    clean(release, tags=["planning", "tender"])
    dict_release = PublicationSerializer(release).data
    return JSONRenderer().render(dict_release).decode()
