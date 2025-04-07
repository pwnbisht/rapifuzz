from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user_auth.models import BaseModel, User

class Incident(BaseModel):
    
    INCIDENT_TYPE_CHOICES = [
        ('Enterprise', 'Enterprise'),
        ('Government', 'Government'),
    ]
    
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    incident_id = models.CharField(
        _('incident ID'), max_length=20, unique=True, editable=False
    )
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='incidents'
    )
    incident_type = models.CharField(
        _('incident type'), max_length=20, choices=INCIDENT_TYPE_CHOICES
    )
    incident_details = models.TextField(_('incident details'))
    reported_date_time = models.DateTimeField(
        _('reported date time'), auto_now_add=True
    )
    priority = models.CharField(
        _('priority'), max_length=10, choices=PRIORITY_CHOICES
    )
    status = models.CharField(
        _('status'), max_length=20, choices=STATUS_CHOICES, default='Open'
    )

    class Meta:
        verbose_name = _('incident')
        verbose_name_plural = _('incidents')
        ordering = ['-reported_date_time']

    def __str__(self):
        return self.incident_id