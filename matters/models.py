from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """ Inherits from Django's AbstractUser, then adds a custom field """
    role = models.CharField(
        choices = [
            ('AT', 'Attorney'), 
            ('LS', 'Legal Specialist'),
            ('LC', 'Legal Coordinator'),
            ('NAM', 'Non-Attorney Manager'),
            ],
        max_length=30)
    
    team = models.ForeignKey('Team', related_name='assigned_team', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Associate(models.Model):
    """ Legal Dept associates who can be assigned to a matter """
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Team(models.Model):
    """ Defines the team a user can belong to """
    team_name = models.CharField(max_length=200)
    team_lead = models.ForeignKey('User', related_name='team_lead_name', null=True, blank=True, on_delete=models.SET_NULL)
    team_assocgc = models.ForeignKey('User', related_name='assocgc_name', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        """ Return a string representation of the model """
        return self.team_name


class State(models.Model):
    """ A list of states and provinces that will also drive the choice of court """
    name = models.CharField(max_length=25)

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Client(models.Model):
    """ A list of business units """
    name = models.CharField(max_length=100)

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Court(models.Model):
    """ The court where a dispute is filed """
    name = models.CharField(max_length=100)
    state = models.ManyToManyField(State)
    court_type = models.CharField(
        choices = [
            ('ST', 'State'),
            ('FD', 'Federal'),
        ],
    max_length=8)

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Matter(models.Model):
    """ A basic matter to track """
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True)
    client = models.ForeignKey("Client", null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    main_assignee = models.ForeignKey("User", null=True, blank=True, on_delete=models.SET_NULL)
    matter_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Dispute(Matter):
    """ Dispute matter type """
    type = models.CharField(
        choices = [
            ('DP', 'Dispute'), 
            ('AD', 'Advice'),
            ('DL', 'Deal'),
        ],
    max_length=10,
    default="Dispute")

    plaintiff = models.CharField(max_length=100)
    defendant = models.CharField(max_length=100)
    dispute_type = models.CharField(
        choices = [
            ('PT', 'Patent'), 
            ('TM', 'Trademark'),
            ('CY', 'Copyright'),
            ('BR', 'Bankruptcy'),
            ('VN', 'Vendor'),
            ('IS', 'Installed Sales'),
            ('CT', 'Customer Transaction'),
            ('DA', 'ADA'),
            ('CN', 'Construction'),
            ('RE', 'Real Estate'),
            ('PI', 'Personal Injury'),
            ('AM', 'Automobile'),
        ],
    max_length=25)

    state = models.ForeignKey('State', null=True, blank=True, on_delete=models.SET_NULL)
    court = models.ForeignKey('Court', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Advice(Matter):
    """ An advice and counsel matter """
    type = models.CharField(
        choices = [
            ('DP', 'Dispute'), 
            ('AD', 'Advice'),
            ('DL', 'Deal'),
        ],
    max_length=10,
    default="Advice")

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Deal(Matter):
    """ A transactional matter """
    type = models.CharField(
        choices = [
            ('DP', 'Dispute'), 
            ('AD', 'Advice'),
            ('DL', 'Deal'),
        ],
    max_length=10,
    default="Deal")
    
    def __str__(self):
        """ Return a string representation of the model """
        return self.name