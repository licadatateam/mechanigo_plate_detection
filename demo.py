# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:23:35 2024

@author: carlo
"""

import plate_recognizer as pr


if __name__ == "__main__":
    image_name = "plate_number_6.jpg"
    image_file_path = r".\images\{0}".format(image_name)
    
    # for execution via python function
    plate_number = pr.get_plate_number(image_file_path)