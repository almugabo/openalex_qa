# Addressing Inconsistencies in OpenAlex venue data  

## 1. Motivation
OpenAlex inherited from MAG a dataset with only about 50k “venues” disambiguated.  
It has done tremendous job in:
- disambiguation of the rest of venues (it has minted over 120k PID and matched most to issnl_l ) and
- in assigning works to them.

There are however some inconsistencies in the venue data which need to be addressed to improve the quality of OpenAlex data.

Here we highlight two – interrelated - types of inconsistencies in the data, which in our view, could be improved relatively easily

1. Label (names of journals)
2. Duplicates (venues which should be merged)



## 2. Examples of inconsistencies

N.B: we use **OpenAlex  20221010** release


Here an example of inconsistencies

|id|issn_l|display_name|
|--|------|------------|
|https://openalex.org/V4210216535|2807-2294|Academia|
|https://openalex.org/V4210179427|1012-8255|Academia|
|https://openalex.org/V4210180254|2622-8726|Academia|
|https://openalex.org/V192814187|0959-8138|BMJ|
|https://openalex.org/V4210185579|1756-1833|BMJ|
|https://openalex.org/V4210210398|1559-2464|Music supervisors' bulletin|
|https://openalex.org/V113086556||Music Supervisors' Bulletin|
|https://openalex.org/V4210210546|0090-0028|Nature|
|https://openalex.org/V137773608|0028-0836|Nature|
|https://openalex.org/V4210191612|0300-8746|Nature|
|https://openalex.org/V4210185689|1740-0287|New review of bioethics|
|https://openalex.org/V77440030||New Review of Bioethics|
|https://openalex.org/V4210237713|2469-9950|Physical review|
|https://openalex.org/V4210238307|2470-0010|Physical review|
|https://openalex.org/V4210168441|0556-2813|Physical review|
|https://openalex.org/V4210190737|0556-2821|Physical review|
|https://openalex.org/V4210190682|2469-9896|Physical review|
|https://openalex.org/V4210235286|2470-0045|Physical review|
|https://openalex.org/V4210210554|1550-2368|Physical review|
|https://openalex.org/V4210219937|0556-2791|Physical review|
|https://openalex.org/V4210174675|0163-1829|Physical review|
|https://openalex.org/V4210224030|1063-651X|Physical review|
|https://openalex.org/V4210208989|0556-2805|Physical review|
|https://openalex.org/V4210182288|2469-9926|Physical review|
|https://openalex.org/V54862371|0031-899X|Physical Review|
|https://openalex.org/V164566984|1050-2947|Physical Review A|
|https://openalex.org/V6791298|1098-0121|Physical Review B|
|https://openalex.org/V118093565|2469-9985|Physical Review C|
|https://openalex.org/V133490392||Physical Review D|
|https://openalex.org/V35412551|1539-3755|Physical Review E|
|https://openalex.org/V137042341|2160-3308|Physical Review X|
|https://openalex.org/V3880285|0036-8075|Science|
|https://openalex.org/V4210189058|2797-1031|Science|

In those case, there are three possibilities:
- (a) Journals are different but have in reality an identical name
- (b) Journals are different and mislabeled in OpenAlex (for example OpenAlex has only the first part of the name)
- (c) Journals are in fact the same journals, but the name in OpenAlex is written in slightly different way.

We refer to cases (a) and (b) as labeling issue and case (c) as a duplicate issue

In our view, this is also important for the newly created OpenAlex web interface (https://explore.openalex.org/) when using "venue" as search criteria.

N.B:
in the following we normalize the names of the journals  *trim(upper(display_name))*
**because in OpenAlex venue data, the “display name” is not normalized, we often have entries with slight variations in name**
such as  "Physical *review*" and "Physical *Review*" or "New *review* of bioethics" and "New *Review* of Bioethics"


## 3. Using a reference dataset as a method to identify and adress inconsistencies

One way to distinguish between a labeling and a duplicate issue is
- to match the works (or a selection of works) assigned to a given venue in OpenAlex to the work assigned to a venue in another reference set (for example using DOI).
- aggregate the venues in OpenAlex to the venues in the reference’s dataset.

With this, one can find indications of :
- **labeling issues** if the venue labels are different in OpenAlex and the reference dataset
- **duplicate issues** if the different OpenAlex ids point to the same venue in the reference dataset

We tested the use of Crossref as a reference dataset
- We used the dump of **april 2022**
- matched the works by DOI (uppercased in both dataset)
- as venue names in Crossref are not standardised, we used the label of the crossref issn_l associated with most work

The table below shows the results of this matching (after manually selecting crossref journals associated with most work)

|openalex_venue_id|openalex_venue_issnl|openalex_venue_name|cref_issn_min|cref_container_name|nr_articles|
|-----------------|--------------------|-------------------|-------------|-------------------|-----------|
|https://openalex.org/V4210179427|1012-8255|Academia|1012-8255|Academia Revista Latinoamericana de Administración|278|
|https://openalex.org/V4210180254|2622-8726|Academia|2622-8726|Academia: Jurnal Ilmu Sosial dan Humaniora|27|
|https://openalex.org/V4210216535|2807-2294|Academia|2807-1808|ACADEMIA: Jurnal Inovasi Riset Akademik|40|
|https://openalex.org/V192814187|0959-8138|BMJ|0959-8138|BMJ|405117|
|https://openalex.org/V4210185579|1756-1833|BMJ|1756-1833|BMJ|31974|
|https://openalex.org/V137773608|0028-0836|Nature|0028-0836|Nature|423604|
|https://openalex.org/V4210210546|0090-0028|Nature|0090-0028|Nature New Biology|2769|
|https://openalex.org/V4210191612|0300-8746|Nature|0300-8746|Nature Physical Science|2334|
|https://openalex.org/V4210219937|0556-2791|Physical review|0556-2791|Physical Review A|18206|
|https://openalex.org/V4210182288|2469-9926|Physical review|2469-9926|Physical Review A|16214|
|https://openalex.org/V4210174675|0163-1829|Physical review|0163-1829|Physical Review B|92605|
|https://openalex.org/V4210237713|2469-9950|Physical review|2469-9950|Physical Review B|32974|
|https://openalex.org/V4210208989|0556-2805|Physical review|0556-2805|Physical Review B|10577|
|https://openalex.org/V4210168441|0556-2813|Physical review|0556-2813|Physical Review C|36595|
|https://openalex.org/V4210190737|0556-2821|Physical review|0556-2821|Physical Review D|41315|
|https://openalex.org/V4210210554|1550-2368|Physical review|1550-2368|Physical Review D|34981|
|https://openalex.org/V4210238307|2470-0010|Physical review|2470-0010|Physical Review D|23688|
|https://openalex.org/V4210224030|1063-651X|Physical review|1063-651X|Physical Review E|21278|
|https://openalex.org/V4210235286|2470-0045|Physical review|2470-0045|Physical Review E|13394|
|https://openalex.org/V4210190682|2469-9896|Physical review|2469-9896|Physical Review Physics Education Research|627|
|https://openalex.org/V3880285|0036-8075|Science|0036-8075|Science|362561|
|https://openalex.org/V4210189058|2797-1031|Science|2797-0744|SCIENCE : Jurnal Inovasi Pendidikan Matematika dan IPA|56|



We see here for example that
- the data quality could be improved by changing the labels of such venues like "Academia, Nature, Physical review"
- this table also indicate where we may have duplicates (BMJ, Physical Review A) [see section 4 for discussion]

In our view, this shows that although approach is an imperfect (Crossref may also have errors for example), it can help in most of the cases .


#### Cases of journals with identical names

There are also - few - cases in which the venues have an identical names for example
- two journals called **Development** , one in economics and the other one in Biology.
- two venues with the same name one being a journal and the other a book series

In such cases, one could add further information to distinguish them (see example table below)
|openalex_venue_id|openalex_venue_displayname|proposed_new_venue_name|
|-----------------|--------------------------|-----------------------|
|https://openalex.org/V198620474|ACTA NEUROPATHOLOGICA|ACTA NEUROPATHOLOGICA|
|https://openalex.org/V4210201326|ACTA NEUROPATHOLOGICA|ACTA NEUROPATHOLOGICA SUPPLEMENTUM (book series)|
|https://openalex.org/V4210178434|ADVANCED MATERIALS AND TECHNOLOGIES|ADVANCED MATERIALS AND TECHNOLOGIES (book series)|
|https://openalex.org/V2765038284|ADVANCED MATERIALS AND TECHNOLOGIES|ADVANCED MATERIALS AND TECHNOLOGIES|
|https://openalex.org/V122441808|ADVANCES IN MATHEMATICS|ADVANCES IN MATHEMATICS|
|https://openalex.org/V4210184223|ADVANCES IN MATHEMATICS|ADVANCES IN MATHEMATICS: SCIENTIFIC JOURNAL|
|https://openalex.org/V4210205812|APPLIED SCIENCES|APPLIED SCIENCES -MDPI|
|https://openalex.org/V2736532880|APPLIED SCIENCES|APPLIED SCIENCES - APPS|
|https://openalex.org/V121830084|BIOSCIENCE|BIOSCIENCE - OUP|
|https://openalex.org/V4210201212|BIOSCIENCE|BIOSCIENCE - UNP|
|https://openalex.org/V117898428|CEREBRAL CORTEX|CEREBRAL CORTEX|
|https://openalex.org/V4210213823|CEREBRAL CORTEX|CEREBRAL CORTEX - Book Series|
|https://openalex.org/V152760256|CHEMICAL COMMUNICATIONS|CHEMICAL COMMUNICATIONS - ChemComm|
|https://openalex.org/V4210207732|CHEMICAL COMMUNICATIONS|CHEMICAL COMMUNICATIONS (LONDON)|
|https://openalex.org/V63392143|COMPUTER NETWORKS|COMPUTER NETWORKS|
|https://openalex.org/V4210231469|COMPUTER NETWORKS|COMPUTER NETWORKS (1976)|
|https://openalex.org/V4210228694|CRITICAL CARE|CRITICAL CARE - SPRINGER|
|https://openalex.org/V191417626|CRITICAL CARE|CRITICAL CARE - BMC|
|https://openalex.org/V4210189519|DEVELOPMENT|DEVELOPMENT - SID|
|https://openalex.org/V86558740|DEVELOPMENT|DEVELOPMENT|


## 4.The tricky cases of "duplicates"

One the "labeling issue" is adressed, it can point out to "duplicate" venues.
This however has to be done carefully because what is a "duplicate" is not always obvious because journals change:
for example
- by merging  
- by rebranding
- by transfer to different publishers (in case of which they seem to get new issn numbers)

There are also cases, in which a venue in OpenAlex has no work associated with it but has the same *normalized* name with another one which is associated with works.
This could be an indication that the venue without work is in a duplicate of the second one.  (see example below)

|id|issn_l|name_normalized|cited_by_count|
|--|------|---------------|--------------|
|https://openalex.org/V4210186651|2614-6339|ABDIMAS SILIWANGI|19|
|https://openalex.org/V4210220333|2614-7629|ABDIMAS SILIWANGI|0|
|https://openalex.org/V4210187670|1925-3621|ACADEMIC FORENSIC PATHOLOGY|1671|
|https://openalex.org/V2764848257||ACADEMIC FORENSIC PATHOLOGY|0|
|https://openalex.org/V4210171597|0810-5391|ACCOUNTING AND FINANCE|28351|
|https://openalex.org/V140643119||ACCOUNTING AND FINANCE|760|
|https://openalex.org/V4210207935|1439-2232|ADVANCED TEXTBOOKS IN CONTROL AND SIGNAL PROCESSING|7445|
|https://openalex.org/V4210177296|2510-3814|ADVANCED TEXTBOOKS IN CONTROL AND SIGNAL PROCESSING|0|
|https://openalex.org/V68090385|0105-4538|ALLERGY|374645|
|https://openalex.org/V4210172350|0108-1675|ALLERGY|0|
|https://openalex.org/V4210200754|0044-8249|ANGEWANDTE CHEMIE|1291268|
|https://openalex.org/V4210217132|0170-9046|ANGEWANDTE CHEMIE|0|
|https://openalex.org/V4210210661|0932-2140|ANGEWANDTE CHEMIE (1932)|0|
|https://openalex.org/V4210226177|2049-0801|ANNALS OF MEDICINE AND SURGERY|12039|
|https://openalex.org/V2764697058||ANNALS OF MEDICINE AND SURGERY|34|
|https://openalex.org/V4210233075|2146-2909|ANNALS OF PAEDIATRIC RHEUMATOLOGY|197|
|https://openalex.org/V2764568482||ANNALS OF PAEDIATRIC RHEUMATOLOGY|0|
|https://openalex.org/V131706786|1509-3859|ARTIFICIAL SATELLITES|1050|
|https://openalex.org/V4210209924|0208-841X|ARTIFICIAL SATELLITES|0|
|https://openalex.org/V70769875|1867-1381|ATMOSPHERIC MEASUREMENT TECHNIQUES|90625|
|https://openalex.org/V4210197165|1867-8610|ATMOSPHERIC MEASUREMENT TECHNIQUES|0|
|https://openalex.org/V175325897|1017-060X|BULLETIN OF THE IRANIAN MATHEMATICAL SOCIETY|2247|
|https://openalex.org/V4210189674|1018-6301|BULLETIN OF THE IRANIAN MATHEMATICAL SOCIETY|0|
|https://openalex.org/V119941230|2391-5412|CENTRAL EUROPEAN JOURNAL OF BIOLOGY|7852|
|https://openalex.org/V4210208118|1895-104X|CENTRAL EUROPEAN JOURNAL OF BIOLOGY|0|


## 5.Conclusions/Suggestions

- external (reference) datasets can help in detecting and adressing the inconsistencies in OpenAlex venue data
- here we used Crossref but other open data sets can be used as well (ed. pubmed/medline)
- In some cases, this may require to make decisions based on other information (e.g. deciding to "merge" journals. in our view, while different opinions may exists about that, any decision - as long as it is documented - is not problematic per se.
- adressing the inconsistencies is a task the user community can help OpenAlex team adress
