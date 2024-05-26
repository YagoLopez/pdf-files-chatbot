# Private AI

This is a proof of concept

In this example, we will create a private AI using the Embedchain framework.

Private AI is useful when you want to chat with your data and documents, and you dont want to spend money and your 
data should stay on your machine. In this example a PDF file will be used.

## How to install

First create a virtual environment and install the requirements by running

```bash
pip install -r requirements.txt
```

## How to use

* Now open privateai.py file and change the line `app.add` to point to your directory or data source.
* If you want to add any other data type, you can browse the supported data types [here](https://docs.embedchain.ai/components/data-sources/overview)

* Now simply run the file by

```bash
python privateai.py
```

* Now you can enter and ask any questions from your data.
* The response will contain the chat prompt in first place
* Search in the console for the "answer". That would be the real answer
* The response will contain metadata about the answer quality, embeddings used, etc.
* This is a sample of question:
```
How is the weather in Asturias?
```

* And this is a sample of response:

```
You are a Q&A expert system. Your responses must always be rooted in the context provided for each query. Here are some guidelines to follow:

1. Refrain from explicitly mentioning the context provided in your response.
2. The context should silently guide your answers without being directly acknowledged.
3. Do not use phrases such as 'According to the context provided', 'Based on the context, ...' etc.

Context information:
----------------------
rain and snow are regular weather features of Asturian winters. In coastal or near-coastal areas, daytime high temperatures generally average around 12 °C (54 °F) – 13 °C (55 °F) during winter and 22 °C (72 °F) – 23 °C (73 °F) in summer.[12]Municipalities of Asturias Parishes Geography and climate | (56.3) Mean daily minimum °C (°F)5.9 (42.6)5.7 (42.3)6.8 (44.2)7.5 (45.5)10.0 (50.0)12.8 (55.0)14.8 (58.6)15.3 (59.5)13.7 (56.7)11.3 (52.3)8.4 (47.1)6.5 (43.7)9.9 (49.8) Record low °C (°F)−3.0 (26.6)−2.6 (27.3)−2.4 (27.7)−0.6 (30.9)2.0 (35.6)5.6 (42.1)8.0 (46.4)8.4 (47.1)6.5 (43.7)3.0 (37.4)−0.8 (30.6)−3.0 (26.6)−3.0 (26.6) Average precipitation mm (inches)103 (4.1)88 (3.5)82 (3.2)99 (3.9)79 (3.1)61 (2.4)47 (1.9)60 (2.4)73 (2.9)116 (4.6)134 (5.3)117 (4.6)1,062 (41.8) Mean monthly sunshine hours 98 109 142 151 166 163 173 182 170 130 96 76 1,670 Source: Agencia Estatal de Meteorología[15] This part of Spain is one of the best conserved in the entire country, and full of vegetation and wild spaces. It holds two of the most important natural parks in Spain, and is very renowned for the Picos de Europa and Somiedo areas. The Gijón area was marked and singled out as one of the pollution hots pots in Western Europe in a 2015 report from the International Insti tute for Applied Science | Asturias in Caldoveiro Peak . The Asturian coastline is extensi ve, with hundreds of beaches, coves and natural sea caves. Notable examples include the Playa del Silencio (Beach of Silence ) near the fishing village of Cudillero (west of Gijón ), as well as the many beaches surrounding the summer resort of Llanes, such as the Barro, Ballota and Torimbia (the latter a predominantly nudist beach). Most of Asturias's beaches are sandy, clean, and bordered by steep cliffs, on top of which it is not unusual to see grazing livestock. The key features of Asturian geography are its rugged coastal cliffs and the mountainous interior. The climate of Asturias is heavily marked by the Gulf Stream. Falling within the Cantabrian belt known as Green Spain it has high precipitations all year round. Summers are mild and, on the coast, winters also have relatively benign temperatures, rarely including frost. The cold is especially felt in the mountains, where snow is present from October till May. Both
----------------------

Query: how is the weather in Asturias?
Answer:
Asturias experiences a maritime climate influenced by the Gulf Stream. The region has significant precipitation throughout the year, with mild summers and relatively benign winters along the coast. Snow is common in the mountainous interior, typically lasting from October to May.
========================================
```

```json
[
    [
        "rain and snow are regular weather features of Asturian winters. In coastal or near-coastal areas, daytime high temperatures generally average around 12 \u00b0C (54 \u00b0F) \u2013 13 \u00b0C (55 \u00b0F) during winter and 22 \u00b0C (72 \u00b0F) \u2013 23 \u00b0C (73 \u00b0F) in summer.[12]Municipalities of Asturias Parishes Geography and climate",
        {
            "app_id": "default-app-id",
            "data_type": "pdf_file",
            "doc_id": "default-app-id--7cd0cdb0edaca5a807784f8cdb91365021e05d1881df644ca82409e0c37c9661",
            "hash": "501d4d089b87cbaaa6a7b6ff03b82868",
            "page": 2,
            "source": "./docs/datasource.pdf",
            "url": "./docs/datasource.pdf",
            "score": 0.6025212711511893
        }
    ],
    [
        "(56.3) Mean daily minimum \u00b0C (\u00b0F)5.9 (42.6)5.7 (42.3)6.8 (44.2)7.5 (45.5)10.0 (50.0)12.8 (55.0)14.8 (58.6)15.3 (59.5)13.7 (56.7)11.3 (52.3)8.4 (47.1)6.5 (43.7)9.9 (49.8) Record low \u00b0C (\u00b0F)\u22123.0 (26.6)\u22122.6 (27.3)\u22122.4 (27.7)\u22120.6 (30.9)2.0 (35.6)5.6 (42.1)8.0 (46.4)8.4 (47.1)6.5 (43.7)3.0 (37.4)\u22120.8 (30.6)\u22123.0 (26.6)\u22123.0 (26.6) Average precipitation mm (inches)103 (4.1)88 (3.5)82 (3.2)99 (3.9)79 (3.1)61 (2.4)47 (1.9)60 (2.4)73 (2.9)116 (4.6)134 (5.3)117 (4.6)1,062 (41.8) Mean monthly sunshine hours 98 109 142 151 166 163 173 182 170 130 96 76 1,670 Source: Agencia Estatal de Meteorolog\u00eda[15] This part of Spain is one of the best conserved in the entire country, and full of vegetation and wild spaces. It holds two of the most important natural parks in Spain, and is very renowned for the Picos de Europa and Somiedo areas. The Gij\u00f3n area was marked and singled out as one of the pollution hots pots in Western Europe in a 2015 report from the International Insti tute for Applied Science",
        {
            "app_id": "default-app-id",
            "data_type": "pdf_file",
            "doc_id": "default-app-id--7cd0cdb0edaca5a807784f8cdb91365021e05d1881df644ca82409e0c37c9661",
            "hash": "501d4d089b87cbaaa6a7b6ff03b82868",
            "page": 4,
            "source": "./docs/datasource.pdf",
            "url": "./docs/datasource.pdf",
            "score": 0.7018021655030646
        }
    ],
    [
        "Asturias in Caldoveiro Peak . The Asturian coastline is extensi ve, with hundreds of beaches, coves and natural sea caves. Notable examples include the Playa del Silencio (Beach of Silence ) near the fishing village of Cudillero (west of Gij\u00f3n ), as well as the many beaches surrounding the summer resort of Llanes, such as the Barro, Ballota and Torimbia (the latter a predominantly nudist beach). Most of Asturias's beaches are sandy, clean, and bordered by steep cliffs, on top of which it is not unusual to see grazing livestock. The key features of Asturian geography are its rugged coastal cliffs and the mountainous interior. The climate of Asturias is heavily marked by the Gulf Stream. Falling within the Cantabrian belt known as Green Spain it has high precipitations all year round. Summers are mild and, on the coast, winters also have relatively benign temperatures, rarely including frost. The cold is especially felt in the mountains, where snow is present from October till May. Both",
        {
            "app_id": "default-app-id",
            "data_type": "pdf_file",
            "doc_id": "default-app-id--7cd0cdb0edaca5a807784f8cdb91365021e05d1881df644ca82409e0c37c9661",
            "hash": "501d4d089b87cbaaa6a7b6ff03b82868",
            "page": 2,
            "source": "./docs/datasource.pdf",
            "url": "./docs/datasource.pdf",
            "score": 0.7316455289649761
        }
    ]
]
```
