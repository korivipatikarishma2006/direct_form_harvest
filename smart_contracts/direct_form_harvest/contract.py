from algopy import UInt64, gtxn
from algopy import ARC4Contract, arc4, Global, itxn, BoxMap
class TaskData(arc4.Struct, frozen= True):
     client: arc4.Address
     farmer: arc4.Address
     amount: arc4.UInt64
class TasksupplyContract(ARC4Contract):
 
    def __init__(self) -> None:
         self.box_map_struct = BoxMap(arc4.UInt64, TaskData, key_prefix="users")
@arc4.abimethod
    def create_supply96(self, payment_txn: gtxn.PaymentTransaction ,task_id: arc4.UInt64, cilent: arc4.Address, farmer: arc4.Address, reward: arc4.UInt64) -> None:
         # Check payment is in group txn 0
         # payment_txn = gtxn.PaymentTransaction(0)
         assert payment_txn.receiver == Global.current_application_address
         assert payment_txn.amount == amount.native
         assert payment_txn.sender == cilent.native
          task_data = TaskData(
             cilent=cilent,
             farmer=farmer,
             amount=amount,  
         )
        self.box_map_struct[task_id] = task_data

        def release_amount(self, task_id: arc4.UInt64, caller: arc4.Address) -> UInt64:
         task_data = self.box_map_struct[task_id]
         assert caller == task_data.cilent,
         result = itxn.Payment(
             sender=Global.current_application_address,
             amount=task_data.farmer.native,
              amount=task_data.reward.native,
             fee=10000
         ).submit()

        del self.box_map_struct[task_id]
        return result.amount

