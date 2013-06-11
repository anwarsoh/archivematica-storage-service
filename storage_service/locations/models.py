from django import forms
from django.db import models

from django_extensions.db.fields import UUIDField

class Location(models.Model):
    """ Stores information about a location. """

    id = UUIDField(primary_key=True)

    TRANSFER_SOURCE = 'TS'
    AIP_STORAGE = 'AS'
    # QUARANTINE = 'QU'
    # BACKLOG = 'BL'

    PURPOSE_CHOICES = (
        (TRANSFER_SOURCE, 'Transfer Source'),
        (AIP_STORAGE, 'AIP Storage'),
        # (QUARANTINE, 'Quarantine'),
        # (BACKLOG, 'Backlog Transfer'),
    )
    purpose = models.CharField(max_length=2,
                               choices=PURPOSE_CHOICES)

    LOCAL_FILESYSTEM = 'FS'
    # NFS = 'NFS'
    # SAMBA = 'SAMBA'
    # LOCKSS = 'LOCKSS'
    # FEDORA = 'FEDORA'
    ACCESS_PROTOCOL_CHOICES = (
        (LOCAL_FILESYSTEM, "Local Filesystem"),
    )
    access_protocol = models.CharField(max_length=6,
                            choices=ACCESS_PROTOCOL_CHOICES)

    path = models.TextField()
    # quota=0 -> unlimited
    quota = models.BigIntegerField(help_text="Size in bytes")
    used = models.BigIntegerField(default=0,
                                  help_text="Amount used in bytes")

    def __unicode__(self):
        return "{uuid}: {path} ({purpose}/{protocol})".format(
            uuid=self.id,
            path=self.path,
            purpose=self.purpose,
            protocol=self.access_protocol,
            )


# For validation of resources
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location