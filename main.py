from evmosgrpc.messages.msgsend import create_msg_send
from evmosgrpc.builder import TransactionBuilder
from evmosgrpc.transaction import Transaction

seed = 'garment seat help gallery ride divide truth smooth end chunk '\
       'ten cross badge want vehicle mirror dismiss remind crouch '\
       'base crouch palm leader dinner'
builder = TransactionBuilder(seed)
msg = create_msg_send(
    builder.address,
    "evmos1sgg7ny6mkk375ghdlx837hkm92dqxs450fxwwz",
    100,
)
res = builder.send_tx(Transaction().generate_tx(builder, msg))
# res =
# tx_response {
#   txhash: "F4DFCF8E0BAEBBE088DF0C8A4DA1EF70CD29983C5F7663A523A87F1CE479BFF5"
#   raw_log: "[]"
# }
print(res)

# To read the response as a dict:
from google.protobuf.json_format import MessageToDict
res_obj = MessageToDict(res)