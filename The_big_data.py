
import json
with open('precipitation.json') as file:
    rain_levels = json.load(file) 
    print(rain_levels) #printing all data for all stations

# precipitation values for Seattle
seattle_levels = [0]*12
for entry in rain_levels:
   if entry['station'] == 'GHCND:US1WAKG0038':
        #seattle_levels.append(entry) 
        # calculating total values of seattle precipitation per month
        months = int(entry['date'].split('-')[1]) # turning monthly date values into integers
        seattle_levels[months - 1] += entry['value'] # ensuring that values are added together to result in total monthly precip

print(seattle_levels)

# calculating total annual level of precipitation for seattle.
total_rainfall = sum(seattle_levels)
print(total_rainfall)

# calculating monthly percentage based on total annual precip
monthly_percentages = [x / total_rainfall for x in seattle_levels]
print(monthly_percentages)

# converting final results into a json file
with open('result.json', 'w') as file:
    json.dump(seattle_levels, file),
    json.dump(total_rainfall, file),
    json.dump(monthly_percentages, file)
    






   