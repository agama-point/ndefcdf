import ndefcdf

pay = ndefcdf.lnpay.CDFLNPay("https://example.org/payurl")
pay_label = ndefcdf.lnpay.CDFLNPay("Label 1:https://example.org/payurl")
print(pay)
print(pay_label)

wit = ndefcdf.lnwithdrawal.CDFLNWithdrawal("https://example.org/withdrawal")
wit_label = ndefcdf.lnwithdrawal.CDFLNWithdrawal("Label 1:https://example.org/withdrawal")
print(wit)
print(wit_label)

encoded = wit._encode()

print(encoded)
print(ndefcdf.lnwithdrawal.CDFLNWithdrawal._decode_payload(encoded, True))
