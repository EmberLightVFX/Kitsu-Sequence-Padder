from pydoc import doc
import gazu
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PROJECT = os.getenv('PROJECT')
PADDING = int(os.getenv('PADDING'))

gazu.set_host(HOST + "/api")
gazu.log_in(USER, PASSWORD)

project_dict = gazu.project.get_project_by_name(PROJECT)

sequences_dict = gazu.shot.all_sequences_for_project(project_dict)

for sequence in sequences_dict:
    if len(sequence['name']) < PADDING:
        old_name = sequence['name']
        while len(sequence['name']) < PADDING:
            sequence['name'] = '0' + sequence['name']
        sucess = gazu.shot.update_sequence(sequence)
        if sucess:
            print(old_name + ' was renamed to ' + sequence['name'])
        else:
            print('Something went wrong when renaming ' +
                  old_name + " to " + sequence['name'])
