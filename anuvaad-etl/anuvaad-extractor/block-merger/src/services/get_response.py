import json
from src.services import get_xml
import pandas as pd
from anuvaad_auditor.loghandler import log_info
import base64
from anuvaad_auditor.loghandler import log_error
import src.utilities.app_context as app_context
import time

def df_to_json(p_df):
    #start_time = time.time()
    page_data = []
    try:
        p_df      = p_df.where(p_df.notnull(), None)
        if len(p_df) > 0 :
            p_df = get_xml.drop_cols(p_df)
            for index ,row in p_df.iterrows():
                block = row.to_dict()
                for key in block.keys():
                    if key in ['text']:
                        block[key] = block[key]
                    if key not in ['text', 'children']:
                        try :
                            block[key] = int(block[key])
                        except :
                            pass
                    
                if block['attrib'] == "TABLE":
                    pass
                else :
                    if 'children' in list(block.keys()):
                        if block['children'] == None :
                            pass
                        else :
                            block['children'] = df_to_json(pd.read_json(row['children']))
                page_data.append(block)
        else:
            page_data = None

        #end_time = time.time()
        #extraction_time = end_time - start_time
        #log_info('Generating response of p_df completed in {}'.format(extraction_time), app_context.application_context)
            
    except Exception as e :
        log_error('Error in generating response of p_df', app_context.application_context, e)
        return None

    return page_data

def process_image_df(img_df):
    start_time = time.time()
    image_data = []
    try:
        if len(img_df)>0:
            img_df   = get_xml.drop_cols(img_df)
                    
            for index ,row in img_df.iterrows():
                block           = row.to_dict()
                block['base64'] = block['base64'].decode('ascii')
                image_data.append(block)
            
        else:
            image_data =None
            
    except Exception as e :
        log_error('Error in generating response of img_df', app_context.application_context, e)
        return None

    end_time            = time.time()
    extraction_time     = end_time - start_time
    log_info('Generating response of img_df completed in {}'.format(extraction_time), app_context.application_context)
    return image_data

def process_table_df(table_df):
    start_time = time.time()
    table_data = []
    try:
        if len(table_df)>0:
            table_df = get_xml.drop_cols(table_df)

            for index ,row in table_df.iterrows():
                block             = row.to_dict()
                block['children'] = row['children']
                for child in row['children']:
                    for sub_child in child['text']:
                        if 'xml_index' in sub_child.keys():
                            sub_child.pop('xml_index')

                table_data.append(block)
            
        else:
            table_data = None
    except Exception as e :
        log_error('Error in generating response of table_df', app_context.application_context, e)
        return None
    end_time            = time.time()
    extraction_time     = end_time - start_time
    log_info('Generating response of table_df completed in {}'.format(extraction_time), app_context.application_context)
    return table_data       

def process_line_df(line_df):
    start_time = time.time()
    line_data  = []
    try:
        if len(line_df)>0:
            line_df   = get_xml.drop_cols(line_df)
                    
            for index ,row in line_df.iterrows():
                block           = row.to_dict()
                line_data.append(block)
            
        else:
            line_data = None
    except Exception as e :
        log_error('Error in generating response of line_df', app_context.application_context, e)
        return None
    end_time            = time.time()
    extraction_time     = end_time - start_time
    log_info('Generating response of line_df completed in {}'.format(extraction_time), app_context.application_context)
    return line_data        


def process_bg_image(bg_img):
    bg_image_data = []
    try:
        with open(bg_img, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read())
            img_base64 = img_base64.decode('ascii')
            bg_image_data.append(img_base64)
            return bg_image_data
    except Exception as e :
            log_error("Service get_response", "Error in processing bg_image", None, e)