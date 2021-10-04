# Geocoding a csv column of "addresses" in R

#load ggmap
library(ggmap)

# Select the file from the file chooser
#fileToLoad <- "~project2/adstanle/marcdloeb/geocoding/south_no_pre.csv (new = TRUE)"

# Read in the CSV data and store it in a variable 
origAddress <- read.csv("/project2/adstanle/marcdloeb/geocoding/east_no_suffix.csv", stringsAsFactors = FALSE)

# Initialize the data frame
geocoded_east_no_suffix <- data.frame(stringsAsFactors = FALSE)

# Loop through the addresses to get the latitude and longitude of each address and add it to the
# origAddress data frame in new columns lat and lon

origAddress

for(j in 1:nrow(origAddress)){
  
  print("Working...")
  print(j)
  result <- geocode(origAddress$full[j], output = "latlona", source = "google")
  origAddress$lon[j] <- as.numeric(result[1])
  origAddress$lat[j] <- as.numeric(result[2])
  origAddress$geoAddress[j] <- as.character(result[3])
  
}

# Write a CSV file containing origAddress to the working directory
filepath <- "/project2/adstanle/marcdloeb/geocoding/geocoded_east_no_suffix.csv"
write.csv(origAddress, filepath, row.names=FALSE)
