import  pyqrcode


url=input("Url Giriniz : ")
qr_code=pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=5)
