from django.contrib.auth.forms import (
  AuthenticationForm, PasswordChangeForm, UserCreationForm
)

from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea

from accounts.models import Profile

class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = biography = CharField(label='Biography', widget=Textarea(attrs={'placeholder': 'Tell us your story with movies'}), 
    min_length=40)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result