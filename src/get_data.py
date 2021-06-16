##read parameters
##process the data
##return the dataframe

import os
import yaml
import pandas as pd
import argparse

#defining a function to read the parameters from the parameters.yaml file
def read_params(config_path):
    with open(config_path) as yaml_file: #opening the yaml file, as the default is parameters.yaml
        config =  yaml.safe_load(yaml_file) #loading the file in the variable config
    return config


#defining a method to read the data
def get_data(config_path):
    config = read_params(config_path) #getting the config using the above method read_params
    print(config)
    #data_path = config['data_source']['s3_source'] #getting the data path for the give data file
    #df = pd.read_csv(data_path)  #loading the data frame from the given data 
    #return df


if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="parameters.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
