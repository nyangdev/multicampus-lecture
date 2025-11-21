import folium

# https://www.google.com/maps/dir/''//data=!4m8!4m7!1m5!1m1!1s0x357ca50007befb21:0x8892754ec6bbe866!2m2!1d127.0733985!2d37.5481533!1m0?entry=ttu&g_ep=EgoyMDI1MDkyNC4wIKXMDSoASAFQAw%3D%3D
# 127.0733985 37.5481533
my_loc = folium.Map(location=[37.5481533, 127.0733985], zoom_start=100)

my_loc.save("visual01.html")