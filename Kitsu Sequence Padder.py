import gazu
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PROJECT = os.getenv('PROJECT')
PADDING = int(os.getenv('PADDING'))


def run():

    gazu.set_host(HOST + "/api")
    if not gazu.client.host_is_up():
        print("Can't find host " + HOST)
        return

    try:
        gazu.log_in(USER, PASSWORD)
    except Exception as exc:
        print("Can't login. Please check your credentials in the .env file")
        return

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

    print("Done!")


run()
