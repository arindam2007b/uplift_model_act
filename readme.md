activate conda
'''bash
source ~/anaconda3/bin/activate
'''

create environment
'''bash
conda create -n uplift_model python=3.7 -y
'''

activate environment
'''bash
conda activate uplift_model
'''

create a requirement file
'''bash
touch requirements.txt
'''

install the required packages from requirement file
'''bash
conda install --file requirement.txt
'''

create a template.py file
'''bash 
touch template.py
'''

creating another directory for given data 
'''bash
mkdir data_given
'''

put the data in the data_given directory

'''bash
git init
dvc init
dvc add data_given/Uplift_model_data_mar_18.csv
git add . #put everything in git
git commit -m "first commit"
git add . && git commit -m "update readme.md"
'''

