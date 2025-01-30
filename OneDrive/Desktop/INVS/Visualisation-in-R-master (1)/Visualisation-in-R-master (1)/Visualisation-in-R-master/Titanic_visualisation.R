library(ggplot2)

titanic<-read.csv("C:\\Users\\dillu\\Documents\\Kaggle\\titanic\\Titanic.csv")

# set as factors
titanic$Pclass <-as.factor(titanic$Pclass)
titanic$Survived<-as.factor(titanic$Survived)
titanic$Sex<-as.factor(titanic$Sex)
titanic$Embarked<-as.factor(titanic$Embarked)

### first question what is the Survival rate

ggplot(data=titanic ,aes(x=Survived) )+geom_bar()

### Percentge of Surivival rate
prop.table(table(titanic$Survived))

### now moving to customisation

ggplot(data=titanic ,aes(x=Survived))+
  theme_bw()+
  geom_bar()+
  labs(y="passsenger Count",
        title="Survival rate")

### Survival rate by Gender 

ggplot(data=titanic ,aes(x=Sex,fill=Survived))+
  theme_bw()+
  geom_bar()+
  labs(y="passsenger Count",
       title="Survival rate by Gender")

#### Survival rate by class

ggplot(data=titanic ,aes(x=Pclass,fill=Survived))+
  theme_bw()+
  geom_bar()+
  labs(y="passsenger Count",
       title="Survival rate by class")

#### Survival rate by class and Gender 

ggplot(data=titanic ,aes(x=Sex,fill=Survived))+
  theme_bw()+
  facet_wrap(~Pclass)+
  geom_bar()+
  labs(y="passsenger Count",
       title="Survival rate by Gender and class")
######## till now we have focussed only on factor cols now we will check Numeric


# what is the percentage distribution of Ages
ggplot(data = titanic,aes(x=Age))+
  theme_bw()+
  geom_histogram(binwidth = 5)+
  labs(y= "Passenger count", 
        x=" Age (bin =5",
       title ="Titanic Age distribution")
  
# what is the Survival rate Ages

ggplot(data = titanic,aes(x=Age, fill= Survived))+
  theme_bw()+
  geom_histogram(binwidth = 5)+
  labs(y= "Passenger count", 
       x=" Age (bin =5",
       title ="Titanic Survival rate by age") 
  
## let's try box whisker plot 


ggplot(data = titanic,aes(y=Age, x= Survived))+
  theme_bw()+
  geom_boxplot()+
  labs(y= "Age", 
       x=" Survived",
       title ="Titanic Survival rate by age") 


# Survivability with age , class , sex Density plot

ggplot(data=titanic ,aes(x=Age,fill=Survived))+
  theme_bw()+
  facet_wrap(Sex ~Pclass)+
  geom_density(alpha =0.5)+
  labs(y="age ",
       x="Surivived",
       title="Survival rate by age, Gender and class")

ggplot(data=titanic ,aes(x=Age,fill=Survived))+
  theme_bw()+
  facet_wrap(Sex ~Pclass)+
  geom_histogram(binwidth =5)+
  labs(y="age ",
       x="Surivived",
       title="Survival rate by age, Gender and class")
