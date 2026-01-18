from fastapi import HTTPException, status
from models import deskModel
import requests


def get_desks(data,db):
    try:
        response = requests.get('')
        if response.status_code == 200:
            return response
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An error occurred, when calling api')
    
    
def get_desk_by_id(id,db):
    pass