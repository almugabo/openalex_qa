#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:51:25 2022

@author: mike

process openalex files 
based on Richard's scripts 


"""

import csv
#import glob
import gzip
import json
import os

#import time 

# initialize csv writer 
def init_dict_writer(csv_file, lst_columns, **kwargs):
    writer = csv.DictWriter(csv_file, 
                            fieldnames=lst_columns, 
                            **kwargs
                           )
    
    writer.writeheader()
    return writer

# Processfile 
# parameter : jsonl_file_name

def process_file_work(jsonl_file_name, CSV_DIR, verbose = False):
    
    '''
    will extract data and write csv for DB import 
    
    TO DO : 
    - put hard coded parts in a yaml file (which also is used to create postgresql tables)
    - change the file objects to allow a function to write in the file (would be easier to maintain and possible isolate parts which may cause errors)
    
    -- ADD host_venue_id in works 
    
    
    '''


    ## ------------------------------------
    # prepare CSV files for the results
    ## -----------------------------------

    xfilename_csv_suffix =  jsonl_file_name.split('=')[1].replace('-', '').replace('/', '_').replace('.gz', '.csv')  ## unique name 
    ## initialize names of file 
    csv_filename_works = os.path.join(CSV_DIR, 'works_' + xfilename_csv_suffix ) 
    csv_filename_alternate_host_venues = os.path.join(CSV_DIR,'alternate_host_venues_'  + xfilename_csv_suffix ) 
    csv_filename_authorships = os.path.join(CSV_DIR,'authorships_' + xfilename_csv_suffix ) 
    csv_filename_biblio = os.path.join(CSV_DIR,'biblio_' + xfilename_csv_suffix ) 
    csv_filename_concepts = os.path.join(CSV_DIR,'concepts_' + xfilename_csv_suffix ) 
    csv_filename_ids = os.path.join(CSV_DIR,'ids_' + xfilename_csv_suffix ) 
    csv_filename_mesh = os.path.join(CSV_DIR,'mesh_' + xfilename_csv_suffix ) 
    csv_filename_open_access =  os.path.join(CSV_DIR,'open_access_' + xfilename_csv_suffix ) 
    csv_filename_referenced_works =  os.path.join(CSV_DIR,'referenced_works_' + xfilename_csv_suffix ) 
    #csv_filename_related_works =  os.path.join(CSV_DIR,'related_works_' + xfilename_csv_suffix ) 
    csv_filename_host_venue =  os.path.join(CSV_DIR,'host_venue_' + xfilename_csv_suffix )     


    lst_fields_works = ['id', 'doi', 'title', 'display_name', 'publication_year', 
                        'publication_date', 'type', 'cited_by_count', 
                        'is_retracted', 'is_paratext'] # host venue wil be in a table of its own 
    lst_fields_alternate_host_venues = ['work_id', 'venue_id']
    lst_fields_authorships = ['work_id', 'author_position', 'author_id', 'institution_id']
    lst_fields_biblio = ['work_id', 'volume', 'issue', 'first_page', 'last_page']
    lst_fields_concepts =  ['work_id', 'concept_id', 'score']
    lst_fields_ids = ['work_id', 'openalex', 'doi', 'mag', 'pmid', 'pmcid']
    lst_fields_mesh =  ['work_id', 'descriptor_ui', 'descriptor_name', 'qualifier_ui', 'qualifier_name']
    lst_fields_open_access = ['work_id', 'is_oa', 'oa_status', 'oa_url']
    lst_fields_referenced_works = ['work_id', 'referenced_work_id']
    #lst_fields_related_works = ['work_id', 'related_work_id']
    lst_fields_host_venue = ['work_id', 'id',  'issn_l',  'issn',  'display_name',  'publisher',  'type',  'url',  'is_oa',  'version', 'license']
    
       


    # initializes file objects 
    with open(csv_filename_works, 'w') as handle_works, \
         open(csv_filename_alternate_host_venues, 'w')   as handle_alternate_host_venues, \
         open(csv_filename_authorships, 'w')   as handle_authorships, \
         open(csv_filename_biblio, 'w')   as handle_biblio ,\
         open(csv_filename_concepts, 'w')   as handle_concepts, \
         open(csv_filename_ids, 'w')   as handle_ids ,\
         open(csv_filename_mesh, 'w')   as handle_mesh ,\
         open(csv_filename_open_access, 'w')   as handle_open_access, \
         open(csv_filename_referenced_works , 'w')   as handle_referenced_works, \
         open(csv_filename_host_venue, 'w') as handle_host_venue:
         
         #open(csv_filename_related_works  , 'w')   as handle_related_works
         

            # initalize the csv writers 
            csv_writer_works  = init_dict_writer(handle_works,
                                                 lst_fields_works, extrasaction='ignore')
            csv_writer_biblio = init_dict_writer(handle_biblio ,
                                                 lst_fields_biblio, extrasaction='ignore')
            csv_writer_concepts = init_dict_writer(handle_concepts ,
                                                   lst_fields_concepts, extrasaction='ignore')
            csv_writer_ids = init_dict_writer(handle_ids ,
                                              lst_fields_ids, extrasaction='ignore')
            csv_writer_mesh = init_dict_writer(handle_mesh ,
                                               lst_fields_mesh, extrasaction='ignore')
            csv_writer_open_access = init_dict_writer(handle_open_access ,
                                                      lst_fields_open_access , extrasaction='ignore')
            csv_writer_referenced_works = init_dict_writer(handle_referenced_works ,
                                                           lst_fields_referenced_works, extrasaction='ignore')
            #csv_writer_related_works = init_dict_writer(handle_related_works ,
                                                        #lst_fields_related_works, extrasaction='ignore')
            csv_writer_alternate_host_venues = init_dict_writer(handle_alternate_host_venues,
                                                                lst_fields_alternate_host_venues , extrasaction='ignore')
            csv_writer_authorships = init_dict_writer(handle_authorships ,
                                                      lst_fields_authorships, extrasaction='ignore')
            
            csv_writer_host_venue = init_dict_writer(handle_host_venue ,
                                                      lst_fields_host_venue , extrasaction='ignore')
            
            


            # process the json_line 

            with gzip.open(jsonl_file_name, 'r') as works_jsonl:
                for work_json in works_jsonl:
                    if not work_json.strip():
                        continue
                    work = json.loads(work_json)
                    #if work.get('alternate_host_venues'):
                    #    break

                    #--- id set to avoid duplicates
                    seen_work_ids = set()

                    if not (work_id := work.get('id')) or work_id in seen_work_ids:
                        continue

                    seen_work_ids.add(work_id)

                    #process the jsonline to extract data for the tables 

                    #tab_works(work)   
                    
                    #works 
                    dict_work = work
                    csv_writer_works.writerow(dict_work )
                    
                    # alternate_host_venues
                    if alternate_host_venues := work.get('alternate_host_venues'):
                            for alternate_host_venue in alternate_host_venues:
                                if venue_id := alternate_host_venue.get('id'):
                                        dict_alternate_host_venues = {}
                                        dict_alternate_host_venues['venue_id'] = venue_id
                                        dict_alternate_host_venues['work_id'] = work_id
                                        csv_writer_alternate_host_venues.writerow(dict_alternate_host_venues)


                    # authorships
                    if authorships := work.get('authorships'):
                        for authorship in authorships:
                            if author_id := authorship.get('author', {}).get('id'):
                                institutions = authorship.get('institutions')
                                institution_ids = [i.get('id') for i in institutions if i]
                                institution_ids = [i for i in institution_ids if i]
                                institution_ids = institution_ids or [None]

                                for institution_id in institution_ids:
                                    dict_authorships = {}
                                    dict_authorships['work_id'] = work_id       
                                    dict_authorships['author_position'] =  authorship.get('author_position')
                                    dict_authorships['author_id'] =  author_id
                                    dict_authorships['institution_id'] =  institution_id
                                    csv_writer_authorships.writerow(dict_authorships)

                    # biblio
                    if dict_biblio := work.get('biblio'):
                            dict_biblio['work_id'] = work_id
                            csv_writer_biblio.writerow(dict_biblio)
                            

                    # ids
                    if dict_ids := work.get('ids'):
                            dict_ids['work_id'] = work_id
                            csv_writer_ids.writerow(dict_ids)

                    # mesh
                    for dict_mesh in work.get('mesh'):
                        dict_mesh['work_id'] = work_id
                        csv_writer_mesh.writerow(dict_mesh)

                    # open_access
                    if dict_open_access := work.get('open_access'):
                            dict_open_access['work_id'] = work_id
                            csv_writer_open_access.writerow(dict_open_access)


                    # concepts  
                    for concept in work.get('concepts'):
                        if concept_id := concept.get('id'):
                                dict_concept = {}
                                dict_concept['concept_id'] = concept_id
                                dict_concept['score'] = concept.get('score')             
                                dict_concept['work_id'] = work_id
                                csv_writer_concepts.writerow(dict_concept)            

                    # referenced_works
                    for referenced_work in work.get('referenced_works'):
                        if referenced_work:
                            dict_referenced_work = {}
                            dict_referenced_work['work_id'] = work_id
                            dict_referenced_work['referenced_work_id'] = referenced_work
                            csv_writer_referenced_works.writerow(dict_referenced_work)

                    # # related_works
                    # for related_work in work.get('related_works'):
                    #     if related_work:
                    #         dict_related_works = {}
                    #         dict_related_works['work_id'] = work_id
                    #         dict_related_works['related_work_id'] = related_work  
                    #        csv_writer_related_works.writerow(dict_related_works)
        
                    # host_venue
                    if dict_host_venue := work.get('host_venue'):
                            dict_host_venue['work_id'] = work_id
                            csv_writer_host_venue.writerow(dict_host_venue )                            
                            
        

    if verbose:
        print('processed:', xfilename_csv_suffix)        
        
