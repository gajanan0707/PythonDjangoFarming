from django import forms
from .models import Contact,Feedback, Complaint


class ContactFrom(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'second_name','email_id','message','mobile_no')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('farmer_name', 'email','details')

class ComplaintForm(forms.ModelForm):

    class Meta:
        model=Complaint
        fields=('name','email','complaint_type','complaint_message')