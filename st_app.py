import streamlit as st
import requests
import json
import io

def post_run(image_bytes):
    url = "http://backend_fastapi:8000/predict"

    payload = {}
    files=[
    ('file',('image.JPG',image_bytes,'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return (response.text)

def run():
    st.write("# TOMATO DISEASE CLASSIFIER :tomato:")

    st.write("### this web app can classify 9 commonly happening disease in tomato plant using uploaded image of the plant leaf :seedling:")

    st.write('upload the file to analyze the health of your tomato plant :point_down:')

   


    # create a file uploader widget
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # check if an image file was uploaded
    if uploaded_file is not None:
        # display the uploaded image
        st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
        #uploaded_file = UploadedFile(uploaded_file.name, uploaded_file.type, uploaded_file.size, uploaded_file.data)
    

    if(st.button('Predict health')):
        #with open(uploaded_file, 'rb') as f:
        #    image_data = f.read()
         # Create a dictionary of form data with the image data as a value
        image_bytes = uploaded_file.read()
        #upload_file = UploadFile( image_bytes)
        #form_data = {'file': upload_file}
        #response = requests.post('http://localhost:8000/predict',data=form_data)
        prediction = post_run(image_bytes)
        dict1 = json.loads(prediction)
        disease = dict1['class']
        confidence = dict1['confidence']
        st.success(f'TOMATO HEALTH ------->  {disease}')
        st.write(f'CONFIDENCE ------->  {confidence}')

   

if __name__ == '__main__':
    run()