import uuid
from django.db import models
from django_quill.fields import QuillField


class SiteInfo(models.Model):

    key = models.CharField(
        max_length=200,
        unique=True,
        )

    value = models.CharField(
        max_length=200,
        blank=True
        )

    html_content = QuillField(
        blank=True,
        )

    def __str__(self):
        return self.key

    @staticmethod
    def get_data():
        site_info = {}
        for data in SiteInfo.objects.all():
            if data.value:
                val = data.value
            else:
                val = data.html_content.html
            site_info[data.key] = val
        return site_info


class Donor(models.Model):

    name = models.CharField(
        max_length=200,
        )

    url = models.CharField(
        max_length=200,
        blank=True,
        )

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(
        max_length=200,
        unique=True,
        )

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/document_<id>|<filename>
    return f'document_{instance.uuid}'


class Document(models.Model):

    PHOTO = 'photo'
    VIDEO = 'video'
    PDF = 'pdf'

    TYPOLOGY_CHOICES = [
        (PHOTO, 'Photo'),
        (VIDEO, 'Video'),
        (PDF, 'PDF'),
    ]

    name = models.CharField(max_length=200, )

    content = models.FileField(upload_to=user_directory_path, )

    typology = models.CharField(
        max_length=16,
        choices=TYPOLOGY_CHOICES,
        default=PHOTO,
        )

    description = QuillField(
        blank=True,
        )

    year = models.CharField(
        max_length=200,
        blank=True,
        )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )

    donor = models.ForeignKey(
        'Donor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )

    date = models.DateField(auto_now_add=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, )

    def __str__(self):
        return self.name
