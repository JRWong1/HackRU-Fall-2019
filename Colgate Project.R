install.packages("rmarkdown")
library(rmarkdown)

ColgateData <- read.csv(file="C:/Users/tonys/OneDrive/Documents/R/hack_ru2(1).csv")

## Removes the columns "ingredients" and "x"
TempData <- subset(ColgateData, select = -X)
## Linear model to get the weights
Model <- lm(price_per_100g_ml_dollars ~ ., data = TempData)
ModelSummary <- summary(Model)
ModelCoeffs <- ModelSummary$coefficients

## creates number variables that describe unique number of each categorical variable
numCountries <- length(unique(ColgateData$country))
numCompanies <- length(unique(ColgateData$company))
numIngredients <- length(TempData)-5
  
##writes the coefficient data into 
write.csv(ModelCoeffs, file = "Coeff4.csv")
