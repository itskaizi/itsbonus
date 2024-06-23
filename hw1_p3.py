C = 299792458    #speedoflight
Alpha_Centauri = 4.3   #AlphaCentauri:4.3LightYears
Barnard_Star = 6.0   #Barnard’sStar:6.0LightYears
Betelgeuse = 309   #Betelgeuse(intheMilkyWay):309LightYears
Andromeda_Galaxy = 2000000   #AndromedaGalaxy(closestgalaxy):2000000LightYears

Velocity = float(input(" Input velocity: "))
index  = 1 - (Velocity**2 )/(C**2)
Denominator = index**0.5
Gamma = 1/(Denominator)
Speed_of_light_u_ship = Velocity/C

Delta_ship_Alpha_Centauri = Alpha_Centauri / Gamma  #Travel time to Alpha Centaur
Delta_ship_Barnard_Star =  Barnard_Star / Gamma #Travel time to Barnard's Star
Delta_ship_Betelgeuse = Betelgeuse / Gamma
Delta_ship_Andromeda_Galaxy = Andromeda_Galaxy / Gamma

print("Percentage of light speed:", Speed_of_light_u_ship)
print("Travel time to Alpha Centauri =", Delta_ship_Alpha_Centauri)
print("Travel time to Barnard's Star =", Delta_ship_Barnard_Star)
print("Travel time to Betelgeuse (in the Milky Way) =", Delta_ship_Betelgeuse)
print("Travel time to Andromeda Galaxy (closest galaxy) =", Delta_ship_Andromeda