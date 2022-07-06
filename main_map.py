#interactive map
#jaylen ho luc, Neal Lowry
import folium
import pandas as pd
import json

main_map = folium.Map(
    location=[39.9042, 116.4074],   
    max_bounds = True,
    zoom_start = 3
)

add = '/tile/{z}/{y}/{x}'
#add more map textures later
maps = dict(Grey='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer',
            Divisional='https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer',
            Topographical='https://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer',
            Terrain= 'https://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer'
            )


# https://leafletjs.com/reference-1.7.1.html#path
colors = ''
fillColors = ''

sino = folium.FeatureGroup(name='Sinosphere')
indo = folium.FeatureGroup(name='Indo China')
hindu = folium.FeatureGroup(name='Hindustan')
ME = folium.FeatureGroup(name='Middle East')
turkistan = folium.FeatureGroup(name='Turkistan')
west = folium.FeatureGroup(name='The West')
orth = folium.FeatureGroup(name='The Orthodoxy')
cush = folium.FeatureGroup(name='Cushite')
westafr = folium.FeatureGroup(name='West Africa')
southafr = folium.FeatureGroup(name='South Africa')
bantu = folium.FeatureGroup(name='Bantu')
northafr = folium.FeatureGroup(name='North Africa')
sud = folium.FeatureGroup(name='Sudan')
cau = folium.FeatureGroup(name='Caucauses')
mada = folium.FeatureGroup(name='Madagascar')
mel = folium.FeatureGroup(name='Melanesia')
micro = folium.FeatureGroup(name='Micronesia')
poly = folium.FeatureGroup(name='Polynesia')
him = folium.FeatureGroup(name='The Himilayas')
euro_am = folium.FeatureGroup(name='Euro-North American Settler-Colonies')
Mexica = folium.FeatureGroup(name='Spanish-occupied Mexica')
Tupi = folium.FeatureGroup(name='Portuguese-Occupied Tupi-Guarani')
Inca = folium.FeatureGroup(name='Spanish-Occupied Inca')
Euro_Hispanic = folium.FeatureGroup(name='Euro-Hispanic Occupied South-West America ')
Gran_colombia = folium.FeatureGroup(name='Gran_colombia')
Caribbean = folium.FeatureGroup(name='Caribbean')

class nation:
    classification = []
    Sinosphere = ['CHN','PRK','KOR','JPN','TWN','SGP','VNM']
    Indo_China = ['LAO','THA','MMR','KHM','PHL','MYS','IDN','TLS']
    Hindustan = ['IND','PAK','BGD','LKA']
    Middle_East = ['IRN','IRQ','SYR','SYR','ISR','PSE','LBN',\
        'SAU','YEM','OMN','ARE','QAT','BHR','KWT','AFG','JOR']
    Turkistan = ['TKM','UZB','KAZ','KGZ','TJK','MNG']
    The_West = ['MLT','ESP','PRT','FRA','BEL','NLD','GBR','IRL',\
        'DEU','LUX','ITA','AND','CHE','AUT','DNK','NOR','SWE','FIN','EST','FRO','ISL',\
        'GRL','MCO','AUS','NZL']
    The_Orthodoxy = ['POL','LTU','LVA','BLR','UKR','CZE','SVK','HUN'\
        'ROU','BGR','HRV','SVN','BIH','GRC','TUR','MKD','ALB','RUS','CYP',\
        'SRB','MNE','MDA','ROU','HUN']
    Cushite = ['ETH','ERI','SOM','DJI']
    West_Africa = ['CIV','GHA','NGA','BEN','TGO','BFA','LBR','SLE','GIN','SEN',\
        'GNB','MLI','NER','CMR','GNQ','GAB']
    Bantoid = ['CAF','COD','COG','UGA','KEN','TZA','ZMB','AGO','MWI',\
        'MOZ','ZWE','NAM','BWA','RWA','BDI']
    South_Africa = ['ZAF','LSO']
    North_Africa = ['LBY','DZA','MAR','MRT','ESH','DZA','TUN','EGY','TCD']
    Sudan = ['SDN','SSD']
    Caucauses = ['GEO','ARM','AZE']
    Madagascar = ['COM','MDG','MUS']
    Melanesia = ['PNG','SLB','VUT','NCL']
    Micronesia = ['MHL','MNP','GUM','PLW','NRU','KIR']
    Polynesia = ['WSM','TUV','WLF','NIU','TON','NFK','COK','PCN','FJI']
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
        name_n.add_child(folium.GeoJson(
            i,
            tooltip = folium.GeoJsonTooltip(fields=('ADMIN',),
            aliases=('Nation-State',)),
            show = True,
            style_function=lambda x:bordersStyle))
        #.add_to(main_map)
        #nation.classification.append(new_country)

with open(r'C:\Users\Jaylen\Desktop\projects\countries.geojson') as open_f: #replace file path of the countries geojson file
    country_r = json.loads(open_f.read())
'''
print(len(nation.classification))
for i in range(6):
    print(nation.classification[i])
'''
for i in country_r['features']:
    #sinosphere
    if i['properties']['ISO_A3'] in nation.Sinosphere : nation.style_func('#D12601','#D12601', i,"Sinosphere",sino)
    #indo-china
    elif i['properties']['ISO_A3'] in nation.Indo_China: nation.style_func('#cc8899','#cc8899', i,"Indo China",indo)
    #Hindustan
    elif i['properties']['ISO_A3'] in nation.Hindustan: nation.style_func('#654321','#654321', i,"Hindustan",hindu)
    #Middle East
    elif i['properties']['ISO_A3'] in nation.Middle_East: nation.style_func('#009000','#009000', i,"Middle East",ME)
    #Turkistan
    elif i['properties']['ISO_A3'] in nation.Turkistan: nation.style_func('#09EBEE','#09EBEE', i,"Turkistan",turkistan)
    #The West
    elif i['properties']['ISO_A3'] in nation.The_West: nation.style_func('blue','blue', i,'The West',west)
    #The Orthodoxy
    elif i['properties']['ISO_A3'] in nation.The_Orthodoxy: nation.style_func('purple','purple', i,'The Orthodoxy',orth)
    #Cushite
    elif  i['properties']['ISO_A3'] in nation.Cushite: nation.style_func('#376550','#376550', i,'Cushite',cush)
    #West Africa
    elif i['properties']['ISO_A3'] in nation.West_Africa: nation.style_func('#ff8c00','#ff8c00', i,'West Africa',westafr)
    #Bantoid
    elif i['properties']['ISO_A3'] in nation.Bantoid:nation. style_func('#FBC490','#FBC490', i,'Bantu',bantu)
    #South Africa
    elif i['properties']['ISO_A3'] in nation.South_Africa: nation.style_func('black','black', i,'South Africa',southafr)
    #North Africa
    elif i['properties']['ISO_A3'] in nation.North_Africa: nation.style_func('#00c300','#00c300', i,'North Africa',northafr)
    #Sudan
    elif i['properties']['ISO_A3'] in nation.Sudan: nation.style_func('#FFCC00','#FFCC00', i,'Sudan',sud)
    #caucauses
    elif i['properties']['ISO_A3'] in nation.Caucauses:nation.style_func('#75816b','#75816b', i,'Caucauses',cau)

    #madagascar
    elif i['properties']['ISO_A3'] in nation.Madagascar: nation.style_func('#800020','#800020', i,'Madagascar',mada)
    #melanesia
    elif i['properties']['ISO_A3'] in nation.Melanesia: nation.style_func('#8da825','#8da825', i,'Melanesia',mel)
    #Micronesia
    elif i['properties']['ISO_A3'] in nation.Micronesia: nation.style_func('#00008B','#00008B', i,'Micronesia',micro)
    #Polynesia
    elif i['properties']['ISO_A3'] in nation.Polynesia: nation.style_func('#39FF14','#39FF14', i,'Polynesia',poly)
    #Himilayas
    elif i['properties']['ISO_A3'] in nation.Himilayas: nation.style_func('#ACD5F3','#ACD5F3', i,'The Himilayas',him)
    #Euro-North American Settler-Colonies
    elif i['properties']['ISO_A3'] in nation.Euro_North: nation.style_func('#000080','#000080', i,'Euro-North American Settler-Colonies',euro_am)
    #Mexican-occupied Mexica
    elif i['properties']['ISO_A3'] in nation.Mexica: nation.style_func('#125454','#125454', i,'Spanish-occupied Mexica',Mexica)
    #Portuguese-Occupied Tupi-Guarani
    elif i['properties']['ISO_A3'] in nation.Tupi: nation.style_func('#F36196','#F36196', i,'Portuguese-Occupied Tupi-Guarani',Tupi)
    #Spanish-Occupied Inca
    elif i['properties']['ISO_A3'] in nation.Inca: nation.style_func('#C19A6B ','#C19A6B ', i,'Spanish-Occupied Inca',Inca)
    #Euro-Hispanic Occupied South-West America 
    elif i['properties']['ISO_A3'] in nation.SW_Am: nation.style_func('#0d98ba ','#0d98ba ', i,'Euro-Hispanic Occupied South-West America ',Euro_Hispanic)
    #Gran_colombia
    elif i['properties']['ISO_A3'] in nation.Gran_colombia: nation.style_func('#C49102 ','#C49102 ', i,'Gran_colombia',Gran_colombia)
    #Caribbean
    elif i['properties']['ISO_A3'] in nation.Caribbean: nation.style_func('#00A36C ','#00A36C ', i,'Caribbean',Caribbean)

    

#folium.GeoJsonTooltip(fields=['TYPE', 'R_STATEFP', 'L_STATEFP']).add_to(US_Geojson)

for map_name, url in maps.items():
    url+=add
    folium.TileLayer(
        url,
        name=map_name,
        attr='My attr').add_to(main_map)
#fg=folium.FeatureGroup(name='CIvilization', show=False)
#main_map.add_child(fg)
main_map.add_child(sino)
main_map.add_child(indo)
main_map.add_child(hindu)
main_map.add_child(ME)
main_map.add_child(turkistan)
main_map.add_child(west)
main_map.add_child(orth)
main_map.add_child(cush)
main_map.add_child(westafr)
main_map.add_child(southafr)
main_map.add_child(bantu)
main_map.add_child(northafr)
main_map.add_child(sud)
main_map.add_child(cau)
main_map.add_child(mada)
main_map.add_child(mel)
main_map.add_child(micro)
main_map.add_child(poly)
main_map.add_child(euro_am)
main_map.add_child(Mexica)
main_map.add_child(Tupi)
main_map.add_child(Inca)
main_map.add_child(Gran_colombia )
main_map.add_child(Euro_Hispanic )
main_map.add_child(Caribbean )
main_map.add_child(him )
folium.TileLayer('Stamen Terrain').add_to(main_map)
folium.TileLayer('cartodbdark_matter').add_to(main_map)
folium.TileLayer('Stamen Toner').add_to(main_map)
folium.TileLayer('Stamen Water Color').add_to(main_map)
folium.TileLayer('cartodbpositron').add_to(main_map)
folium.LayerControl().add_to(main_map)
main_map.save('output.html')
#folium.GeoJson()

#folium.Marker(
#    location = []
#)