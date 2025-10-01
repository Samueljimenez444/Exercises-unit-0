
sales_information = {}

user_selecction = int(input("Introduce your selecction"))

while(user_selecction != 0):
    
    if user_selecction == 1:

        product_name = input("Introduce the product name")

        quantity = int(input("Introduce the quantity sold"))

        if(sales_information.get(product_name, "Error") != "Error"):

            sales_information[product_name] += quantity
        else:
            sales_information[product_name] = quantity    

        

    elif user_selecction == 2:    

        product_name = input("Introduce the product name")

        print(sales_information.get(product_name, "Product has not been sold yet"))
    
    user_selecction = int(input("Introduce your selecction"))

