class ShoppingCart:
    def __init__(self):
        self.items= []

    def add_items(self,name,price,quantity):
        item ={
            "name":name,
            "price":price,
            "quantity":quantity
        }
        self.items.append(item)
        print(f"{name} is added successfully")

    def remove_items(self,name):
        for item in self.items:
            if item[name] == name:
                self.items.remove(item)
                print(f"{name} is removed")       

        print("Item Not Found") 

    def viewCart(self):

        if len(self.items)==0:
            print("Cart is Empty")

        print("\nCart Items")
        for item in self.items:
            print(
                f"{item['name']} "
                f"Price:{item['price']} "
                f"Qty:{item['quantity']}"
            )


    def Calculate_total(self):
        total = 0 
        for item in self.items:
            total += item["price"] * item["quantity"]
        return  total
    
    def checkout(self):
        total = self.Calculate_total()
        print(f"The Total Amount is {total}")


cart1 = ShoppingCart()
cart1.add_items("MOuse",500,2)
cart1.add_items("Keyboard",850,4)
cart1.add_items("speakers",1700,2)

cart1.viewCart()

cart1.checkout()