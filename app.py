# Import Library
import os.path

import streamlit as st
from PIL import Image
import qrcode
import os
import time

# Specify the QR Code Details
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3)


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
            # Display QR Image
            qr_img = load_qr_image(img_file)
            st.image(qr_img)

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
