# Assessing and Improving data quality in OpenAlex

## 1. an opportunity for collective quality assurance of scientometric resources
* [OpenAlex](openalex.org/) will be released in January 2022. It strives to be a replacement for Microsoft Academic Graph (MAG) and as such be a large, comprehensive collection of scholarly publications and other research outputs. Its name is inspired by the Library of Alexandria and in its own description is “index of hundreds of millions of interconnected entities (scholarly papers, authors, institutions, and more) across the global research system.”

* OpenAlex is developed by OurResearch, an organization committed to the Principles of Open Scholarly Infrastructure [POSI principles](https://blog.ourresearch.org/posi/). This guarantees the openness of the data

* Open data (in sense of the POSI principles) offer several obvious advantages in comparison with the commercially licensed and/or restricted access and usage data incl. reproducibility and transparency of analysis based on them. In addition, it also enables the sharing of corrections of the data and enhancement made by the community of users: **this is often explicitly forbidden by commercial licenses**

* The data quality of bibliometric databases is a major concern in the users’ community. It has been a constant topic in bibliometric debates ([see list of about 100 papers on this](https://github.com/almugabo/open_metadata/wiki/Data-Quality-in-Scientometric--Databases---Datasets))  and is renewed every time a new database is created. Equally perennial has been calls to improve the situation and those calls – addressed mainly to the database providers – were the only thing the scientometric community could do.

* No bibliometric database is perfect and OpenAlex will be no exception.   Open databases, like OpenAlex, however make a big difference in terms of data quality: They offer an opportunity for collective data quality assurance and data enhancement. This is, in my view, one of the most important advantages of openness of the data. It mirrors, in some ways, the practises which made the open-source movement successful (enabling customization, open collaboration …)

> The objective of this repository is to share some work done on the assessing and improving the data quality in OpenAlex and hopefully link to other users working on the topic. 

* Talking about *open source*, the repo is more a testing ground for patches to suggest rather than a fork. 

## 2. What is meant by “Data Quality”?

* The “quality of data” is a judgement passed on a given dataset. But it cannot be made without the consideration of the context in which the dataset is to be used. In this sense, “data quality” is always context dependent. As a concept, it is best understood as  [“fitness for use in a given context”](https://en.wikipedia.org/wiki/Data_quality). Depending on the intended usage the same data can be considered high/acceptable quality or useless (for the purpose). 

* OpenAlex is likely to be used by several communities for different purposes. It cannot be expected that it will cover every aspect of each user community, but its openness allows the users to build upon its core components and create datasets most suitable for their needs. The focus here is the usage of scholarly data (mainly publications but also selected other scholarly results) both for **the study of science** and for **evaluative purposes** (especially the Monitoring and Evaluation of research funding programs).

* [Data Quality Management (DQM)](https://en.wikipedia.org/wiki/Data_quality)  has several dimensions such as completeness, accuracy, precision, timeliness  whose exact definition is also context dependent. For our purpose we will focus (in short and mid-term) on five aspects (1) coverage, (2) coverage (3) completeness (4) accuracy and (5) interoperability 

##### Figure 1: Dimensions of data quality prioritised in short/mid term


![DQM aspects ](/_images/Quality_Aspects.png)


#### Main questions: 
1. [**Scope**](https://github.com/almugabo/openalex_qa/tree/main/scope):
- Which entity types are included in OpenAlex ?
- Which entity types are missing? (assessed against a given usage scenario) 

2. [**Coverage**](https://github.com/almugabo/openalex_qa/tree/main/coverage):
- What is the coverage for each entity type? (assessed against a reference) 

3. **Completeness**
- How complete are the records (and associated metadata) for each entity type (assessed against a reference)

4. **Accuracy**
- How accurate are the records ? (assessed against a reference/”ground truth”)

5. **Interoperability**
- Which data can be externally linked? Which other datasets should be created? (assessed against a given usage scenario)



## 3. Caveats and Disclaimers and Caveats

* OpenAlex is still in its infancy. Documentation of how it is created, and future development plans are not yet released. As OpenAlex and the wider eco-system of open scholarly data evolve, this work will be periodically revised to avoid unnecessary duplication (the proverbial “re-inventing of the wheel”. For example, we may adapt it to the roadmap of OpenAlex development (or plans of other providers of open scholarly data)

* The repository includes personal thoughts, scripts, and results related to assessing the quality of data in OpenAlex and suggestions for improvements (*from the perspective of a one user*. The repository affiliated with OpenAlex and/or OurResearch and they cannot be held responsible for any of its imperfections. 

* Although related to some aspects of my work at the European Research Council Executive Agency (ERCEA), this is a personal repository. Any views expressed here are mine. They do not reflect the views or official positions of ERC or the European Commission.

* The scripts and datasets are provided here "as-is" and without warranty of any kind, express, implied, or otherwise.

## 4 Call for collaboration/contribution
* Any feedback/suggestions appreciated.

* Please contact me for collaboration /contribution if this work is of interest to you. If there are enough people interested, we may consider refactoring the repository and agree on its future organisation


```Disclaimer: any views expressed here are strictly in personal capacity ```
