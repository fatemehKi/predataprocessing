# importing the adtaset

dataset = read.csv('Data.csv')

#taking care of missing data in Age
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

#taking care of missing data in Salary
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)
                        
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
                        
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))

                        
#Splitting the edataset
#install.packages('caTools')
library(caTools)
set.seed(123)
split= sample.split(dataset$Purchased, SplitRatio = 0.8)
