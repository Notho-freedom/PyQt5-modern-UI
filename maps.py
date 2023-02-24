# import folium library
import folium
########################################################################
## 
########################################################################
class MapCreator():
	print("Craeting a map")
	########################################################################
	## Create map object
	########################################################################
	mapObj = folium.Map(location=[35.068359, -6.751896],
	                    zoom_start=2)

	########################################################################
	## Create map marker for Nairobi
	########################################################################
	folium.Marker(location=[-1.28333, 36.81667],
	              icon=folium.Icon(icon='road', prefix='fa', color='black'),
	              popup=folium.Popup(
	                  """Building Uhuru Highway Fly-over
	                  """, max_width=500),
	              tooltip='Nairobi- Kenya'
	              ).add_to(mapObj)


	########################################################################
	## Create map marker for Pretoria
	########################################################################
	folium.Marker(location=[-25.740529, 28.212891],
	              icon=folium.Icon(icon='building', prefix='fa', color='green'),
	              popup=folium.Popup(
	                  """Building Construction
	                  """, max_width=500),
	              tooltip='Pretoria- South Africa'
	              ).add_to(mapObj)

	########################################################################
	## Create map marker for Bengazi
	########################################################################
	folium.Marker(location=[32.509762, 20.632324],
	              icon=folium.Icon(icon='plane', prefix='fa', color='purple'),
	              popup=folium.Popup(
	                  """Construction Of The Airport
	                  """, max_width=500),
	              tooltip='Bengazi - Libya'
	              ).add_to(mapObj)

	########################################################################
	## Create map marker for Alberta
	########################################################################
	folium.Marker(location=[55.341642, -115.400391],
				  icon=folium.Icon(icon='industry', prefix='fa', color='red'),
	              popup=folium.Popup(
	                  """Timber factory construction
	                  """, max_width=500),
	              tooltip='Alberta - Canada'
	              ).add_to(mapObj)


	########################################################################
	## Create map marker for Milan
	########################################################################
	folium.Marker(location=[45.490946, 9.173584],
				  icon=folium.Icon(icon='pencil', prefix='fa', color='orange'),
	              popup=folium.Popup(
	                  """Urban city planning
	                  """, max_width=500),
	              tooltip='Milan - Italy'
	              ).add_to(mapObj)	
	              

	########################################################################
	## Save the Html map object
	########################################################################
	mapObj.save('output.html')

	########################################################################
	## END
	########################################################################