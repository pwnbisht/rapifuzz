from django.utils.crypto import get_random_string
from datetime import datetime
from ..incidents.models import Incident

def generate_incident_id():
    """
    Generates a unique incident ID in the format RMGxxxxxYYYY.
    """
    year = datetime.now().year
    while True:
        random_number = get_random_string(length=5, allowed_chars='0123456789')
        incident_id = f"RMG{random_number}{year}"
        if not Incident.objects.filter(incident_id=incident_id).exists():
            return incident_id
