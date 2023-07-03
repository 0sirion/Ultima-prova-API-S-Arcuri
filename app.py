import streamlit as st
import requests
import json


def main():
    st.title("API Frontend made with Streamlit")
    url_API =st.text_input("Please insert API url ","http://localhost:8000/predict")
    rdspend = st.number_input("Please insert rdspend value:")
    administration = st.number_input("Please insert administration value:")
    marketing = st.number_input("Please insert marketing value:")



    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rdspend={rdspend}&administration={administration}&marketing={marketing}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result}")




    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rdspend":rdspend,
                                                   "administration":administration,
                                                   "marketing":marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result}")



if __name__ == "__main__":
    main()