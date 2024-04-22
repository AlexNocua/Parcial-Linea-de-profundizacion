import pymongo
from pymongo import MongoClient
import certifi


def Conexion():
    # coneccion = '190.171.76.72/32'

    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["Suministros_de_computo"]

        # client = pymongo.MongoClient(MONGO, tlsCAFile=certificado)
        # db = client["App_Flask"]
        print('Conecto')
    except ConnectionError:
        print('Error de coneccion')

    # collection = db["conexionFlask"]

    return db


Conexion()
