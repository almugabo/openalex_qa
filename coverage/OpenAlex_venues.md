# Matching OpenAlex venues to Wikidata identifiers


Here we report on work done to match OpenAlex venues to Wikidata.

**tldr**:

- out of 97.225 scholarly journals in wikidata with an issn_l, 78% have an OpenAlex id (75.911) (up from 29k on March 11th)
- from the 112.215 venues with an issn_l in OpenAlex, 67% have a wikidata identifier (75.541)
- more work needed to match OpenAlex venues to wikidata (and other identifiers), the best way to help is to add OpenAlex ids to wikidata

**disclaimer:**
I am not the only the one adding OpenAlex identifiers to Wikidata. This builds on work of several other wikidata volunteers. The approach described here are the one I use.


## 1. Background / Motivation


Linking OpenAlex venues to wikidata can be helpful for multiple purposes. It can:

    (a) enhance OpenAlex interoperability
    (b) help in creating OpenAlex Collections (more on that later )
    (c) be useful in adding *venue type*  to OpenAlex
    (d) be used in analysis which make use of other metadata of venues (such as starting year, countries/regions of the venues publishers etc ..)

in addition, wikidata external identifiers can also he useful for the OpenAlex community for example
for

 (a) getting issn_l for OpenAlex venues for which it is missing.

 (b) assessing and improving the data quality in OpenAlex venues e.g help detect candidates duplicates and detect candidates of venues which needs to be split


## 2. Matching process

For the matchng, we use :

- OpenAlex venues dataset (version of 12 april 2022)
- Wikidata (quasi in "realtime" as retrieved via a SPARQL query - see below)

The matching can be tricky. Here various ways considered and the approach used here.

|approach | Pro | cons   |
|---------|-----|--------|
|Match by ISSNL | issn_l is the canonical id in OpenAlex | not all venues have issn_l - which should have it and ISSN_L my be wrongly recorded |  
|Match by ISSN Numbers | Issns numbers are supposed to be unique identifiers of journals | Issns are sometimes used inconsistently; can be obsolete |
|Matching by titles | Could be the only way in absence of identifiers | Can be difficult because titles may be inconsistently recorded (e.g. different languages or differently written) and some journals have very similar names  |
|Match by publications e.g. using DOI and then venues | Higher confidence one uses publication and venue | more work needed |

The approach used here to match only two venues if there are at least two elements from the above list which match (e.g. issn_l and title very similar).

In the future, we plan to match also by publications using open datasets (e.g. from CRIS systems etc...)


## 3. Data overview (so far)

##### 3.1 Wikidata Journals  (retrieved on 13th May 2022)


| set                              | counts     |
| ----------------------------     | ------------ |
|items which are scholarly journals	| 114,511 |
|items with issnl	| 97,225 |
|...with OpenAlex_id	| 75,911 |
|...with crossref_journal_id	| 68,109 |
|...with scopus_source_id|	33,818|
|...with era_journal_id	| 19,911|
|...with iso_4|	3,663|
|...with oclc_control_id|	6,696|
|...with danish_bif_id|	14,156|
|...with opencitation_id	|12,637|
|...with dimension_source_id|	2,360|
|...with springer_journal_id|	2,571|
|...with viaf_id|	884|
|...with fatcat_id|	378|

N.B:
the number of wikidata items more than doubled since March 11th, increasing from 29,150 to 61,897
(https://doi.org/10.5281/zenodo.6347127)




##### 3.1 OpenAlex (version 20220412)


| set                              | numbers |
| ----------------------------     | ------------- |
|Venues	|  124,066 |
|... Venues with issnl	| 112,215 |
|... Venues wth issnl and wikidata id	| 75,541|




## 3. Call for contribution

- the best way to help is to help edit wikidata by adding OpenAlex id
- additionally, by checking OpenAlex venues and signaling to OurResearch potentially problematic entries (duplicates, venues which need to be split)

N.B: I am aware that - as journals change (merge, are renamed ....) - what is considered "the same journal" can be a matter of perspective (and design choice)


## Annex : SPARQL queries

- adapted from various queries found online
- thanks also user https://stackoverflow.com/users/7879193/stanislav-kralin for his explanations on stackoverflow which helped craft the second query


```
# number of scholary journals in wikidata
SELECT  (COUNT (DISTINCT ?entity) AS ?entries)
WHERE
{
  ?entity wdt:P31/wdt:P279? wd:Q737498.
}

# number of scholarly journals with issn_l

SELECT  (COUNT (DISTINCT ?entity) AS ?entries)
WHERE
{
  ?entity wdt:P31/wdt:P279? wd:Q737498.
  ?entity wdt:P7363 ?xissnl.
}
```
and to create a  dataframe with identifiers

```
#!pip install wikidataintegrator
from wikidataintegrator import wdi_core, wdi_login

xQuery = '''
SELECT DISTINCT  ?entity ?entityLabel
                    ?xissnl ?ext_id_OpenAlex_id
                    ?ext_id_crossref_journal_id ?ext_id_nlm_unique_id
                    ?ext_id_era_journal_id ?ext_id_danish_bif_id
                    ?ext_id_scopus_source_id  ?ext_id_iso_4
                    ?ext_id_springer_journal_id ?ext_id_viaf_id         
                    ?ext_id_opencitation_id ?ext_id_oclc_control_id
                    ?ext_id_dimension_source_id ?ext_id_fatcat_id

                 (GROUP_CONCAT ( DISTINCT ?xissn; separator="; " ) AS ?xlist_issns )

            WHERE
            {
                ?entity wdt:P31/wdt:P279? wd:Q737498.
                ?entity wdt:P7363 ?xissnl.
                #OPTIONAL {?entity wdt:P7363 ?xissnl}.                
                OPTIONAL {?entity wdt:P10283 ?ext_id_OpenAlex_id}.
                OPTIONAL {?entity wdt:P8375 ?ext_id_crossref_journal_id}.
                OPTIONAL {?entity wdt:P105 ?ext_id_nlm_unique_id}.
                OPTIONAL {?entity wdt:P1058 ?ext_id_era_journal_id}.
                OPTIONAL {?entity wdt:P1250 ?ext_id_danish_bif_id}.
                OPTIONAL {?entity wdt:P1156 ?ext_id_scopus_source_id}.
                OPTIONAL {?entity wdt:P1160 ?ext_id_iso_4}.
                OPTIONAL {?entity wdt:P5983 ?ext_id_springer_journal_id}.         
                OPTIONAL {?entity wdt:P214 ?ext_id_viaf_id}.         
                OPTIONAL {?entity wdt:P3181 ?ext_id_opencitation_id}.
                OPTIONAL {?entity wdt:P243 ?ext_id_oclc_control_id}.
                OPTIONAL {?entity wdt:P6180 ?ext_id_dimension_source_id}.
                OPTIONAL {?entity wdt:P8608 ?ext_id_fatcat_id}.

                OPTIONAL {?entity wdt:P236 ?xissn}.            

                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en, de,fr, ru, " }
            }
            group by ?entity ?entityLabel
            ?xissnl ?ext_id_OpenAlex_id
            ?ext_id_crossref_journal_id ?ext_id_nlm_unique_id
            ?ext_id_era_journal_id ?ext_id_danish_bif_id
            ?ext_id_scopus_source_id  ?ext_id_iso_4
            ?ext_id_springer_journal_id ?ext_id_viaf_id         
            ?ext_id_opencitation_id ?ext_id_oclc_control_id
            ?ext_id_dimension_source_id ?ext_id_fatcat_id
'''


print(time.asctime())
dset_venue_OpenAlex = wdi_core.WDItemEngine.execute_sparql_query(xQuery , as_dataframe=True)

print(len(dset_venue_OpenAlex))



```
