this project has code to make an end to end deep learning model which farmers can use to identify disease in their tomato plants.
here i have created two docker containers which you can run in any environment and on any serverless servers like AWS, GCR etc. 
one container is frontend where streamlit is running and other container is backed where fastapi and uvicorn is running .

ports used by this container

front end : streamlit ---> 8501
backend : fastapi ---> 8000