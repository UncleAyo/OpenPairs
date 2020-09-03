from django import forms
from .models import StudentDetail

country_list = [
    ('Algeria', 'Algeria'), ('Angola', 'Angola'), ('Benin', 'Benin'), ('Botswana', 'Botswana'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Camoros', 'Camoros'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Republic of the Congo', 'Republic of the Congo'), ('Djibouti', 'Djibouti'), ('Egypt', 'Egypt'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Ethiopia', 'Ethiopia'), ('Gabon', 'Gabon'), ('The Gambia', 'The Gambia'), ('Ghana', 'Ghana'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Côte d\'Ivoire', 'Côte d\'Ivoire'), ('Kenya', 'Kenya'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Mali', 'Mali'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Somalia', 'Somalia'), ('Somaliland', 'Somaliland'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Sudan', 'Sudan'), ('Swaziland', 'Swaziland'), ('Tanzania', 'Tanzania'), ('Togo', 'Togo'), ('Tunisia', 'Tunisia'), ('Uganda', 'Uganda'), ('Western Sahara', 'Western Sahara'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'), ("Other...", "Other...")
    ]

region_list = [
    ('North Africa', 'North Africa'),
    ('Southern Africa', 'Southern Africa'),
    ('West Africa', 'West Africa'),
    ('East Africa','East Africa'),
    ('Central Africa', 'Central Africa'),
    ('Islands', 'Islands'),
    ('Outside Africa', 'Outside Africa')
]

year_group = [
    ('Year One', 'Year One'), 
    ('Year Two', 'Year Two'),
    ('Catalyst', 'Catalyst')
]

sex_list = [('Male','Male'),('Female','Female')]

temp_list = [
    (1, 'Really hot'), 
    (2, 'Cool'), 
    (3, 'Really cold')
]

sleeper_list = [
    (1, 'Very Light Sleeper'), 
    (2, 'Light Sleeper'), 
    (3, 'Heavy Sleeper'),
    (4, 'Really Heavy Sleeper')
]

sleep_school_list = [
    (1, 'Before 10 PM'), 
    (2, '10 PM to 12 AM'), 
    (3, '12 AM to 2 AM'),
    (4, 'After 2 AM')
]

sleep_weekend_list = [
    (1, 'Before 10 PM'), 
    (2, '10 PM to 12 AM'), 
    (3, '12 AM to 2 AM'),
    (4, 'After 2 AM')
]

awake_list = [
    (1, 'Before 5 AM'), 
    (2, '5 AM to 6 AM'), 
    (3, '6 AM to 7 AM'),
    (4, 'After 7 AM')
]

sleep_light_list = [
    (1, 'Completely dark'), 
    (5, 'Some lights here and there'),
    (9, 'As bright as possible'),
]

room_brightness_list = [
    (1, 'Completely dark'), 
    (5, 'Some lights here and there'),
    (9, 'As bright as possible'),
]

sound_list = [
    (1, 'Love playing music always'), 
    (3, 'Don\'t mind some music'), 
    (5, 'Prefer quiet, silence often')
]

sleep_noise_list = [
    (1, 'Complete silence'), 
    (2, 'Can tolerate low hums in the background'), 
    (3, 'Can tolerate voices or music, not too loud'),
    (4, 'Couldn\'t care less')
]

private_time_list = [
    (1, 'Minimal'), 
    (5, 'Not too much'), 
    (9, 'Lots of it'),
]

meditate_list = [
    (1, 'Yes'), 
    (9, 'No'), 
    (5, 'Sometimes'),
]

chatty_list = [
    (1, 'I love having conversations at any point in time'), 
    (3, 'I don\'t mind talking with the person I\'ll live with'), 
    (5, 'I don\'t want any kind of interactions'),
]

sharing_list = [
    (1, 'Yes'), 
    (9, 'No'), 
    (5, 'It depends...'),
]

visitors_list = [
    (1, 'Would love to have lots of people'),
    (5, 'I don\'t mind too many people'),
    (9, 'Just myself and my roommate'),
]

quiet_space_list = [
    (1, 'Utmost importance'), 
    (3, 'Sometimes'),
    (5, 'I love a social room'),
    (7, 'No preference'),
]

visiting_time_list = [
    (1, '9 PM sharp'), 
    (2, '10 PM sharp'), 
    (3, '11 PM sharp'),
    (4, 'Later than 11 PM'),
]

room_decor_list = [
    (1, 'Yes!!!'),
    (2, 'No preference'),
    (3, 'No'),
]

allergies1_list = [
    (1,'Yes'),
    (9, 'No'),
]



class StudentForm(forms.Form):
    student_number  = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"placeholder":"ALAXXXX-XXX",'class': 'form-control', 'style': 'width:auto;'}))

    full_name       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}))
    
    sex             = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style': 'border: 1px solid #dc3545;'}), choices=sex_list)

    region          = forms.CharField(max_length=20, widget=forms.Select(choices=region_list, attrs={'class':'form-control', 'style': 'width:50%;'}))

    country         = forms.CharField(widget=forms.Select(choices=country_list, attrs={'class':'form-control','style': 'width:50%;'}))

    year_group      = forms.ChoiceField(widget=forms.RadioSelect, choices=year_group)
    
    temperature     = forms.ChoiceField(label='How would you like the temperature in your room?',      widget=forms.RadioSelect, choices=temp_list)

    sleep = forms.ChoiceField(label='Would you consider yourself a...', widget=forms.RadioSelect, choices=sleeper_list)

    sleep_school_time  = forms.ChoiceField(label='What time do you usually go to sleep during school days?',widget=forms.RadioSelect, choices=sleep_school_list)

    sleep_weekend_time  = forms.ChoiceField(label='What time do you usually go to sleep during weekends?',widget=forms.RadioSelect, choices=sleep_weekend_list)

    wakeup_school_time = forms.ChoiceField(label='What time do you usually get up on school days?', widget=forms.RadioSelect, choices=awake_list)

    wakeup_weekend_time = forms.ChoiceField(label='What time do you usually get up on weekends?', widget=forms.RadioSelect, choices=awake_list)

    sleep_light = forms.ChoiceField(label='How sensitive are you to light when asleep?', 
                                    widget=forms.RadioSelect, 
                                    choices=sleep_light_list)

    room_brightness_day = forms.ChoiceField(label='How bright would you like your room to be during the day?', widget=forms.RadioSelect,choices=room_brightness_list)

    room_brightness_night = forms.ChoiceField(label='How bright would you like your room to be at night?', widget=forms.RadioSelect,choices=room_brightness_list)

    noise = forms.ChoiceField(label='Do you mind sound/music in your room?',widget=forms.RadioSelect, choices=sound_list)

    sleep_noise = forms.ChoiceField(label='How sensitive are you to sound when asleep?', widget=forms.RadioSelect, choices=sleep_noise_list)

    private_time = forms.ChoiceField(label='How much private time would you prefer', widget=forms.RadioSelect, choices=private_time_list)

    meditate = forms.ChoiceField(label='Do you like to pray or meditate in your room?', widget=forms.RadioSelect, choices=meditate_list)

    conversational = forms.ChoiceField(label='How conversational would you describe yourself to be?', widget=forms.RadioSelect, choices=chatty_list)

    sharing = forms.ChoiceField(label='Do you have a problem sharing things with your roommate',widget=forms.RadioSelect, choices=sharing_list)

    day_visitors = forms.ChoiceField(label='How open would you be to visitors in your room during the day?', widget=forms.RadioSelect,choices=visitors_list)

    night_visitors = forms.ChoiceField(label='How open would you be to visitors in your room at night?', widget=forms.RadioSelect,choices=visitors_list)

    visiting_time = forms.ChoiceField(label='What is the latest time for visitors?', widget=forms.RadioSelect,choices=visiting_time_list)

    quiet_space = forms.ChoiceField(label='How important is it that your room is a quiet space?', widget=forms.RadioSelect, choices=quiet_space_list)

    allergies = forms.ChoiceField(label='Do you have any allergies/conditions that require you to have a well-ventilated room?', widget=forms.RadioSelect, choices=allergies1_list)

    room_decor = forms.ChoiceField(label='Would you like to have room decorations?', widget=forms.RadioSelect, choices=room_decor_list)
