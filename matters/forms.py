from django import forms
from .models import State, Court, Dispute, Advice, Deal


# class MatterModelForm(forms.ModelForm):
#     class Meta:
#         model = Matter
#         fields = (
#             'name',
#             'desc',
#             'main_assignee',
#             )


class AdviceModelForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = (
            'name',
            'desc',
            'main_assignee',
            )


class DealModelForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = (
            'name',
            'desc',
            'main_assignee',
            )


class DisputeModelForm(forms.ModelForm):
    class Meta:
        model = Dispute
        fields = (
            'name',
            'desc',
            'client',
            'main_assignee',
            'matter_active',
            'plaintiff',
            'defendant',
            'dispute_type',
            'state',
            'court',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['court'].queryset = Court.objects.none()

        if 'state' in self.data:
            try:
                state = int(self.data.get('state'))
                self.fields['court'].queryset = Court.objects.filter(state=state).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty court queryset
        elif self.instance.pk:
            self.fields['court'].queryset = self.instance.state.court_set.order_by('name')  