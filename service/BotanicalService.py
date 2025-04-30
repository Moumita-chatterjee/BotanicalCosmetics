from repository.BotanicalRepo import BotanicalRepo


class BotanicalService:
    def __init__(self):
        pass
    def create_product(self,botanical):
        botanicalRepo = BotanicalRepo()
        for items in botanicalRepo.get_list():
            if botanical.product_id == items.product_id:
                    raise ValueError(f"Item '{botanical.product_id}' already exists. Unable to create")
        botanicalRepo.create_product(botanical)
        return "Product added sucessfully"

    def delete_product(self,botanical):
        botanicalRepo = BotanicalRepo()
        for items in botanicalRepo.get_list():
            if botanical.product_id == items.product_id:
                botanicalRepo.delete_product(botanical.product_id)
                return f"Product with ID {botanical.product_id} deleted successfully"


