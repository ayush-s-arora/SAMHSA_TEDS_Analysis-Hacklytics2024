# Hacklytics 2024
# NoLapse - Data-Driven Drug Rehabilitation Prediction 

## Project Summary 
### Inspiration ✨
* The inspiration behind our project stems from the urgent need to address the pervasive and escalating issue of substance abuse and relapse across the United States. Substance abuse disorders not only pose significant health risks to individuals but also exert a profound societal and economic burden. Despite concerted efforts, substance abuse continues to pose major public health concerns, affecting individuals of all ages, demographics, and socio-economic backgrounds. Our motivation lies in leveraging data-driven insights to shed light on the complex interplay of factors influencing relapse and to empower healthcare institutions and experts in combating the inexorable spread and continuation of substance abuse across the nation.  

### Purpose and Function 📝
* The idea here is that we want to evaluate / analyze the factors that can theoretically contribute to a patient’s potential relapse pertaining to substance abuse.
  By analyzing existing SAMHSA data spanning 1992 - 2021, the team opted to create a predictive model that can accurately identify the most significant correlative factors for relapse.
  This, in conjunction with a variety of Tableau visualizations, provides valuable insight into America’s current substance abuse crisis and potential future actions to mitigate its consequences. 

### Methodology ⌨️
* We used Python and Tableau alongside machine learning library tools to produce data-driven insights on patterns among patients admitted to drug rehabilitation institutions across the United States. Python libraries including pandas, numpy, and sci-kit learn were leveraged to optimize our dataset for the application of machine learning models such as random forests to predict the possibility of readmission, given a set of parameters for individual patients. Additionally, the team implemented a fully interactable dashboard using Gradio and HTML/CSS linked with Tableau to include geo visualizations of national health data to tell the story of the impact of psychoactive substances on institutional healthcare decisions and American society as a whole.
  
  - Dataset Resource: https://www.datafiles.samhsa.gov/dataset/treatment-episode-data-set-admissions-2021-teds-2021-ds0001

### Challenges Faced 💻
* The most prominent challenges involved locating and aggregating national health datasets pertaining to rehabilitative treatment that corresponded to our project’s particular use case and stated objective.
  Firstly, it is important to note the discordant practices and ethical health standards between different states as well as the prevalence of null values, where certain governments and institutions omit
  the collection of data in certain key areas, including education, employment status, waiting times before treatment, and others. Additionally, many of the datasets the team encountered were formatted such
  that values were encoded in a way that became difficult to interpret and/or visualize in a digestible manner.
### Accomplishments 🎉
* Aggregating diverse datasets: Among the most challenging obstacles from the onset of our development process was coming up with an actionable idea alongside the inclusion of appropriate datasets to facilitate our analysis. Our team successfully navigated these tasks and demonstrated the ability to overcome logistical barriers and compile and normalize a comprehensive dataset with which to accomplish our objectives. 
* Achieving higher model accuracy: One of our proudest achievements was the implementation of an appropriate predictive model whose outputs surpassed our initial accuracy expectations and early results. Our first linear regression model returned an accuracy of 15%, and the original random forest model returned 39% accuracy, compared to our final random forest model’s output at 71.72% accuracy. This demonstrated a remarkable improvement and provided a sense of relief among all of our team members. Overall, through rigorous testing and iteration, we were able to successfully develop a model with vastly improved performance metrics that afforded more reliable predictions for our target variable of relapse probabilities. 
* Implementing an interactive dashboard: Another significant accomplishment achieved by our team involved creating a user-friendly interface to illustrate our findings. By integrating Gradio, HTML/CSS, and Tableau, our team developed an interactable dashboard which enables users to intuitively explore our data-driven insights with ease. 
* Learning and growth: As a team, we faced the challenges and learning opportunities presented by this event with confidence. In fact, this was the first hackathon experience for two of our group members, and we believe that we obtained substantial results in spite of the circumstances. From tailoring complex datasets to refining data science techniques, each member gained valuable experience that will hopefully yield dividends for each of our respective future careers. 


### Lessons Learned 📚
* Throughout the course of this project, the team achieved a greater understanding regarding the importance of normalizing large-scale datasets with respect to our specific use cases, as well as isolating features corresponding to higher levels of predictive significance. Given that this event constituted a first-time hackathon experience for several of our members, we also learned a great deal about the fundamental components of data science projects ranging from discovering real world business problems and integrating large-scale datasets to converging upon a rigorous and unique set of solutions. 

### Potential Areas for Expansion 🚀
Moving forward, our team is committed to further enhancing the capabilities and impact of our project. Here are some key areas we plan to focus on:
* Experimenting with more models: While our current random forest model has shown promising results, we acknowledge the importance of testing  additional machine learning algorithms to unveil deeper insights. By experimenting with various models, we will strive to refine our predictive accuracy and identify the most effective approach for forecasting relapse probabilities with respect to the most relevant factors. Additionally, expanding our dataset pool is essential for enriching our analysis and uncovering a more comprehensive framework for substance abuse trends and forecasts. We therefore acknowledge the potential benefits of integrating additional datasets from a diverse range of sources including research institutions, public agencies, and industry healthcare providers. Specifically for our existing dataset, we would like to address omissions in data for states such as Washington, Oregon, Idaho, and Delaware to promote more expansive geographical coverage and representativeness. 
* Continued optimization: Optimization is an ongoing process, and we are committed to fine-tuning our models to achieve even greater precision and reliability. This involves refining feature selection, hyperparameter tuning, and performance evaluation techniques to ensure optimal performance across unseen datasets and new conditions. 
* Addressing missing values: Missing data entries can significantly impact the robustness of our analysis and model outputs. We have a set of initial ideas for developing strategies to handle missing values effectively, such as imputation techniques, data augmentation, and specified data collection efforts. By mitigating the impact of missing values, we hope to improve the reliability and generalizability of our findings.
* Stakeholder Management: We believe that open collaboration with healthcare professionals and public institutions is vital for translating our initial insights into actionable strategies to affect real-world change. In future stages, we hope to engage with relevant stakeholders to garner feedback, streamline our findings, and cooperate in developing solutions that could potentially alleviate the maladaptive impacts addressed by substance abuse prevention and treatment. 


---
