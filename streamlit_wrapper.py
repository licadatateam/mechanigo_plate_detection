# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:35:46 2024

@author: carlo
"""

import streamlit as st
import plate_recognizer as pr


image_file = st.file_uploader(label = 'Upload photo of plate number to read.',
                 type = ['png', 'jpg'],
                 accept_multiple_files = False)

if image_file is not None:
    data = image_file.read()
    
    st.image(data, use_column_width = True)
    
    results = pr.get_plate_number(data)

    plate_col, score_col = st.columns(2)
    
    with plate_col:
        
        pn = st.metric('Plate Number',
                       value = results['plate'].upper())
    
    with score_col:
        
        score = st.metric('Confidence score',
                          value = f"{results['score']*100}%")

with st.expander('Usage', expanded = False):
    stats = pr.get_statistics()
    
    usage = st.metric('API Calls',
              value = f"{stats['usage']['calls']}/{stats['total_calls']}")

    st.write(f"Reset date: {stats['usage']['resets_on']}")
