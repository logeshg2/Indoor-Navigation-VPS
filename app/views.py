# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
# import json
# import folium
# import folium.map

# # Create your views here.
# @csrf_protect
# def index(request):
#     def post(request):
#         lat=lng=0
#         print(request.body)
#         try:
#             data = json.loads(request.body)
#             if data:
#                 print(data)
#                 lat = data.latitude
#                 lng = data.longitude
#         except Exception as e: 
#             print(e)
#         return float(lat),float(lng)

#         #print(data['coord'])

#     # map object:
#     m = folium.Map()
#     folium.Marker([post(request)[0],post(request)[1]]).add_to(m)
#     m = m._repr_html_()


#     context = {
#         'm' : m
#     }
#     return render(request, 'index1.html', context)
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
import json
import folium

m = None
marker = None
lat = 0
lng = 0
@csrf_protect
def show_map(request):
    #lat = 0.0
    #lng = 0.0
    global m, marker,lat,lng

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lat = data.get('coord', [0, 0])[0]
            lng = data.get('coord', [0, 0])[1]
        except Exception as e:
            print(e)

    # m = folium.Map(location=[lat,lng], zoom_start=15) 
    # #print(lat)
    # marker = folium.Marker([lat,lng])
    # marker.add_to(m)

    # #print(marker.location)
    # context = {
    #     'm': m._repr_html_()
    # }
    # #print(context['m'])
    return render(request, 'show_map.html')

def index(request):
    return login_view(request)
    # return render(request,'login.html')

def login_view(request):
    return render(request, 'login.html')

def admin_login(request):
    # Logic for Admin Login (similar to earlier)
    return render(request, 'admin_login.html')

def student_login(request):
    # Logic for Student Login (similar to earlier)
    return render(request, 'student_login.html')

def guest_dashboard(request):
    # Logic for Guest Access
    return show_map(request)
    # return render(request, 'show_map.html') # the map loads as default for guest
