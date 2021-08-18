from django.shortcuts import render
import phonenumbers
from phonenumbers import geocoder, carrier
from django.contrib import messages

# Create your views here.
def home(request):
    infodict = {}
    if request.method == 'POST':
        phone_num = request.POST.get('phone', '')
        if phone_num == '':
            infodict['error'] = "Please Enter Number"
            return render(request, 'app/home.html')
        else:
            track_num = phonenumbers.parse(phone_num, None)
            country = geocoder.country_name_for_number(track_num,"en")
            operator = carrier.name_for_number(track_num, "en")
            validity = phonenumbers.is_valid_number(track_num)
            if validity:
                message = "Number Is Valid"
            else:
                message = "Number Is Not Valid"
            
            infodict['cc'] = track_num
            infodict['country'] = country
            infodict['operator'] = operator
            infodict['validity'] = validity
            infodict['message'] = message
   
    context = {
        'result':infodict  
    }
    return render(request, 'app/home.html', context)