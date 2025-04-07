from rest_framework import serializers
from .models import Incident
from ..utils import incidents

class IncidentSerializer(serializers.ModelSerializer):
    reporter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Incident
        fields = [
            'id', 'incident_id', 'reporter', 'incident_type', 'incident_details',
            'reported_date_time', 'priority', 'status'
        ]
        read_only_fields = ['incident_id', 'reporter', 'reported_date_time']

    def validate(self, attrs):
        if self.instance and self.instance.status == 'Closed':
            raise serializers.ValidationError(
                {"status": "Opps..you cannot edit a closed incident"}
            )
        return attrs

    def create(self, validated_data):
        validated_data['incident_id'] = incidents.generate_incident_id()
        validated_data['reporter'] = self.context['request'].user
        return super().create(validated_data)