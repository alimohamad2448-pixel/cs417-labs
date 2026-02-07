def parse_product_basic(response):
    
   

   return {
        "id": response["id"],
        "name": response["name"],}


def parse_availability(response):
    
    if "in_stock" in response:
        return response["in_stock"]

    else:
        return False