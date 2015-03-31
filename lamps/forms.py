from django.forms import ModelForm
from lamps.models import List, Gift, UserProfile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password', 'email']:
            self.fields[fieldname].help_text = None


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class ListForm(ModelForm):
    class Meta:
        model = List
        exclude = ['list_id', 'user_id', 'gift', 'slug']


class AddGiftsForm(ModelForm):
    class Meta:
        model = Gift
        exclude = ['gift_id']


class EditGiftsForm(ModelForm):
    class Meta:
        model = Gift
        exclude = ['gift_id']
