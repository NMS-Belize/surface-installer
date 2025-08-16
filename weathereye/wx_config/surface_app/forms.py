from django import forms
from .models import InstallType

class SurfaceConfigurationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SurfaceConfigurationForm, self).__init__(*args, **kwargs)
        
        install_type = InstallType.objects.last()
        
        if install_type and install_type.install_type == 'remote':
            self.fields['host'] = forms.CharField(
                label="Remote Host for SURFACE install:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg.. username@xxx.xx.xxx.xx'})
            )
            self.fields['surface_repo_path'] = forms.CharField(
                label="Path on remote machine to clone SURFACE repository:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control',})
            )
            self.fields['remote_connect_password'] = forms.CharField(
                label="Password to connect to the remote machine:", 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control',})
            )
            self.fields['root_password'] = forms.CharField(
                label="Root password on the remote machine:", 
                required=True, 
                widget=forms.PasswordInput(attrs={'class': 'form-control',})
            )
        elif install_type and install_type.install_type == 'local':
            self.fields['surface_repo_path'] = forms.CharField(
                label="Path to clone SURFACE repository:", 
                required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control',})
            )

    with_data = forms.ChoiceField(
        label="Start with Backup data:", 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        required=True, 
        initial='no',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input',})
    )
    globals_data_path = forms.CharField(
        label="Globals backup dump file path on host machine:", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '(e.g. /path/to/globals/backup.sql.gz)'})
    )
    data_path = forms.CharField(
        label="Backup dump file path on host machine:", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '(e.g. /path/to/backup.sql.gz)'})
    )
    admin = forms.CharField(
        label="Admin Username:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    admin_email = forms.CharField(
        label="Admin Email:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    admin_password = forms.CharField(
        label="Admin Password:", 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control',})
    )
    
    # New form fields
    lrgs_user = forms.CharField(
        label="LRGS User:", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    lrgs_password = forms.CharField(
        label="LRGS Password:", 
        required=False, 
        widget=forms.PasswordInput(attrs={'class': 'form-control',})
    )
    timezone_name = forms.CharField(
        label="Timezone Name:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    timezone_offset = forms.CharField(
        label="Timezone Offset:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    map_latitude = forms.CharField(
        label="Map Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    map_longitude = forms.CharField(
        label="Map Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    map_zoom = forms.IntegerField(
        label="Map Zoom Level:", 
        required=True, 
        widget=forms.NumberInput(attrs={'id':'zoomField','class': 'form-control',})
    )
    spatial_analysis_initial_latitude = forms.CharField(
        label="Spatial Analysis Initial Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_initial_longitude = forms.CharField(
        label="Spatial Analysis Initial Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_final_latitude = forms.CharField(
        label="Spatial Analysis Final Latitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )
    spatial_analysis_final_longitude = forms.CharField(
        label="Spatial Analysis Final Longitude:", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field',})
    )

    # wis2box options
    surface_encryption_key = forms.CharField(
        label="Encryption Key:", 
        required=True, 
        max_length=44,  # Ensures Django enforces the limit at the model/form level
        widget=forms.TextInput(attrs={'class': 'form-control disabled-field form-larger-size', 'maxlength': '44'})  # Limits input length in the frontend
    )
    # # regional
    # wis2box_user_regional = forms.CharField(
    #     label=" Regional WIS2BOX Storage Username:", 
    #     required=False, 
    #     widget=forms.TextInput(attrs={'class': 'form-control',})
    # )
    # wis2box_password_regional = forms.CharField(
    #     label="Regional WIS2BOX Storage Password:", 
    #     required=False, 
    #     widget=forms.PasswordInput(attrs={'class': 'form-control',})
    # )
    # wis2box_endpoint_regional = forms.CharField(
    #     label="Regional Endpoint:", 
    #     required=False, 
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg.. xxx.xx.xxx.xx:port#'})
    # )

    # # local
    # wis2box_user_local = forms.CharField(
    #     label="Local WIS2BOX Storage Username:", 
    #     required=False, 
    #     widget=forms.TextInput(attrs={'class': 'form-control',})
    # )
    # wis2box_password_local = forms.CharField(
    #     label="Local WIS2BOX Storage Password:", 
    #     required=False, 
    #     widget=forms.PasswordInput(attrs={'class': 'form-control',})
    # )
    # wis2box_endpoint_local = forms.CharField(
    #     label="Local Endpoint:", 
    #     required=False, 
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg.. xxx.xx.xxx.xx:port#'})
    # )


    # Define the list of options as choices
    TOPIC_HIERARCHY_CHOICES = [
        ('', '--------'),
        ('origin/a/wis2/ag-antiguamet/data/core/weather/surface-based-observations/synop', 'Antigua (ag-antiguamet)'),
        ('origin/a/wis2/ky-cinws/data/core/weather/surface-based-observations/synop', 'Cayman Islands (ky-cinws)'),
        ('origin/a/wis2/dm-dms/data/core/weather/surface-based-observations/synop', 'Dominica (dm-dms)'),
        ('origin/a/wis2/gd-metservice/data/core/weather/surface-based-observations/synop', 'Grenada (gd-metservice)'),
        ('origin/a/wis2/gy-hydromet/data/core/weather/surface-based-observations/synop', 'Guyana (gy-hydromet)'),
        ('origin/a/wis2/kn-metservice/data/core/weather/surface-based-observations/synop', 'St. Kitts and Nevis (kn-metservice)'),
        ('origin/a/wis2/sx-metservice/data/core/weather/surface-based-observations/synop', 'Sint Maarten (sx-metservice)'),
        ('origin/a/wis2/tc-metservice/data/core/weather/surface-based-observations/synop', 'Turks and Caicos (tc-metservice)'),
        ('origin/a/wis2/lc-metservice/data/core/weather/surface-based-observations/synop', 'Saint Lucia (lc-metservice)'),
        ('origin/a/wis2/tt-trin-met/data/core/weather/surface-based-observations/synop', 'Trinidad and Tobago (tt-trin-met)'),
        ('origin/a/wis2/vc-metservice/data/core/weather/surface-based-observations/synop', 'Saint Vincent (vc-metservice)'),
        ('origin/a/wis2/ai-metservice/data/core/weather/surface-based-observations/synop', 'Anguilla (ai-metservice)'),
        ('origin/a/wis2/jm-msj/data/core/weather/surface-based-observations/synop', 'Jamaica (jm-msj)'),
        ('origin/a/wis2/bz-nms/data/core/weather/surface-based-observations/synop', 'Belize (bz-nms)'),
        ('origin/a/wis2/bs-metservice/data/core/weather/surface-based-observations/synop', 'Bahamas (bs-metservice)'),
        ('origin/a/wis2/ms-metservice/data/core/weather/surface-based-observations/synop', 'Montserrat (ms-metservice)'),
        ('origin/a/wis2/vg-metservice/data/core/weather/surface-based-observations/synop', 'British Virgin Islands (vg-metservice)')
    ]

    # The hierarchy
    # Make wis2box_topic_hierarchy a dropdown
    wis2box_topic_hierarchy = forms.ChoiceField(
        label="Topic Hierarchy:",
        choices=TOPIC_HIERARCHY_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form-larger-size'})
    )
