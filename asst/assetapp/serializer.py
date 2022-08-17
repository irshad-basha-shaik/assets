from .utils import *
from rest_framework import serializers
from .models import AssetModel
from django.template.loader import render_to_string


class AssetSerializers(serializers.ModelSerializer):

    def create(self, validate_data):
        subject ='Warranty expiry'
        plain_message ='Warranty is expiring soon'
        from_email = 'ibasha36@gmail.com'
        to_email = ['swamy0075@gmail.com','swamy@gefindia.net']
        html_message = render_to_string('mail_template.html', {'context': 'values'})
        EmailThread(subject, plain_message, from_email, to_email, html_message).start()
        return AssetModel.objects.create()

    class Meta:
        model = AssetModel
        fields = '__all__'

        password = serializers.CharField(max_length=128, write_only=True, required=True)
