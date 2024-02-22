# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:20:37 2024

@author: carlo
"""

import requests
import json


def get_settings():
    '''
    Imports api call settings
    '''
    try:
        with open('settings.txt') as s:
            settings = json.load(s)
        
        return settings
    
    except Exception as e:
        raise e

def get_plate_number(file : str) -> dict:
    '''
    Send post request to plate_recognizer API to extract plate number info from
    Snapshot SDK API
    
    Args:
    -----
        - file : str
            image file path
        - regions : list
            list of country codes for plate number usage
    
    Returns:
    --------
        - best_candidate : dict
            dictionary containing best plate number result and corresponding score
            Keys:
            -----
                - plate : extracted plate number
                - score : confidence score of extracted plate number
    
    '''
    settings = get_settings()
    
    # open file
    try:
        with open(file, 'rb') as fp:
            #success, image_jpg = cv2.imencode('.jpg', fp)
            image = fp.read()
    
    except Exception as e:
        image = file
    
    # send post request via snapshot sdk api
    try:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=settings["regions"]),  #Optional
            files=dict(upload=image),
            headers={'Authorization': f'Token {settings["api_key"]}'})
    
    except:
        response = None
    
    # obtain best candidate result, if applicable
    if response is not None:
        results = response.json()['results'][0]
        best_candidate = sorted(results['candidates'], 
                                key = lambda s: s['score'],
                                reverse = True)
        
        return best_candidate[0]
    
    else:
        return {'plate' : '',
                'score' : 0}
    

def get_statistics():
    '''
    Returns information on api usage
    
    - total_calls : int
        max number of calls available for plan
    - usage : dict
        Keys:
            - year : int
            - month : int
            - resets_on : str
            - calls : number of api calls made
            
    
    '''
    # imports settings
    settings = get_settings()
    
    # send get request
    try:
        r = requests.get('https://api.platerecognizer.com/v1/statistics/', 
                     headers = {'Authorization' : f"Token {settings['api_key']}"})
        
        return r.json()
    
    except:
        return None
        
    
                     

