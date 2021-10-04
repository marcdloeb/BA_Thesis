
library(stringr)
library(tidyverse)
myfiles <- data.frame(list.files("/project2/adstanle/marcdloeb/valid_output/east_no_suffix/"))



names(myfiles) <- "addr"
fcount <- nrow(myfiles)


mf2 <- str_split(myfiles$addr, "@")

#mf2[[2]][2]

#mf2[[2]][1]

valid_addresses <- data.frame(character(0), character(0), stringsAsFactors = FALSE) #"addr", "search") #(addr = "", search = "")     #(c("addr", "search"))
names(valid_addresses) <- c("addr", "search")

for (j in 1:fcount){
  print(j)
  addrz <- str_replace_all(mf2[[j]][2], "_", " ")
  searchz <- str_replace_all(mf2[[j]][1], "_", " ")
  full <-addrz
  print(addrz)
  print(searchz)
  #valid_addresses[j]$addr <- addrz
  #valid_addresses[j]$search <- searchz
  #valid_addresses %>% add_row(addr = addrz, search = searchz)
  valid_addresses[nrow(valid_addresses) + 1,] = list(addrz, searchz)
  
}

valid_addresses$city_state <- "Chicago, IL"

valid_addresses$full <- paste(valid_addresses$addr, valid_addresses$city_state, sep=', ')


valid_addresses

filepath <- "/project2/adstanle/marcdloeb/geocoding/east_no_suffix.csv"
write_csv(valid_addresses, filepath)
