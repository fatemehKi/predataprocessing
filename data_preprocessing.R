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
                        
ataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
