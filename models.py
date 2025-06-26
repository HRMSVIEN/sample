from django.db import models
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator

class Emp(models.Model):
    name = models.CharField(max_length=255)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    created_at=models.DateField(auto_now_add=True)
    score=models.IntegerField(null=True)
    topic=models.CharField(max_length=20,null=True)
    tech_score=models.IntegerField(null=True)
    count=models.IntegerField(default=0)
    slug=models.SlugField(unique=True)
    # Section 1: Personal Information
    dob = models.CharField(max_length=255)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Other', 'Other'),
    ]
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    nationality = models.CharField(max_length=100)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)

    # Section 2: Application Details
    position_applied = models.CharField(max_length=255)
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'), ('HR', 'HR'), ('Networking', 'Networking'),
        ('Digital Marketing', 'Digital Marketing'), ('Operations', 'Operations'),
        ('Sales', 'Sales'), ('Other', 'Other'),
    ]
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)


    # Section 3: Professional Details
    ug_qualification = models.CharField(max_length=255)
    ug_category = models.CharField(max_length=255, null=True, blank=True)
    year_of_graduation = models.CharField(max_length=4) # Changed to CharField for flexibility, though IntegerField is also possible
    current_employer = models.CharField(max_length=255)
    total_experience = models.CharField(max_length=100)
    relevant_experience = models.CharField(max_length=255, blank=True, null=True)
    skills_certifications = models.TextField(blank=True, null=True)
    pg_qualification = models.CharField(max_length=255, blank=True, null=True)
    pg_category = models.CharField(max_length=255, null=True, blank=True)
    year_of_pg_graduation = models.CharField(max_length=4, blank=True, null=True)  # Changed to CharField for flexibility

    # Section 4: Document Submission
    resume_upload = models.FileField(upload_to="picture")
    photo_upload = models.ImageField(upload_to="picture")
    DEGREE_TYPE_CHOICES = [
        ('UG', 'Undergraduate (UG)'),
        ('PG', 'Postgraduate (PG)'),
        ('Diploma', 'Diploma'),
    ]
    # Allow multiple degrees
    degrees = models.CharField(max_length=100, help_text="Comma-separated: UG,PG,Diploma", null=True, blank=True)

    # PG-specific fields
    pg_degree_name = models.CharField(max_length=255, null=True, blank=True)
    pg_category = models.CharField(max_length=255, null=True, blank=True)

    # These fields are conditionally required based on is_experienced
    payslip_upload = models.FileField(upload_to="picture", blank=True)

    def __str__(self):
        return self.full_name


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name + "_" + str(self.created_at))
        return super().save(*args,**kwargs) 
    def __str__(self):
        return self.name