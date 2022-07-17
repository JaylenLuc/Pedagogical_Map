#interactive map
#jaylen ho luc

import folium
import pandas as pd
import json
import api_mod as api
import time
from folium.plugins import MousePosition
import time
from folium.plugins import Search
import requests

start1 = time.time()

main_map = folium.Map(
    location=[39.9042, 116.4074],   
    max_bounds = True,
    zoom_start = 3
)

formatter_lat = "function(num) {return L.Util.formatNum(num, 3) + ' º '+'N';};"
formatter_long = "function(num) {return L.Util.formatNum(num, 3) + ' º '+'E';};"


MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter_lat,
    lng_formatter=formatter_long,
).add_to(main_map)

add = '/tile/{z}/{y}/{x}'

#add more map textures later

maps = dict(Grey='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer',
            Divisional='https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer',
            Topographical='https://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer',
            Terrain= 'https://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer'
            )





c_search = folium.FeatureGroup(name='Countries',show=False,overlay=False, control=False)


#mcg = folium.plugins.MarkerCluster(control=False).add_to(main_map)
#main_map.add_child(mcg)
#cap = folium.plugins.MarkerCluster(name='Capitals',show=False).add_to(main_map)
# https://leafletjs.com/reference-1.7.1.html#path
colors = ''
fillColors = ''

sse = folium.FeatureGroup(name='Search Area')


#class to fetch api information
country_object = api.server_fetch()
#country_object.in_fetch()
csvfile = pd.read_csv((r'worldcities.csv'))
search_geo = {
            "type": "FeatureCollection",
            "features": []
        }

class nation:
    classification = []
    style_func_time = 0
    Sinosphere = ['MAC','HKG','CHN','PRK','KOR','JPN','TWN','SGP','VNM']
    Indo_China = ['LAO','THA','MMR','KHM','PHL','MYS','IDN','TLS']
    Hindustan = ['IND','PAK','BGD','LKA']
    Middle_East = ['IRN','IRQ','SYR','SYR','ISR','PSE','LBN',\
        'SAU','YEM','OMN','ARE','QAT','BHR','KWT','AFG','JOR']
    Turkistan = ['TKM','UZB','KAZ','KGZ','TJK','MNG']
    The_West = ['BMU','ALA','GIB','SMR','VAT','MLT','ESP','PRT','FRA','BEL','NLD','GBR','IRL',\
        'DEU','LUX','ITA','AND','CHE','AUT','DNK','NOR','SWE','FIN','EST','FRO','ISL',\
        'GRL','MCO','AUS','NZL']
    The_Orthodoxy = ['POL','LTU','LVA','BLR','UKR','CZE','SVK','HUN'\
        'ROU','BGR','HRV','SVN','BIH','GRC','TUR','MKD','ALB','RUS','CYP',\
        'SRB','MNE','MDA','ROU','HUN']
    Cushite = ['ETH','ERI','SOM','DJI']
    West_Africa = ['CPV','CIV','GHA','NGA','BEN','TGO','BFA','LBR','SLE','GIN','SEN',\
        'GNB','MLI','NER','CMR','GNQ','GAB']
    Bantoid = ['CAF','COD','COG','UGA','KEN','TZA','ZMB','AGO','MWI',\
        'MOZ','ZWE','NAM','BWA','RWA','BDI']
    South_Africa = ['ZAF','LSO']
    North_Africa = ['LBY','DZA','MAR','MRT','ESH','DZA','TUN','EGY','TCD']
    Sudan = ['SDN','SSD']
    Caucauses = ['GEO','ARM','AZE']
    Madagascar = ['COM','MDG','MUS']
    Melanesia = ['PNG','SLB','VUT','NCL']
    Micronesia = ['FSM','MHL','MNP','GUM','PLW','NRU','KIR']
    Polynesia = ['PYF','WSM','TUV','WLF','NIU','TON','NFK','COK','PCN','FJI']
    Himilayas = ['NPL','BTN']
    Euro_North = ['USA','CAN']
    Mexica = ['MEX','BLZ','GTM','HND','SLV','NIC','CRI','PAN']
    Tupi =['GUY','SUR','BRA']
    Inca = ['ECU','PER','BOL','CHL']
    SW_Am = ['ARG','URY','PRY','CHL']
    Gran_colombia = ['VEN','COL']
    Caribbean = ['CUB','DMA','HTI','TCA','DOM','BHS','JAM','PRI','ATG','MSR',\
        'KNA','VCT','TTO','BRB','GRD','LCA','CUW','ABW']


    @staticmethod
    def style_func(colorsz,fillColorsz,i,namez,name_n):
        colors = colorsz
        fillColors = fillColorsz
        bordersStyle={
            'color': f'{colors}',
            'weight':2,
            'fillColor':f'{fillColors}',
            'fillOpacity' : .2
        }
        #included in the tooltip popup::
         
        #print(i['properties']['ISO_A3'])
        

        #print(i['geometry']['coordinates'])

        st = time.time()
        #print(i['properties']['ISO_A3'])
       
        ht = country_object.form_str(i['properties']['ISO_A3'])

        en = time.time()
        
        html = f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<div style="white-space: normal"><b>Civilization</b>: \
            <pz>{namez}</pz><br>{ht}'
        geo = folium.features.GeoJson(
            i,
            #tooltip = folium.GeoJsonTooltip(fields=('ADMIN','ISO_A3',), aliases=('Nation-State','ALPHA3',)),
            tooltip= folium.Tooltip(text=folium.Html(html, script=True,width=500).render()),
            show = True,
            control = False,
            zoom_on_click = True,
            name = name_n,
            style_function=lambda x:bordersStyle)
       

        popup = folium.Popup('') #main thingy thing news api maybe maybe news api
        popup.add_to(geo)
        #c_search.add_child(geo)
        main_map.add_child(geo)

        #geo.add_to(main_map)

        #.add_to(main_map)
        #nation.classification.append(new_country)
#web scrap the gepjson file
ugh = time.time()
with open(r'countries.geojson') as open_f: #replace file path of the countries geojson file
    country_r = json.loads(open_f.read())
ughe = time.time()
print(f'open file: {ughe-ugh}')
func_time = 0
start2 = time.time()

#each country code has a value which is the style function maybe maybe not so much of a pain in the ass

#make this a lot shorter and cleawner and less bopilerplate by making a dicitonary 
#optimize style_func




for i in country_r['features']:
    #sinosphere
    if i['properties']['ISO_A3'] in nation.Sinosphere : 
        
        y = time.time()

        nation.style_func('#D12601','#D12601', i,"Sinosphere",i['properties']['ADMIN'])#pass in admin instead
        x = time.time()
        func_time += x-y
    #indo-china
    elif i['properties']['ISO_A3'] in nation.Indo_China: 
        y = time.time()
        nation.style_func('#cc8899','#cc8899', i,"Indo China",i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Hindustan
    elif i['properties']['ISO_A3'] in nation.Hindustan: 
        y = time.time()
        nation.style_func('#654321','#654321', i,"Hindustan",i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Middle East
    elif i['properties']['ISO_A3'] in nation.Middle_East:
        y = time.time()
        nation.style_func('#009000','#009000', i,"Middle East",i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Turkistan
    elif i['properties']['ISO_A3'] in nation.Turkistan: 
        y = time.time()
        nation.style_func('#09EBEE','#09EBEE', i,"Turkistan",i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #The West
    elif i['properties']['ISO_A3'] in nation.The_West: 
        y = time.time()
        nation.style_func('blue','blue', i,'The West',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #The Orthodoxy
    elif i['properties']['ISO_A3'] in nation.The_Orthodoxy: 
        y = time.time()
        nation.style_func('purple','purple', i,'The Orthodoxy',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Cushite
    elif  i['properties']['ISO_A3'] in nation.Cushite: 
        y = time.time()
        nation.style_func('#376550','#376550', i,'Cushite',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #West Africa
    elif i['properties']['ISO_A3'] in nation.West_Africa: 
        y = time.time()
        nation.style_func('#ff8c00','#ff8c00', i,'West Africa',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Bantoid
    elif i['properties']['ISO_A3'] in nation.Bantoid:
        y = time.time()
        nation. style_func('#FBC490','#FBC490', i,'Bantu',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #South Africa
    elif i['properties']['ISO_A3'] in nation.South_Africa: 
        y = time.time()
        nation.style_func('black','black', i,'South Africa',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #North Africa
    elif i['properties']['ISO_A3'] in nation.North_Africa: 
        y = time.time()
        nation.style_func('#00c300','#00c300', i,'North Africa',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Sudan
    elif i['properties']['ISO_A3'] in nation.Sudan: 
        y = time.time()
        nation.style_func('#FFCC00','#FFCC00', i,'Sudan',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #caucauses
    elif i['properties']['ISO_A3'] in nation.Caucauses:
        y = time.time()
        nation.style_func('#75816b','#75816b', i,'Caucauses',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #madagascar
    elif i['properties']['ISO_A3'] in nation.Madagascar: 
        y = time.time()
        nation.style_func('#800020','#800020', i,'Madagascar',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #melanesia
    elif i['properties']['ISO_A3'] in nation.Melanesia: 
        y = time.time()
        nation.style_func('#8da825','#8da825', i,'Melanesia',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Micronesia
    elif i['properties']['ISO_A3'] in nation.Micronesia: 
        y = time.time()
        nation.style_func('#00008B','#00008B', i,'Micronesia',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Polynesia
    elif i['properties']['ISO_A3'] in nation.Polynesia:
        y = time.time() 
        nation.style_func('#39FF14','#39FF14', i,'Polynesia',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Himilayas
    elif i['properties']['ISO_A3'] in nation.Himilayas: 
        y = time.time()
        nation.style_func('#ACD5F3','#ACD5F3', i,'The Himilayas',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Euro-North American Settler-Colonies
    elif i['properties']['ISO_A3'] in nation.Euro_North: 
        y = time.time()
        nation.style_func('#000080','#000080', i,'Euro-North American Settler-Colonies',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Mexican-occupied Mexica
    elif i['properties']['ISO_A3'] in nation.Mexica: 
        y = time.time()
        nation.style_func('#125454','#125454', i,'Spanish-occupied Mexica',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Portuguese-Occupied Tupi-Guarani
    elif i['properties']['ISO_A3'] in nation.Tupi: 
        y = time.time()
        nation.style_func('#F36196','#F36196', i,'Portuguese-Occupied Tupi-Guarani',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Spanish-Occupied Inca
    elif i['properties']['ISO_A3'] in nation.Inca: 
        y = time.time()
        nation.style_func('#C19A6B ','#C19A6B ', i,'Spanish-Occupied Inca',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Euro-Hispanic Occupied South-West America 
    elif i['properties']['ISO_A3'] in nation.SW_Am: 
        y = time.time()
        nation.style_func('#0d98ba ','#0d98ba ', i,'Euro-Hispanic Occupied South-West America ',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Gran_colombia
    elif i['properties']['ISO_A3'] in nation.Gran_colombia: 
        y = time.time()
        nation.style_func('#C49102 ','#C49102 ', i,'Grand colombia',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
    #Caribbean
    elif i['properties']['ISO_A3'] in nation.Caribbean: 
        y = time.time()
        nation.style_func('#00A36C ','#00A36C ', i,'Caribbean',i['properties']['ADMIN'])
        x = time.time()
        func_time += x-y
#findings: style func is quite fast but the for loop itself may be overbearing
end2 = time.time()
print(f'function fetch runtime: {func_time}')
print(f'breakpoint 2 runtime: {end2-start2} seconds')
#folium.GeoJsonTooltip(fields=['TYPE', 'R_STATEFP', 'L_STATEFP']).add_to(US_Geojson)

for map_name, url in maps.items():
    url+=add
    folium.TileLayer(
        url,
        name=map_name,
        attr='My attr').add_to(main_map)
#fg=folium.FeatureGroup(name='CIvilization', show=False)
#main_map.add_child(fg)

#adding cities to map
caps = folium.FeatureGroup(name='Capitals',show=False)
first = folium.FeatureGroup(name='First Level Admin Capital',show=False)
prov = folium.FeatureGroup(name='Province',show=False)
csvfile = pd.read_csv((r'worldcities.csv'))
capitals = csvfile[(csvfile['capital'] == 'primary')]
fir = csvfile[(csvfile['capital'] == 'admin')]
lowe = csvfile[(csvfile['capital'] == 'minor')]
#provinces = csvfile[(csvfile['capital'] == '')]
#popu = csvfile['population']
#icon = folium.features.CustomIcon('star.png',icon_size=(14, 14))
icon = "folium.Icon(color='red')" #High Population (>7,000,000)
icon2 = "folium.Icon(color='orange')"#'Medium Population (between 2,000,000 and 7,000,000)
icon3 = "folium.Icon(color='lightblue')"#Low Population (<2,000,000)
#icon_seach = "folium.Icon(color='lightblue')"
string1 = "first.add_child(folium.Marker("+\
        "location=[i['lat'], i['lng']],"+\
        "popup=folium.Popup(html=f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<b>First Level Admin Capital:</b> \
            {c}<br><b>Population:<b> <pz>{pop}</pz><br><b>Coordinates:</b>{long}º E / {lat}º N',"+\
        "max_width= 200),"+\
       " tooltip=f'<b>First subdivision Capital city:</b> {ci}',"


string2 = "caps.add_child(folium.Marker("+\
        "location=[v['lat'], v['lng']],"+\
        "popup=folium.Popup(html=f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<b>Capital city of:</b> \
            {vc}<br><b>Population:</b><pz> {vpop}</pz><br><b>Coordinates:</b>{vlong}º E / {vlat}º N',"+\
        "max_width= 200),"+\
       " tooltip=f'<b>Capital city:</b> {vci}',name=f'{vc}',"

#main_map.add_child(exec(FeatureGroupSubGroup(caps,string_cap,control=False)))
for (iind,i) in fir.iterrows():
    ci,c,pop,lat,long = i['city'],i['admin_name'],i['population'],i['lat'],i['lng']
    if float(pop) >= 7000000:
        colors = 'red'
        exec(string1 + f"icon= {icon}))")
    
    elif float(pop) < 7000000 and float(i['population']) >= 1000000 :
        colors = 'orange'
        exec(string1 + f"icon= {icon2}))")
    elif float(pop) < 1000000:
        colors = 'lightblue'
        exec(string1 + f"icon= {icon3}))")

        
for (vind, v) in capitals.iterrows():
    vci,vc,vpop,vlat,vlong = v['city'],v['country'],v['population'],v['lat'],v['lng']

    
    if float(vpop) >= 7000000:
        colors = 'red'
        exec(string2 + f"icon= {icon}))")
       
    elif float(vpop) < 7000000 and float(vpop) >= 1000000 :
        colors = 'orange'
        exec(string2 + f"icon= {icon2}))")

    elif float(vpop) < 1000000:
        colors = 'lightblue'
        exec(string2 + f"icon= {icon3}))")

    
#for i,d in capitals.iterrows():

    


main_map.add_child(caps)
main_map.add_child(first)




folium.TileLayer('Stamen Terrain').add_to(main_map)
folium.TileLayer('cartodbdark_matter').add_to(main_map)
folium.TileLayer('Stamen Toner').add_to(main_map)
folium.TileLayer('Stamen Water Color').add_to(main_map)
folium.TileLayer('cartodbpositron').add_to(main_map)




countryesearch = Search(
    layer = caps,
    geom_type = 'Polygon',
    search_label='name',
    placeholder='Search for a country',
    collapsed=False,
    search_zoom=7
    
).add_to(main_map)

end1 = time.time()
print(f'System runtime: {end1-start1} seconds')
print(f'form_str func time: {func_time} seconds')
print(f'API fetching {country_object.fetch_time}')
folium.LayerControl().add_to(main_map)
main_map.save('output.html')
#folium.GeoJson()

#folium.Marker(
#    location = []
#)