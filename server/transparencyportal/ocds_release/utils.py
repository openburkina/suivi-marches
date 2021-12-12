from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

def clean(release : dict):
    """
    Clean release object and set ocid, date and tag
    """
    pass

def to_json_publication(release):
    """
    Convert release to publication-friendly json object
    """
    pass
