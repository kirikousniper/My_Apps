from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()
@app.get("/data_join")
async def data_join():

    impressions = pd.read_csv("https://raw.githubusercontent.com/kirikousniper/My_Apps/main/impressions.csv")

    clics = pd.read_csv("https://raw.githubusercontent.com/kirikousniper/My_Apps/main/clics.csv")

    achats = pd.read_csv("https://raw.githubusercontent.com/kirikousniper/My_Apps/main/achats.csv")


    results= pd.merge(impressions, clics, on="cookie_id", how="left")
    fusion = pd.merge(results, achats, on="cookie_id", how="left")

    fusion_data=fusion.fillna("-")

    return fusion_data.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)