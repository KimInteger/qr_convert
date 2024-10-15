import qrcode


def convert_qr(url,name) :
# QR 코드로 변환할 URL
    convert_url = url

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,  # QR 코드 크기 조절
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 용량
        box_size=10,  # QR 코드 상자 크기
        border=4,  # 테두리 크기
    )

    # URL 추가
    qr.add_data(convert_url)
    qr.make(fit=True)

    # QR 코드 이미지 생성
    img = qr.make_image(fill='black', back_color='white')

    # 이미지 저장
    img.save(f'./qr_convert/{name}.png')

    # QR 코드 보여주기 (선택 사항, 이미지 바로 보여줌)
    img.show()


if __name__ == "__main__":
    file_url = input("file_url :");
    file_name = input("save_name :")
    convert_qr(file_url,file_name)