# Import Library
import streamlit as st
from PIL import Image
import qrcode
import os
import numpy as np
import cv2
import time

# Specify the QR Code Details
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3)

# Create Folder in Current Location


# Function To Load QR Image
def load_qr_image(img):
    qr_img = Image.open(img)
    return qr_img


# Function main
def main():
    menu = ["Home", "DecoderQR", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        # Text input to convert into QR
        with st.form(key="myqr_form"):
            raw_text = st.text_area("Enter Text")
            submit_button = st.form_submit_button("Generate QR")

        # Format Layout
        if submit_button:
            c1, c2 = st.columns(2)
            with c1:
                # Add Data
                qr.add_data(raw_text)

                # Generate QR
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # Image Filename
                date_time = time.strftime("%Y%m%d-%H%M%S")
                img_filename = "QR_Image_{}.png".format(date_time)
                img_path = os.path.join("image_folder", img_filename)
                img.save(img_path)

                # Load QR Image
                img_load = load_qr_image(img_path)
                st.image(img_load)
            with c2:
                st.info("Your Text")
                st.write(raw_text)

    elif choice == "DecoderQR":
        st.subheader("DecoderQR")

        # File Uploader
        img_file = st.file_uploader("Upload QR Image", type=["jpg", "png", "jpeg"])

        if img_file is not None:
            # Display QR Image by Streamlit
            # qr_img = load_qr_image(img_file)
            # st.image(qr_img)

            # Display QR Image by Opencv
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            img_opencv = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            c1, c2 = st.columns(2)
            with c1:
                st.image(img_opencv)
            with c2:
                st.info("Decoded QR Code")
                det = cv2.QRCodeDetector()
                retval, points, straight_qrcode = det.detectAndDecode(img_opencv)

                # Write Decoded QR Code
                st.write(retval)

                # Display QR Code Raw Data
                st.info("QR Code Raw Data")
                st.write(straight_qrcode)
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
