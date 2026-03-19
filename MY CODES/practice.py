class shops:
    def __init__(self,gowns,shoes,flowers,necklaces):
        self.gowns = gowns
        self.shoes = shoes
        self.flowers = flowers
        self.necklaces = necklaces
	 
    def print_details(self):
        print(f"gowns:{self.gowns}")
        print(f"shoes:{self.shoes}")
        print(f"flowers:{self.flowers}")
        print(f"necklaces:{self.necklaces}")
        
Blessed_shop = shops("white gowns","leather shoes","roses","golden")
Blessed_shop.print_details()
 
class retail_shops(shops):
    def __init__(self,gowns,shoes,flowers,necklaces,crowns,ties):
        self.crowns=crowns
        self.ties=ties
        super().__init__(gowns,shoes,flowers,necklaces)
    
    def print_details(self):
        print(f"crowns:{self.crowns}")
        print(f"ties:{self.ties}")
        return super().print_details()
group20=retail_shops("gowns","shoes","flowers","necklaces","crowns","ties")
group20.print_details()
