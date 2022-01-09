# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
def updated_damages_func(damages):
  for item in damages:
    if item == "Damages not recorded":
      updated_damages.append(item)
    elif item[-1] == "M":
      strip_prefixM = item.strip("M")
      convert_to_floatM = float(strip_prefixM) * conversion.get("M")
      updated_damages.append(convert_to_floatM)
    else :
      strip_prefixB = item.strip("B")
      convert_to_floatB = float(strip_prefixB) * conversion.get("B")
      updated_damages.append(convert_to_floatB)
  return updated_damages
      
# test function by updating damages
updated_damages_func(damages)
print(updated_damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
hurricanes = {}
def hurricane_dict():
  for index in range(len(names)):
    hurricanes[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index]}
  return hurricanes
hurricane_dict()
print(hurricanes)


# 3
# Organizing by Year
hurricane_by_year = {}
def hurricane_by_year_func():
  for item in hurricanes:
    current_year = hurricanes[item]["Year"]
    current_cane = hurricanes[item]
    if current_year in hurricane_by_year:
      hurricane_by_year[current_year].append(current_cane)
    else:
      hurricane_by_year[current_year] = [current_cane]
  return hurricane_by_year
        
# create a new dictionary of hurricanes with year and key
hurricane_by_year_func()
print(hurricane_by_year)

# 4
# Counting Damaged Areas
count_affected_areas = {}
def count_affected_areas_func():
    for item in hurricanes:
      for area in hurricanes[item]["Areas Affected"]:
        if area in count_affected_areas:
          count_affected_areas[area] += 1
        else:
          count_affected_areas[area] = 1
    return count_affected_areas
  
# create dictionary of areas to store the number of hurricanes involved in
count_affected_areas_func()
#print(count_affected_areas)

# 5 
# Calculating Maximum Hurricane Count

def max_area_check():
  max_area = ""
  max_area_count = 0    
  for area, value in count_affected_areas.items():
    if count_affected_areas[area] > max_area_count:
      max_area = area
      max_area_count = count_affected_areas[area]
  #print(max_area)
  #print(max_area_count)
  return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
max_count = max_area_check()
print(max_count)



# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane_func():
  deadliest_hurricane = ""
  highest_death = 0
  death_list=[]
  for key,value in hurricanes.items():
    death_list.append(value["Deaths"])
    for deaths in death_list:
      if deaths > highest_death:
        highest_death = deaths
        deadliest_hurricane = key
  return deadliest_hurricane, highest_death

# find highest mortality hurricane and the number of deaths
highest_mortality_hurricane = deadliest_hurricane_func()
print(highest_mortality_hurricane)
# 7
# Rating Hurricanes by Mortality
hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
def hurricane_by_mortality_func():
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  #hurricanes_by_mortality = {}
  for key,value in hurricanes.items():
    if value["Deaths"] == mortality_scale[0]:
      hurricanes_by_mortality[0].append(value["Name"])
    elif mortality_scale[0] < value["Deaths"] <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(value["Name"])
    elif mortality_scale[1] < value["Deaths"] <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(value["Name"])
    elif mortality_scale[2] < value["Deaths"] <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(value["Name"])
    elif mortality_scale[3] < value["Deaths"] <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(value["Name"])
    else:
      hurricanes_by_mortality[5].append(value["Name"])
  return hurricanes_by_mortality
# categorize hurricanes in new dictionary with mortality severity as key
print(hurricane_by_mortality_func())

# 8 Calculating Hurricane Maximum Damage
def max_damage_cane_func():
  max_damage_hurricane = ""
  max_damage = 0
  for key,value in hurricanes.items():
    if value["Damage"] == "Damages not recorded":
      continue
    elif value["Damage"] > max_damage:
      max_damage = value["Damage"]
      max_damage_hurricane = key
  return max_damage_hurricane, max_damage

# find highest damage inducing hurricane and its total cost
print(max_damage_cane_func())

# 9
# Rating Hurricanes by Damage
hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
def hurricanes_by_damage_func():
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for key,value in hurricanes.items():
    if value["Damage"] == "Damages not recorded":
      continue
    elif value["Damage"] == damage_scale[0]:
      hurricanes_by_damage[0].append(value["Name"])
    elif damage_scale[0] < value["Damage"] <= damage_scale[1]:
      hurricanes_by_damage[1].append(value["Name"])
    elif damage_scale[1] < value["Damage"] <= damage_scale[2]:
      hurricanes_by_damage[2].append(value["Name"])
    elif damage_scale[2] < value["Damage"] <= damage_scale[3]:
      hurricanes_by_damage[3].append(value["Name"])
    elif damage_scale[3] < value["Damage"] <= damage_scale[4]:
      hurricanes_by_damage[4].append(value["Name"])
    else:
      hurricanes_by_damage[5].append(value["Name"])
  return hurricanes_by_damage
  
# categorize hurricanes in new dictionary with damage severity as key
print(hurricanes_by_damage_func())