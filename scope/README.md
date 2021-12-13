# Scope of OpenAlex

- OpenAlex (and similar databases of scholarly metadata ) hold information about several entities which are linked between them. 
- We distinguish between “core entities” (which are, arguably,  the entities around which the databases are build , which are then linked to other entities).  An imperfect term for this core entity is “scholarly output”. i.e. a work/product which scholars create (or contribute to its creation”). 
- We use the term “core entities” as shown in a simplified representation in the chart below. (We note that this representation could be improved , for example by including other entities, making a distinction between direct links - like citation - and indirect ones like co-citations … ) 
- The assessment of the scope is guided by two questions (we leave the question on metadata for the next section) 
  * Which entity types are included in OpenAlex (current version) ? 
  * Which entity types are missing - for our intended use case - and how can they be added ?

## 1. Which entity types are included in OpenAlex (current version) ? 

In the table "papers" we have two main fields which can give an indication of the type of documents in OpenAlex

* **DocType**    : taken from MAG. This field will be discontinued
* **Genre**    : provides the document categories from Crossref  

in addition, there are also two other fields which provide additional information ( *IsParatext*: indicating essentially front-matter and *DocSubTypes*: related to retraction status). 

In the table below provides an crosstabulation of the fields “doc_type” and “genre” 



The main/rough insight from the table is that, using the two fields, we have 
For only about a third of the records he two fields agree on the record_type
A third of records are of  “unknown type” (in both field) 
For another third the two fields d not agree on the type of records 



# 1.1 Using other information to reduce the number of records of “unknown type”  ? 

To test whether we can use information available elsewhere to reduce the number of the unknown records , we created a smaller subset of the papers table (filtering year = 2015).  This gives us 9.8 records 
A crosstabulation of doctype/genre is provided below 


## 1.1.1 using original venue 

The table “paper” has a field “original_venue” . 

In the 2015 subset, out of the 3.8 Mio of unknown type (doc_type and genre null) we have 2.2 Mio with an entry in “original_venue” 
The sheet “original_venue_top_entries” in the excel file “original_venue_and_urls” show the top entries i.e with over 500 entries (the non-english names are google-translated) 

=>  It seems that the field can be used to infer document type for some records, however considering that the top 250 entries (with at least 500 records) have a combined total of only about 320k entries , the long tail would cause a challenge 

## 1.1.2 using urls 

The table “papers_url”  provide the url to the record 

We have xx records with a url (out of those without doc_type, genre or original_venue) 
We extracted the url domain (using tldextract) and the top domains are provided in the sheet of the 

=> here also it seems that the url could be used, 

# 1.2 On the discrepancies on type of records  between “doc_type” (MAG) and “genre(Crossref) 

From the 2015 subset, it seems that some discrepancies may be based on different definitions. 

We have 6635 entries with genre=dataset  out of which 5418 (82 %) have as original venue the PsycTESTS database, a collection of unpublished  psychological tests and measurements.
On the other hand, what counts as dataset in "doc_type seem to be records from data repositories (PANGAE, DataverseNL, Inter-university Consortium for Political and Social Research (ICPSR)) 
or supplementary materials of journal articles




# 1.3 suggestion to identify record types 

In my view, identification of records could be made easier by creating two additional data fields with information on the source of the records. 

The development of a good taxonomy in both fields needs some time (and discussions  with Library Information specialists) but a rough idea of what is meant is provided below . 

1.3.1   primary source 

With primary source we mean the type of outlets in which the record has been “published” . The main  categories are shown in the table below 

There are problems with this categorization : for example a dataset can be published in the dataset repository and or as a “journal item” (e.g. supplementary material …). 



1.3.2  secondary source / certification channel … 
“Secondary source” refers here to the authoritative platform which “registers” the record. It would be often the same as the platform from which the record/metadata was taken but not always . 

This would be 






# 2. Which core entities are missing in OpenAlex  ? 
– to be discussed later – 
