# Setting the working directory
setwd("C:/Users/Admin/Documents/Dell E6320/R  Datasets")
# Loading the libraries
library(tidyverse)
library(extrafont)
library(extrafontdb)


# Loading the data 
titanic_data <- read_csv("titanic_data.csv")
head(titanic_data)
      
#The column PassengerId can be removed. We also need to convert the Survived,Sex and Pclass to factors. 
#Survived is coded in 0s and 1s. Os for died and 1s for survived. We can recode Survived appropritely.
titanic_data <- titanic_data %>% 
  select(-1) %>% 
  mutate(Survived = factor(Survived, levels = c(0, 1), labels = c("Died", "Survived")),
         Sex = factor(Sex),
         Pclass = factor(Pclass))

head(titanic_data)
# We may want to visualize the overall survival rates. We can do this using tables or graphs.
# Table
table(titanic_data$Survived)

# Graph
titanic_data %>% 
  ggplot(aes(x = Survived)) +
  geom_bar(width = 0.4) +
  theme_classic() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman",face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold")
  ) +
  labs(title = "Overall Survival Rates", x = NULL, y = "Passenger count")
titanic_data %>% 
  ggplot(aes(x = Sex, fill = Survived)) +
  geom_bar(width = 0.4) +
  theme_classic() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman",face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates by Sex", x = NULL, y = "Passenger count")

titanic_data %>% 
  ggplot(aes(x = Pclass, fill = Survived)) +
  geom_bar(width = 0.4) +
  theme_classic() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman",face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates by Passenger Class", x = NULL, y = "Passenger count")
# Histogram
titanic_data %>% 
  ggplot(aes(x = Age, fill = Survived)) +
  geom_histogram() +
  theme_classic() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman",face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates by Age")

# Boxplot
titanic_data %>% 
  ggplot(aes(x = Survived, y = Age)) +
  geom_boxplot() +
  theme_classic() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman", face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates by Age", x = NULL)

titanic_data %>% 
  ggplot(aes(x = Sex, fill = Survived)) +
  geom_bar(width = 0.4) +
  facet_wrap(~ Pclass) +
  theme_test() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman", face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates Sex and Passenger class", x = NULL, y = "Passenger Count")
titanic_data %>% 
  ggplot(aes(x = Age, fill = Survived)) +
  geom_histogram() +
  facet_wrap(~Sex + Pclass) +
  theme_test() +
  theme(
    plot.title = element_text(family = "Times New Roman", hjust = 0.5),
    axis.text = element_text(family = "Times New Roman", face = "bold"),
    axis.title = element_text(family = "Times New Roman", face = "bold"),
    legend.title = element_blank(),
    legend.text = element_text(family = "Times New Roman")
    
  ) +
  labs(title = "Survival rates Age, Sex and Passenger class")
