from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer

from ..user_auth.authentication import CookieJWTAuthentication


class IncidentListCreateView(generics.ListCreateAPIView):
    """
    List all incidents for the authenticated user or create a new incident.
    """
    serializer_class = IncidentSerializer
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(reporter=self.request.user)

class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an incident by incident_id.
    """
    serializer_class = IncidentSerializer
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'incident_id'

    def get_queryset(self):
        return Incident.objects.filter(reporter=self.request.user)

class IncidentSearchView(generics.ListAPIView):
    """
    Search incidents by incident_id (exact match).
    """
    serializer_class = IncidentSerializer
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        incident_id = self.request.query_params.get('incident_id', None)
        if incident_id:
            return Incident.objects.filter(
                reporter=self.request.user, incident_id=incident_id
            )
        return Incident.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {'detail': 'No incident found with the provided ID'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)