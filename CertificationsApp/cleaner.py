from datetime import datetime, timedelta
import os, shutil
from CertificationsApp.models import Operation
from django.conf import settings

def filesCleaner():
    limit_date = datetime.now() - timedelta(days = 30)
    operations = Operation.objects.filter(certificate_downloaded_at__lte = limit_date, certificate__isnull=False).exclude(certificate="")
    for operation in operations:
        operation.certificate = ""
        operation.save()
        os.chdir(settings.MEDIA_ROOT)
        shutil.rmtree(str(operation.id))