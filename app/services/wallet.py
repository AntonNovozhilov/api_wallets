from app.core.config import settings
from app.repositories.wallet import WalletRepositories

class WalletOperation(WalletRepositories):

        async def _operations(self, obj, method: str, ammount: int):
            if method == settings.DEPOSIT:
                obj.balance += ammount
                return obj.balance
            if method == settings.WITHDRAW:
                obj.balance -= ammount
                return obj.balance
            
wallet_operation = WalletOperation()

    # async def _deposit(self, method, ammount: int):
    #     if method == settings.DEPOSIT:
    #         self.obj.balance += ammount
    #         return self.obj.balance
        
    # async def _withdraw(self, method, ammount: int):
    #     if method == settings.WITHDRAW:
    #         self.obj.balance -= ammount
    #         return self.obj.balance

