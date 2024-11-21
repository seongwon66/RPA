import qrcode

student_id = input("학번을 입력하세요: ")
name = input("이름을 입력하세요: ")
major = input("전공을 입력하세요: ")

info = f"학번: {student_id}\n이름: {name}\n전공: {major}"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
qr.add_data(info)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

filename = "my_info_data.png"
img.save(filename)

print(f"QR 코드가 생성되었습니다: {filename}")