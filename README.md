# Hacklytics 2024 - Data-Driven Drug Rehabilitation Prediction 

## Project Summary 
### Inspiration 
* The inspiration behind our project stems from the urgent need to address the pervasive and escalating issue of substance abuse and relapse across the United States. Substance abuse disorders not only pose significant health risks to individuals but also exert a profound societal and economic burden. Despite concerted efforts, substance abuse continues to pose major public health concerns, affecting individuals of all ages, demographics, and socio-economic backgrounds. Our motivation lies in leveraging data-driven insights to shed light on the complex interplay of factors influencing relapse and to empower healthcare institutions and experts in combating the inexorable spread and continuation of substance abuse across the nation.  

### Purpose and Function
* The idea here is that we want to evaluate / analyze the factors that can theoretically contribute to a patient’s potential relapse pertaining to substance abuse.
  By analyzing existing SAMHSA data spanning 1992 - 2021, the team opted to create a predictive model that can accurately identify the most significant correlative factors for relapse.
  This, in conjunction with a variety of Tableau visualizations, provides valuable insight into America’s current substance abuse crisis and potential future actions to mitigate its consequences. 

### Methodology
* We used Python and Tableau alongside machine learning library tools to produce data-driven insights on patterns among patients admitted to drug rehabilitation institutions across the United States. Python libraries including pandas, numpy, and sci-kit learn were leveraged to optimize our dataset for the application of machine learning models such as random forests to predict the possibility of readmission, given a set of parameters for individual patients. Additionally, the team implemented a fully interactable dashboard using Gradio and HTML/CSS linked with Tableau to include geo visualizations of national health data to tell the story of the impact of psychoactive substances on institutional healthcare decisions and American society as a whole.
  
*Dataset Resource: https://www.datafiles.samhsa.gov/dataset/treatment-episode-data-set-admissions-2021-teds-2021-ds0001

### Challenges Faced
* The most prominent challenges involved locating and aggregating national health datasets pertaining to rehabilitative treatment that corresponded to our project’s particular use case and stated objective.
  Firstly, it is important to note the discordant practices and ethical health standards between different states as well as the prevalence of null values, where certain governments and institutions omit
  the collection of data in certain key areas, including education, employment status, waiting times before treatment, and others. Additionally, many of the datasets the team encountered were formatted such
  that values were encoded in a way that became difficult to interpret and/or visualize in a digestible manner.
### Accomplishments

### Lessons Learned
* Throughout the course of this project, the team achieved a greater understanding regarding the importance of normalizing large-scale datasets with respect to our specific use cases, as well as isolating features corresponding to higher levels of predictive significance. Given that this event constituted a first-time hackathon experience for several of our members, we also learned a great deal about the fundamental components of data science projects ranging from discovering real world business problems and integrating large-scale datasets to converging upon a rigorous and unique set of solutions. 

### Potential Areas for Expansion

---
