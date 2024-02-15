import urllib.request
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import requests
from api_token_falabella import *

url = "https://sellercenter-api.falabella.com/falabella-cl"
api_key = 'a656dfae57a10cdd2714edde988e5a16479dda0c'

parameters = {
    'UserID': 'cecilia.ullua@vasser.com.ar',
    'Format': 'JSON',
    'Version': '1.0',
    'Action': '',
    'Timestamp': datetime.now().isoformat(),
}
headers = {"accept": "application/json"}

# ENDPOINTS DE PRODUCTO
#------------------------------------------------
def get_productos():
    parameters['Action'] = 'GetProducts'

    parameters['Signature'] = generate_signature(api_key, parameters)


    response = requests.get(url, params=parameters, headers=headers)

    print(response.text)

def get_marca():
    parameters['Action'] = 'GetBrands'

    parameters['Signature'] = generate_signature(api_key, parameters)


    response = requests.get(url, params=parameters, headers=headers)

    print(response.text)

def get_categorias():
    parameters['Action'] = 'GetCategoryTree'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_categorias_atributos():
    parameters['Action'] = 'GetCategoryAttributes'
    parameters['PrimaryCategory'] = '112'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_categorias_atributos_set():
    parameters['Action'] = 'GetCategoriesByAttributeSet'
    parameters['AttributeSet'] = '112'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_atributos_marca():
    parameters['Action'] = 'GetCategoriesByAttributeSet'
    parameters['AttributeSet'] = '112'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def post_producto():
    parameters['Action'] = 'ProductCreate'
    parameters['Signature'] = generate_signature(api_key, parameters)

    payload = """<?xml version="1.0" encoding="UTF-8" ?>
        <Request>
            <Product>
                <Brand>adidas</Brand>
                <Description>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat</Description>
                <Name>PRODUCT TEST - TEST - TEST</Name>
                <PrimaryCategory>112</PrimaryCategory>
                <SellerSku>SKU-TEST-12345</SellerSku>
                <Variation>...</Variation>
                <BusinessUnits>
                    <BusinessUnit>
                        <OperatorCode>facl</OperatorCode>
                        <Price>59990</Price>
                        <SpecialPrice>35990</SpecialPrice>
                        <SpecialFromDate>2023-05-26 00:00:00</SpecialFromDate>
                        <SpecialToDate>2023-10-31 23:59:59</SpecialToDate>
                        <Stock>36</Stock>
                        <Status>active</Status>
                    </BusinessUnit>
                </BusinessUnits>
                <ProductData>
                    <ConditionType>Nuevo</ConditionType>
                    <PackageHeight>10</PackageHeight>
                    <PackageLength>10</PackageLength>
                    <PackageWeight>2</PackageWeight>
                    <PackageWidth>10</PackageWidth>
                    <TaxPercentage></TaxPercentage>
                </ProductData>
            </Product>
        </Request>"""

    response = requests.post(url, params=parameters,headers=headers, data=payload)

    print(response.text)

# Por probar !!!!!!!!
def post_eliminar_productos():
    parameters['Action'] = 'ProductRemove'
    parameters['Signature'] = generate_signature(api_key, parameters)

    payload = """<?xml version="1.0" encoding="UTF-8" ?>
        <Request>
            <Product>
                <SellerSku>297afb9c989c6ad</SellerSku>
            </Product>
        <Product>
            <SellerSku>1b71ff01983241f</SellerSku>
            </Product>
        </Request>"""

    response = requests.post(url, params=parameters,headers=headers,data=payload)

    print(response.text)

# Por probar x2 !!!!!!!!
def post_actualizar_productos():
    parameters['Action'] = 'ProductUpdate'
    parameters['Signature'] = generate_signature(api_key, parameters)

    payload = """<?xml version="1.0" encoding="UTF-8" ?>
        <Request>
            <Product>
                <SellerSku>SKU-TEST-12345</SellerSku>
                <ShortDescription>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</ShortDescription>
                <BusinessUnits>
                    <BusinessUnit>
                        <OperatorCode>facl</OperatorCode>
                        <Stock>50</Stock>
                        <Status>active</Status>
                    </BusinessUnit>
                </BusinessUnits>
            </Product>
            <Product>
                <SellerSku>SKU-TEST-999999</SellerSku>
                <Name>PRODUCT TEST - TEST - TEST</Name>
                <ParentSku/>
                <Description>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</Description>
                <Color>Verde</Color>
                <ColorBasico>Rojo</ColorBasico>
                <BusinessUnits>
                    <BusinessUnit>
                        <OperatorCode>facl</OperatorCode>
                        <Price>59990</Price>
                        <SpecialPrice>35990</SpecialPrice>
                        <SpecialFromDate>2023-05-26 00:00:00</SpecialFromDate>
                        <SpecialToDate>2023-10-31 23:59:59</SpecialToDate>
                        <Stock>40</Stock>
                        <Status>inactive</Status>
                    </BusinessUnit>
                </BusinessUnits>
                <ProductData>
                    <ConditionType>Nuevo</ConditionType>
                    <PackageHeight>11</PackageHeight>
                    <PackageWidth>11</PackageWidth>
                    <PackageLength>11</PackageLength>
                    <PackageWeight>4</PackageWeight>
                </ProductData>
            </Product>"""

    response = requests.post(url, params=parameters,headers=headers,data=payload)

    print(response.text)
#------------------------------------------------


# FEED ENDPOINTS
#------------------------------------------------
def get_feeds():
    parameters['Action'] = 'FeedList'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_feeds_fitro():
    parameters['Action'] = 'FeedOffsetList'
    # Opcionales
    #parameters['Offset'] = ''
    #parameters['PageSize'] = ''
    parameters['Status'] = 'Finished'
    #parameters['CreationDate'] = '2024-02-13 15:46:08'
    #parameters['UpdatedDate'] = '2024-02-14 15:46:09'
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_feeds_detalles():
    parameters['Action'] = 'FeedStatus'
    parameters['FeedID'] = '765c72ed-6abf-44ce-b428-8e5a9bbb3328'
    parameters['Signature'] = generate_signature(api_key, parameters)
    
    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)
#------------------------------------------------


# ENDPOINTS DE ÓRDENES
#------------------------------------------------
def get_orden():
    parameters['Action'] = 'GetOrder'
    parameters['OrderId'] = '4075856'
    parameters['Signature'] = generate_signature(api_key, parameters)
    
    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)
    '''
    response_productos = response.json()
    DataOrder = response_productos['SuccessResponse']['Body']['Orders']['Order']
    OrderID = DataOrder['OrderId']
    OrderNumber = DataOrder['OrderNumber']
    NombreCliente = DataOrder['AddressShipping']['FirstName']+ ' ' + DataOrder['AddressShipping']['LastName']
    FechaCreacion = DataOrder['CreatedAt']
    Precio = DataOrder['Price']
    MetodoPago = DataOrder['PaymentMethod']

    #print('Datos Orden: ' ,DataOrder)
    print('Order ID: ' ,OrderID)
    print('Numero de Orden: ' ,OrderNumber)
    print('Nombre Cliente: ' ,NombreCliente)
    print('Fecha Creacion: ' ,FechaCreacion)
    print('Pecio: ' ,Precio)
    print('Metodo de Pago: ' ,MetodoPago)
    '''

# Por probar !!!!!!!!
def get_ordenes():
    parameters['Action'] = 'GetOrders'
    #parameters['CreatedAfter']
    #parameters['CreatedBefore']
    #parameters['UpdatedAfter']
    #parameters['UpdatedBefore']
    #parameters['Limit']
    #parameters['Offset']
    parameters['Status'] = 'Finished'
    #parameters['SortBy']
    #parameters['SortDirection']
    #parameters['ShippingType']
    parameters['Signature'] = generate_signature(api_key, parameters)
    
    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

def get_items():
    parameters['Action'] = 'GetOrderItems'
    parameters['OrderId'] = '4075856'
    parameters['Signature'] = generate_signature(api_key, parameters)
    
    response = requests.get(url, params=parameters,headers=headers)

    print(response.text)

# Por probar !!!!!!!!
def post_cancelar_orden():
    parameters['Action'] = 'SetStatusToCanceled'
    #parameters['OrderItemId']
    #parameters['Reason']
    #parameters['ReasonDetail']
    parameters['Signature'] = generate_signature(api_key, parameters)

    response = requests.post(url, params=parameters,headers=headers)

    print(response.text)
#------------------------------------------------


#------------------------------------------------
#get_productos()
#get_marca()
#get_categorias()
#get_categorias_atributos()
#get_categorias_atributos_set()
#get_categorias_atributos_set()
#post_producto()
#post_eliminar_productos()
#post_actualizar_productos()
#------------------------------------------------
#get_feeds()
#get_feeds_fitro()
#get_feeds_detalles()
#------------------------------------------------
#get_orden()
#get_ordenes()
#get_items()
#post_cancelar_orden()
    