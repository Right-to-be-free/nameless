#empty the environment 
rm(list=ls())

#load the library
library(ggplot2)

#set working dorectory 
setwd("C:/Users/vikya/Downloads")

#load the dataset
police_data = read.csv("PAC_Complaints_2009_2012.csv", na.strings = "", stringsAsFactors = TRUE)
view(police_data)

#drop levels of empty strings for varaibles 
police_data = droplevels(police_data[!grepl("^\\s*$", police_data$SEX),,drop=FALSE])
police_data = droplevels(police_data[!grepl("^\\s*$", police_data$TYPE),,drop=FALSE])
police_data = droplevels(police_data[!grepl("^\\s*$", police_data$ACTION),,drop=FALSE])
police_data = droplevels(police_data[!grepl("^\\s*$", police_data$STATUS),,drop=FALSE])
str(police_data)
head(police_data)

#check for null values 
sum(is.na(police_data))

#total number of males and female complaints 
ggplot(police_data, aes(x = SEX)) +
  geom_bar(width=0.5, fill = "coral") +
  geom_text(stat='count', aes(label=stat(count)), vjust=-0.5) +
  theme_classic()

#Plotting status of the complained for each sex 
ggplot(police_data,aes(x=STATUS,y=..count..,fill=SEX))+
  geom_bar(position='stack')+
  labs(x="Complaint Status", y="Number of complaints", title="Status of complaints by SEX")+
  guides(fill=guide_legend(title = NULL))+coord_flip()


#Plotting Action on complaints with their status
ggplot(police_data,aes(x=ACTION,y=..count..,fill=STATUS))+
  geom_bar(position='stack')+
  labs(x="Action", y="No of complaints", 
       title="Action on complaints with their status")+ coord_flip()

# plotting histogram to see the age distribution of people
hist(police_data$AGE)

#plotting Age histogram of people with their sex and status distribution
ggplot(police_data,aes(x=AGE,y=..count..,fill=STATUS))+
  geom_histogram() +
  facet_wrap(~SEX) +
  theme_test() +
  labs(x="Age", y="No of complaints", 
       title="Age histogram dustribution with sex and status")+ coord_flip()

#plotting action of complaints with their sex and race distribution
ggplot(police_data,aes(x=SEX,y=..count..,fill=RACE))+
  geom_bar(width = 0.4) +
  facet_wrap(~ACTION) +
  theme_test() +
  labs(x="Sex", y="No of complaints", 
       title="Action of complaints with their sex and race distribution")+ coord_flip()

