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
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import json
import folium

m = None
marker = None
lat = lng =0
@csrf_protect
def index(request):
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

    m = folium.Map(location=[11.504479, 77.2749852], zoom_start=2) 
    print(lat)
    
    marker = folium.Marker([lat,lng])
    marker.add_to(m)
    #print(marker.location)
    context = {
        'm': m._repr_html_()
    }
    #print(context['m'])
    return render(request, 'index1.html', context)