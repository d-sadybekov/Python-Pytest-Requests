import requests
import pytest

TOKEN='6bbdc0063d9ea0fc4aa062db5154c4a7'
TRAINER_ID=3691
GLOBAL_URL = 'https://pokemonbattle.me:9104'

def test_get_trainer():
    response=requests.get(GLOBAL_URL+'/trainers',params={
    "trainer_id":TRAINER_ID
    })
    assert response.status_code==200

def test_get_trainer_name():
    response=requests.get(GLOBAL_URL+'/trainers',params={"trainer_id":TRAINER_ID})
    assert response.json()['trainer_name'] == 'Illinoise.D.S'