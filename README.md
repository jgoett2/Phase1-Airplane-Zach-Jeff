<img src='Images/plane.jpg'>

# Instructional Airplane Leasing Program

## Overview

This dataset details every accident investigated by the National Transportation Safety Board over the last 40 years.  This data details the make, models, weather conditions, flight phases, injuries, and deaths during each accident.  The data could potentially help organizations find correlations, and identify conditions of an airplane flight that make it safer.  

Key findings:
1. **Cessna** and **Piper** airplanes appear to offer better protection to its passengers during airplane accidents.
2. Accidents that occur during **taxi**, **takeoff**, and **landing** have the **lowest** fatalities rates.  Accidents that occur during **maneuvers** and **cruise** phases have the **highest** fatality rates. 
3. Flights occurring during the **summer** months tend to have **lower** fatality rates that flights occuring during the **winter** months.

## Business Problem

In order to choose safe airplanes for the flight school, we will investigate these business questions:
1. How does the make of the aircraft affect airplane safety?
2. How does the phase of flight affect the survivability of airplane accidents?
3. How do the time of year and weather conditions affect the survival rate an airplane accident? 

To measure airplane safety, we will consider the protection offered by the airplane during an accident.  We will look at this three different ways
- **Survive:** The fraction of accidents with no fatalities.  
- **Survival Rate:** The fraction of passengers killed during an accident
- **Injury Rate:** The fraction of passengers uninjured during an accident. 

## Data Understanding

## Intake Data 

In this analysis we read in the entire AviationData dataset.  For each record, we use the following data:
- Event Date
- Make of Airplane
- Accidents injured, killed, minor injuries, and uninjured passengers in each accident
- Phase of Flight and weather conditions

## Analysis

### Airplane Safety by Make of Aircraft
    
![png](Reports/Images/output_14_0.png)
    

![png](Reports/Images/output_15_0.png)


![png](Reports/Images/output_16_0.png)

### Model Safety
    
![png](Reports/Images/output_18_0.png)
    
    
![png](Reports/Images/output_19_0.png)
    
    
![png](Reports/Images/output_21_1.png)
    

### Airplane Safety during Phases of Flight
    
![png](Reports/Images/output_23_0.png)
    

![png](Reports/Images/output_24_0.png)
    


Calculating Heatmap

![png](Reports/Images/output_27_0.png)
    

### Airplane Safety during Different Months of the Year

![png](Reports/Images/output_29_0.png)
    

## Conclusions

* Consider __Cessna__ or __Piper__ makes (Cessna 172, 158, or Piper PA-28)
* Focus on safety during __climb__, __cruize__, and __maneuvering__ phases of flight
* Focus on safety during __winter__ flying.

## Next Steps

* Investigate the geopraphical locations of accidents to gain insight.
* Investigate weather conditions.
