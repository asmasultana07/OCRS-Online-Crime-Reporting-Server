# profiles/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'age', 'location','profile_picture']  # Add other fields as needed

# Remove the following line if you added it previously
# UserProfileForm.base_fields['name'] = forms.CharField(max_length=255, required=False)
