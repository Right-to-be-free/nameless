#empty the environment 
rm(list=ls())
# set working directory to load data
getwd()
setwd("C:/Users/rishi/Desktop")

#load library
library(ggplot2); 
library(GGally)

# load data from csv file as chnage the strings into factors 
train_data = read.csv("train.csv", header=TRUE, sep=",", stringsAsFactors = TRUE)
summary(train_data)

#turn categorical variable into factors 
train_data$Survived <- as.factor(train_data$Survived)
# check for null values
sum(is.na(train_data))
sum(is.na(train_data$Age))

#remove the null values
train_data = na.omit(train_data)

library(GGally)
ggcorr(train_data,
       nbreaks = 6,
       label = TRUE,
       label_size = 3)

S#total number of people survived count
ggplot(train_data, aes(x = Survived)) +
  geom_bar(width=0.5, fill = "coral") +
  geom_text(stat='count', aes(label=stat(count)), vjust=-0.5) +
  theme_classic()

barplot(table(train_data$Survived))


#Plotting Survival of passengers by gender
ggplot(train_data,aes(x=Survived,y=..count..,fill=Sex))+
  geom_bar(position='stack')+
  labs(x="Passenger Status", y="# of Passengers", title="Survival of Passengers by sex")+
  guides(fill=guide_legend(title = NULL))+coord_flip()

#Plotting Survival by Class
ggplot(train_data,aes(x=Survived,y=..count..,fill=as.character(Pclass)))+
  geom_bar(position='stack')+
  labs(x="Status Of Passengers", y="# of Passengers", 
       title="Survival of Passengers by Class")+ coord_flip()

#Plotting survival by boarding site.
ggplot(train_data,aes(x=Survived,y=..count..,fill=Embarked))+
  geom_bar(position='dodge')+
  labs(x="Status Of Passengers", y="# of Passengers",
       title="Survival of Passengers by Boarding Site")+coord_flip()

#Plotting survival by boarding site & class
ggplot(train_data,aes(x=Pclass,y=..count..,fill=Embarked))+
  geom_bar(position='dodge')+
  labs(x="Class", y="# of Passengers", 
       title="Class of Passengers by Boarding Site")+ coord_flip()

#Plotting survival by age
ggplot(train_data, aes(x = Age)) +
  geom_density(fill="coral") +
  labs(x="Age", y="# of Passengers",
       title="Survival ofPassengers by Age")

# histogram of Sibsp  
hist(train_data$SibSp)
