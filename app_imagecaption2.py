
import streamlit as st
import  os

import requests
# Import libraries


import gdown
# data flick30k
# url_data = "https://drive.google.com/uc?id=1KQOWoQAq9cvKKurhC00zqGfTfLFtIUw2"
url_data = "https://drive.google.com/uc?id=136_IKI3j8AqdTs2G2JgT8fg-ezTM9eZi"
output_data = "flickr30k.zip"

# predict_flicrk30k
url_json = "https://drive.google.com/uc?id=1QkKLq1Q-xAwJDiU3lN8pn5OgiCopJ4is"
root = "predict_flicrk30k.json"

url_search_sys =  "https://drive.google.com/uc?id=16gUqEan81aq2SY4Se4wBX3d6WRZ9KSjn"
search_sys ="Search_Sys.zip"


#########################################################
##### GIAO DIỆN
#########################################################
#st.title("**OBJECT DETECTION**")
st.markdown("<h1 style='text-align: center;'>IMAGE CAPTIONING</h1>", unsafe_allow_html=True)
st.markdown("""
|Mentor   | Nguyễn Minh Trang  |
|:-------:|:------------------:|
| Mentees |Hà Sơn Tùng         |
|         |Nguyễn Văn Trực     |
|         |Phạm Ngọc Phương Linh |
|         |Nguyễn Chính Nghiệp |
"""
            
            , unsafe_allow_html=True)

st.write("Bắt đầu dowload")

# liên kết gg drive
import zipfile
def download_data(url, output):      
    if (os.path.exists(output)==False):
        gdown.download(url, output, quiet=False)
#         # giai nen data
#         with zipfile.ZipFile(output,'r') as zip_ref:
#             zip_ref.extractall()

# def download_data_2(url, output):      
#     if (os.path.exists(output)==False):
#         wget.download(url)

# #tai data_flick30k.zip
download_data(url_data, output_data)
download_data(url_json, root)
download_data(url_search_sys, search_sys)

# def download(url, name):      
#     if (os.path.exists(name)==False):
#         #st.write("Đang lấy file %s..." % name)
#         w = requests.get(url).content  # lấy nội dung url
#         with open(name,'wb') as f:
#             st.write(f.write(w))   # in ra màn hình
#         f.close()

# def download_json(url, output):      
#     if (os.path.exists(output)==False):
#         gdown.download(url, output, quiet=False)
def giainen(file):
    with zipfile.ZipFile(file,'r') as zip_ref:
        zip_ref.extractall()
    
# #st.write("Đang lấy file weights...")
# download('https://archive.org/download/flickr30k_images/Search_Sys.zip', 'Search_Sys.zip')
# download('https://archive.org/download/flickr30k_images/flickr30k_images.zip', 'flickr30k_images.zip')

giainen('Search_Sys.zip')
giainen('flickr30k_images.zip')

# download_json(url_json, root)


#folder_sys
save_ix = "Search_Sys"


os.system("pwd")
st.write(os.listdir())
st.write("đã giải nén")

import search_system

option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
# img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")
if button:
    search_system.main("baby car")    
