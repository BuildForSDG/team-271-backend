from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import MedicalFacility


class FacilityListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='facilities:facility-detail',
        lookup_field='pk'
    )

    class Meta:
        model = MedicalFacility
        fields = ['url', 'facility_name', 'facility_email',
                  'facilty_location', 'lon', 'lat']


class FacilityDetailSerializer(ModelSerializer):

    class Meta:
        model = MedicalFacility
        fields = ['pk', 'facility_name', 'facility_email',
                  'facilty_location', 'lon', 'lat']
