import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
#
image_path = r".\Image\image.JPG"
image = Image.open(image_path)

st.set_page_config(page_title="Any To Any Language Translation App", layout="centered")
st.image(image, caption='Any To Any Language Translation')
#
# Create a dropdown menu with options
options = ['Acehnese (Arabic script)',
 'Acehnese (Latin script)',
 'Mesopotamian Arabic',
 'Ta’izzi-Adeni Arabic',
 'Tunisian Arabic',
 'Afrikaans',
 'South Levantine Arabic',
 'Akan',
 'Amharic',
 'North Levantine Arabic',
 'Modern Standard Arabic',
 'Modern Standard Arabic (Romanized)',
 'Najdi Arabic',
 'Moroccan Arabic',
 'Egyptian Arabic',
 'Assamese',
 'Asturian',
 'Awadhi',
 'Central Aymara',
 'South Azerbaijani',
 'North Azerbaijani',
 'Bashkir',
 'Bambara',
 'Balinese',
 'Belarusian',
 'Bemba',
 'Bengali',
 'Bhojpuri',
 'Banjar (Arabic script)',
 'Banjar (Latin script)',
 'Standard Tibetan',
 'Bosnian',
 'Buginese',
 'Bulgarian',
 'Catalan',
 'Cebuano',
 'Czech',
 'Chokwe',
 'Central Kurdish',
 'Crimean Tatar',
 'Welsh',
 'Danish',
 'German',
 'Southwestern Dinka',
 'Dyula',
 'Dzongkha',
 'Greek',
 'English',
 'Esperanto',
 'Estonian',
 'Basque',
 'Ewe',
 'Faroese',
 'Fijian',
 'Finnish',
 'Fon',
 'French',
 'Friulian',
 'Nigerian Fulfulde',
 'Scottish Gaelic',
 'Irish',
 'Galician',
 'Guarani',
 'Gujarati',
 'Haitian Creole',
 'Hausa',
 'Hebrew',
 'Hindi',
 'Chhattisgarhi',
 'Croatian',
 'Hungarian',
 'Armenian',
 'Igbo',
 'Ilocano',
 'Indonesian',
 'Icelandic',
 'Italian',
 'Javanese',
 'Japanese',
 'Kabyle',
 'Jingpho',
 'Kamba',
 'Kannada',
 'Kashmiri (Arabic script)',
 'Kashmiri (Devanagari script)',
 'Georgian',
 'Central Kanuri (Arabic script)',
 'Central Kanuri (Latin script)',
 'Kazakh',
 'Kabiyè',
 'Kabuverdianu',
 'Khmer',
 'Kikuyu',
 'Kinyarwanda',
 'Kyrgyz',
 'Kimbundu',
 'Northern Kurdish',
 'Kikongo',
 'Korean',
 'Lao',
 'Ligurian',
 'Limburgish',
 'Lingala',
 'Lithuanian',
 'Lombard',
 'Latgalian',
 'Luxembourgish',
 'Luba-Kasai',
 'Ganda',
 'Luo',
 'Mizo',
 'Standard Latvian',
 'Magahi',
 'Maithili',
 'Malayalam',
 'Marathi',
 'Minangkabau (Arabic script)',
 'Minangkabau (Latin script)',
 'Macedonian',
 'Plateau Malagasy',
 'Maltese',
 'Meitei (Bengali script)',
 'Halh Mongolian',
 'Mossi',
 'Maori',
 'Burmese',
 'Dutch',
 'Norwegian Nynorsk',
 'Norwegian Bokmål',
 'Nepali',
 'Northern Sotho',
 'Nuer',
 'Nyanja',
 'Occitan',
 'West Central Oromo',
 'Odia',
 'Pangasinan',
 'Eastern Panjabi',
 'Papiamento',
 'Western Persian',
 'Polish',
 'Portuguese',
 'Dari',
 'Southern Pashto',
 'Ayacucho Quechua',
 'Romanian',
 'Rundi',
 'Russian',
 'Sango',
 'Sanskrit',
 'Santali',
 'Sicilian',
 'Shan',
 'Sinhala',
 'Slovak',
 'Slovenian',
 'Samoan',
 'Shona',
 'Sindhi',
 'Somali',
 'Southern Sotho',
 'Spanish',
 'Tosk Albanian',
 'Sardinian',
 'Serbian',
 'Swati',
 'Sundanese',
 'Swedish',
 'Swahili',
 'Silesian',
 'Tamil',
 'Tatar',
 'Telugu',
 'Tajik',
 'Tagalog',
 'Thai',
 'Tigrinya',
 'Tamasheq (Latin script)',
 'Tamasheq (Tifinagh script)',
 'Tok Pisin',
 'Tswana',
 'Tsonga',
 'Turkmen',
 'Tumbuka',
 'Turkish',
 'Twi',
 'Central Atlas Tamazight',
 'Uyghur',
 'Ukrainian',
 'Umbundu',
 'Urdu',
 'Northern Uzbek',
 'Venetian',
 'Vietnamese',
 'Waray',
 'Wolof',
 'Xhosa',
 'Eastern Yiddish',
 'Yoruba',
 'Yue Chinese',
 'Chinese (Simplified)',
 'Chinese (Traditional)',
 'Standard Malay',
 'Zulu']

# page header
st.title(f"Any To Any Language Translation App")
with st.form("Translate"):
   text = st.text_input("Enter text here")
   selected_option = st.selectbox("Select target Language :", options)
   #st.title(text)
 
   #
     
   submit = st.form_submit_button("Translate")
   #
   if submit:    
        print(text)
        print(selected_option)
        context = []
        language = []
        # Save the selected option to a variable
        #selected_value = options[selected_option]
        # Display the selected option and text input
        st.write("Selected Target Language :", selected_option)
        st.write("Entered text:", text)
        #
        # create a CSV file
       
        context.append(text)
        language.append(selected_option)
        input = pd.DataFrame({'context': context, 'language': language})
        print(input)
        input.to_csv('input.csv', index=False) 
        os.chmod("input.csv", 0o777)
        
        url = "https://app.aimarketplace.co/api/marketplace/models/language-translation-05408f55/predict/"
        payload={'data': open('input.csv','rb')}
        headers = {'Authorization': 'Api-Key tAKNfH3U.IdwJ3YhHeslMW1ts3gs3TZom5Orqfk1c'}

        response = requests.request("POST", url, headers=headers, files=payload)

        print(response.text)
        result = response.text
        # output header
        st.header("Translated Text")
        # output results
        st.success(f"Translated Text : {result}")