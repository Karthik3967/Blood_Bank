from django.core.mail import send_mail
from django.conf import settings
from django.db import models


class BloodRequest(models.Model):
    ...
    def save(self, *args, **kwargs):
        if self.pk:
            original = BloodRequest.objects.get(pk=self.pk)
            if original.status != self.status:
                send_mail(
                    subject='Your Blood Request Status Changed',
                    message=f'Hello {self.user.username}, your request for {self.group} ({self.units} units) is now {self.status}.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[self.user.email],
                    fail_silently=True
                )
        super().save(*args, **kwargs)
