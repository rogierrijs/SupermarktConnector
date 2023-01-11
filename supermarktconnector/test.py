import supermarktconnector;

from supermarktconnector.jumbo import JumboConnector
connector = JumboConnector('17')
result  = connector.search_products(query='Smint', size=1, page=0)
print(result)