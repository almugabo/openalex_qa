# Feedback on the venues data in OpenAlex  November release (v20221114)


The OpenAlex November release (v20221114) makes a range of improvements/enhancements to the venues data.
* it added about 100k new venues ids , increasing the number of venues from about 123k to 226k (when compared to the release v20221010)
* it adds the "venue type"
* adds external ids (Wikidata, which will increase interoperablity and retrieval of other venues data that Wikidata holds) (see also:
[Matching OpenAlex venues to Wikidata identifiers](https://github.com/almugabo/openalex_qa/blob/main/coverage/OpenAlex_venues.md)  )

Here an overview of the data type in November release and of the new venues added

**Table 1: Overview of data type in OpenAlex venues**

|venue_type|venue_ids|venue_ids_new|
|----------|---------|-------------|
|journal|190.995|67.112|
|ebook platform|28.541|28.541|
|conference|4.540|4.540|
|repository|2.650|2.648|

it seems that, although the most venues added are journals (67k), all ebook platforms ids (~ 29k) have been created in the November edition.

Here we provide feedback on journals, which we believe may help increase the data quality on two issues.

**(1) some problematic issn_l**

**(2) venues types**

not adressed here is the issue of "duplicates and journal titles" , on which feedback was provided earlier: [Detecting and Adressing inconsistencies in Openalex venue data](https://github.com/almugabo/openalex_qa/blob/main/coverage/inconsistencies_in_venue_data.md).

See also [a table with proposed new journal names](https://github.com/almugabo/openalex_qa/blob/main/coverage/proposed_journal_names.md)


## 1. Problematic issn_l

ISSN-LINKING promises to solves the issues of journals having several and changing issns. It is interesting because

- more and more journals lists are using it
- although the ISSN data are not openely available  , the ISSN portal provides a concordance table between issn and issn_l and vice versa
https://www.issn.org/services/online-services/access-to-issn-l-table/

However, we found some problems in ISSN Linking in OpenAlex.

1. About 580 venues include an issn_l id which is in fact not an issn_l but
- either regular issns or refer to "cancelled"

examples
https://openalex.org/V92813228	*current issnl:* 1110-5704  *African Journal of Urology*    **correct issn_l** : https://portal.issn.org/resource/ISSN/1961-9987
https://openalex.org/V2764857279	*current issnl:*0305-862X  *African research and documentation*  **correct issn_l**: https://portal.issn.org/resource/ISSN/2755-1369

- or so called *cancelled records*

examples :

https://openalex.org/V2480243177	*current issnl:* 0379-5292	*Austrian Journal of Forest Science*	**correct issn_l**: https://portal.issn.org/resource/ISSN/0008-9583
https://openalex.org/V4210223565	*current issnl:* 2651-4710	*Asian Journal of Nanoscience and Materials*	**correct issnl**: https://portal.issn.org/resource/ISSN/2588-669X


2. Another 560 have issn_l which refer to non-resolved issn on the ISSN Portal

examples:

https://openalex.org/V46132323	*Israel Medical Association Journal* 	**Unreported record** 	https://portal.issn.org/resource/ISSN/1565-1088
https://openalex.org/V4212762986	*African Journal of Economic Review* 	**Awaiting validation record**	https://portal.issn.org/resource/ISSN/1821-8148
https://openalex.org/V2764615179	*Philippine Journal of Veterinary and Animal Sciences* **ERROR: not resolved at all** https://portal.issn.org/resource/ISSN/0155-2173
https://openalex.org/V2764877152	*Journal of Alabama Archaeology*	**Legacy record**	https://portal.issn.org/resource/ISSN/0449-2153
https://openalex.org/V2764899306	*Kuwait chapter of Arabian Journal of Business & Management Review*	**Suppressed record**	https://portal.issn.org/resource/ISSN/2224-8358


## 2. Venue type

It fair to say that the **venue type** is one of the most important development some users have been waiting for.
(it helps a lot in clarifying some of the confusion caused by the MAG legacy about which documents OpenAlex has)

It seems however that the classification to the type "journal" was done on the basis of whether or not a venue has an issn. In my view, this unfortunately lump together "journals" and all other type of serials (such as book series or conference proceeding series).

examples

https://openalex.org/V43790123	journal	0065-2598	Advances in Experimental Medicine and Biology	http://www.springer.com/series/5584
https://openalex.org/V177811526	journal	0091-679X	Methods in Cell Biology	https://www.sciencedirect.com/bookseries/methods-in-cell-biology
https://openalex.org/V124985173	journal	0084-0173	Wildlife Monographs	https://wildlife.onlinelibrary.wiley.com/journal/19385455
https://openalex.org/V53376162	journal	0265-7651	Oxford Studies in Ancient Philosophy	http://ukcatalogue.oup.com/category/academic/series/philosophy/osap.do
https://openalex.org/V4210226853	journal	1866-2609	Springer topics in signal processing	link: https://www.springer.com/series/8109


In the absence of a authority list of journals/book series/conference series, it can be indeed difficult to distinguish between them, but for most of them the distinction can be made with reasonably well (at least with a reasonable degree of agreements).

Proposed two options to address this :
- **Option 1** : OpenAlex could change the current label in "type" from "Journal" to **"Serial"**. This would be more accurate as the fact of having issns only indicate the "serial" character of the venue" and not the fact that it is a journal.

- **Option 2**: OpenAlex introduces a new label **"book series"** and "crowd-source" to the community classification of the venues (as it has been done in the past with the societies).  [in some cases, there might not be consensus, but those cases could be clearly indicated in the documentation]
