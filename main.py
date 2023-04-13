import requests
from faker import Faker
import random
#import pytest

GLOBAL_URL = 'https://pokemonbattle.me:9104'
TOKEN = 'token'
faker = Faker()
trainerId=3691

#Trainer information
def trainerInf(trainerId):
    response = requests.get(GLOBAL_URL + '/trainers', params={
        'trainer_id': trainerId
    })
    
    print(response.json())
    return response

#generate random pokemon's avatar URL
def pokeImg():
    imgNum=random.randint(1,1008)
    if len(str(imgNum)) == 1:
        imgUrl="https://dolnikov.ru/pokemons/albums"+'/00'+str(imgNum)+'.png'
    if len(str(imgNum)) == 2:
        imgUrl="https://dolnikov.ru/pokemons/albums"+'/0'+str(imgNum)+'.png'    
    if len(str(imgNum)) >= 3:
        imgUrl="https://dolnikov.ru/pokemons/albums"+'/'+str(imgNum)+'.png'
    print('imgUrl: ',imgUrl)
    return imgUrl

#Create new pokemon
def createPokemon(token):
    pokeName=faker.name()
    imgUrl=pokeImg()
    response= requests.post(GLOBAL_URL+'/pokemons',headers={
    'trainer_token': token,
    'Content-Type': 'application/json'
    }, json={
    "name": pokeName,
    "photo": imgUrl
    })
    print(response.text)
    return response

#Modify existing pokemon
def modifyPokemon(pokemonId,token):
    pokeName=faker.name()
    imgUrl=pokeImg()
    response= requests.put(GLOBAL_URL+'/pokemons',headers={
    'trainer_token': token,
    'Content-Type': 'application/json'
    }, json={
    "pokemon_id": pokemonId,    
    "name": pokeName,
    "photo": imgUrl
    })
    print(response.text)
    return response

#Catch pokemon in pokeball
def catchPokemon(pokemonId,token):
    response=requests.post(GLOBAL_URL+'/trainers/add_pokeball',headers={
        'trainer_token': token,
        'Content-Type': 'application/json'
        }, json={
        "pokemon_id": pokemonId
        })
    print(response.text)
    return response

#trainerInf(3691)
#createPokemon('6bbdc0063d9ea0fc4aa062db5154c4a7')
#modifyPokemon(8969)  
#catchPokemon(8969)
