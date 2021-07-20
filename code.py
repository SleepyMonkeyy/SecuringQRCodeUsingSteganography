import qrcode
import numpy as np


data = "https://drive.google.com/drive/folders/1nwDngaAMZ_55Vl8HSehF7MQ8Ap5bGHAP?usp=sharing"
qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4)
	
  
qr.add_data(data)
qr.make()

print("The shape of the QR image:", np.array(qr.get_matrix()).shape)

img = qr.make_image(fill_color="black", back_color="white")
    
img.save("SecureQr.png")