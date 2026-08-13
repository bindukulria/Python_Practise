def getcouponcode():

    print("1st coupon code")
    yield "ABC123"
    print("2nd coupon code")
    yield "XYZ456"
    print("3rd coupon code")
    yield "LMN789"
    print("4th coupon code")
    yield "PQR321"
    
for coupon in getcouponcode():
   print(coupon)
