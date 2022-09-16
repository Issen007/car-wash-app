from django import forms

class EmailForm(forms.Form):
    smtp_server = forms.CharField(label='SMTP Server', max_length=64)
    smtp_port = forms.IntegerField(label='SMTP Port')
    smtp_user = forms.CharField(label='Username', max_length=128)
    smtp_password = forms.CharField(label='Password', max_length=256)
    smtp_subject = forms.CharField(label='Email Subject', max_length=64)
    smtp_body = forms.CharField(widget=forms.Textarea)






    # smtp_server = models.CharField(max_length = 64, default = 'smtp.google.com', blank=False)
    # smtp_port = models.IntegerField(default = 587, blank = False)
    # smtp_user = models.CharField(max_length = 128, default = 'name@company.com', blank=True)
    # smtp_password = models.CharField(max_length = 256, default = 'password', blank=True)
    # smtp_protocol = models.CharField(max_length = 4, choices=EncryptionType.choices, default=EncryptionType.STARTTLS)
    # smtp_subject = models.TextField(max_length = 64, default = 'Default E-Mail Subject Title', blank=True)
    # smtp_body = models.TextField(max_length = 255, default = 'Default Body Field', blank=True)