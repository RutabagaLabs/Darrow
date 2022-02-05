from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from .models import Team, User, Dispute, Court, Advice, Deal
from .forms import DisputeModelForm, AdviceModelForm, DealModelForm

# pylint: disable=no-member


def home_page(request):
    return render(request, "matters/login.html")


# class MatterListView(LoginRequiredMixin, generic.ListView):
#     """ All matters """
#     template_name = "matters/matter_list.html"
#     queryset = Matter.objects.all()
#     context_object_name = "matters"


class MyMatterListView(LoginRequiredMixin, generic.ListView):
    """ All matters assigned to the current user """
    template_name = "matters/my_matters.html"
    context_object_name = "my_matters"

    def get_queryset(self):
        q1 = Dispute.objects.filter(main_assignee = self.request.user).values("name", "main_assignee", "type", "pk")
        q2 = Advice.objects.filter(main_assignee = self.request.user).values("name", "main_assignee", "type", "pk")
        q3 = Deal.objects.filter(main_assignee = self.request.user).values("name", "main_assignee", "type", "pk")
        my_matters = q1.union(q2).union(q3)
        return my_matters


class TeamMatterListView(LoginRequiredMixin, generic.ListView):
    """ All matters assigned to a manager's team """
    template_name = "matters/team_matters.html"
    context_object_name = "team_matters"

    def get_queryset(self):
        my_teams = Team.objects.filter(team_lead = self.request.user)
        team_members = User.objects.filter(team__in = my_teams)
        q1 = Dispute.objects.filter(main_assignee__in = team_members).values_list("name", "main_assignee", "type")
        q2 = Advice.objects.filter(main_assignee__in = team_members).values_list("name", "main_assignee", "type")
        q3 = Deal.objects.filter(main_assignee__in = team_members).values_list("name", "main_assignee", "type")        
        team_matters = q1.union(q2).union(q3).order_by('main_assignee') and Advice.objects.filter(main_assignee__in = team_members).order_by('main_assignee') and Deal.objects.filter(main_assignee__in = team_members).order_by('main_assignee')
        return team_matters


# class MatterDetailView(LoginRequiredMixin, generic.DetailView):
#     """ Details of a single matter """
#     template_name = "matters/matter_detail.html"
#     queryset = Matter.objects.all()
#     context_object_name = "matter"


# class MatterCreateView(LoginRequiredMixin, generic.CreateView):
#     """ Create a new matter """
#     template_name = "matters/matter_create.html"
#     form_class = MatterModelForm

#     def get_success_url(self):
#         return reverse("matters:matter-list")


# class MatterUpdateView(LoginRequiredMixin, generic.UpdateView):
#     """ Update a signle matter """
#     template_name = "matters/matter_update.html"
#     queryset = Matter.objects.all()
#     form_class = MatterModelForm

#     def get_success_url(self):
#         return reverse("matters:matter-list")


# class MatterDeleteView(LoginRequiredMixin, generic.DeleteView):
#     """ Delete a matter """
#     template_name = "matters/matter_delete.html"
#     queryset = Matter.objects.all()

#     def get_success_url(self):
#         return reverse("matters:my-matters")    


class DisputeCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new dispute """
    template_name = "matters/dispute_create.html"
    form_class = DisputeModelForm   

    def get_success_url(self):
        return reverse("matters:my-matters")


class DisputeDetailView(LoginRequiredMixin, generic.DetailView):
    """ Details of a single matter """
    template_name = "matters/dispute_detail.html"
    queryset = Dispute.objects.all()
    context_object_name = "dispute"


class DisputeUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ Update a signle dispute """
    template_name = "matters/dispute_update.html"
    queryset = Dispute.objects.all()
    form_class = DisputeModelForm

    def get_success_url(self):
        return reverse("matters:my-matters")


class DisputeDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ Delete a matter """
    template_name = "matters/dispute_delete.html"
    queryset = Dispute.objects.all()

    def get_success_url(self):
        return reverse("matters:my-matters")  


class AdviceCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new advice and counsel matter """
    template_name = "matters/advice_create.html"
    form_class = AdviceModelForm   

    def get_success_url(self):
        return reverse("matters:my-matters")


class AdviceDetailView(LoginRequiredMixin, generic.DetailView):
    """ Details of a single advice and counsel matter """
    template_name = "matters/advice_detail.html"
    queryset = Advice.objects.all()
    context_object_name = "advice"


class AdviceUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ Update a signle advice and counsel matter """
    template_name = "matters/advice_update.html"
    queryset = Advice.objects.all()
    form_class = AdviceModelForm

    def get_success_url(self):
        return reverse("matters:my-matters")


class AdviceDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ Delete an advice and counsel matter """
    template_name = "matters/advice_delete.html"
    queryset = Advice.objects.all()

    def get_success_url(self):
        return reverse("matters:my-matters") 


class DealCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new transactional matter """
    template_name = "matters/deal_create.html"
    form_class = DealModelForm   

    def get_success_url(self):
        return reverse("matters:my-matters")


class DealDetailView(LoginRequiredMixin, generic.DetailView):
    """ Details of a single tranasactional matter """
    template_name = "matters/deal_detail.html"
    queryset = Deal.objects.all()
    context_object_name = "deal"


class DealUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ Update a signle transactional matter """
    template_name = "matters/deal_update.html"
    queryset = Deal.objects.all()
    form_class = DealModelForm

    def get_success_url(self):
        return reverse("matters:my-matters")


class DealDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ Delete a transactional matter """
    template_name = "matters/deal_delete.html"
    queryset = Deal.objects.all()

    def get_success_url(self):
        return reverse("matters:my-matters") 


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = "matters/dashboard.html"
    context_object_name = "my_matters"

    def get_queryset(self):
        my_matters = Dispute.objects.filter(main_assignee = self.request.user) and Advice.objects.filter(main_assignee = self.request.user) and Deal.objects.filter(main_assignee = self.request.user)
        return my_matters


def load_courts(request):
    state = request.GET.get('state')
    courts = Court.objects.filter(state=state).order_by('name')
    return render(request, 'matters/court_dropdown_list_options.html', {'courts': courts})


def my_matters_pie(request):
    labels = ['red', 'blue']
    data = [1,2]

    # queryset = Dispute.objects.filter(main_assignee = request.user)
    
    # for matter in queryset:
    #     labels.append(matter.dispute_type)
    #     data.append(matter.dispute_type.count)

    return render(request, 'matters/my_matters_pie.html', {
        'labels': labels,
        'data': data,
    })

