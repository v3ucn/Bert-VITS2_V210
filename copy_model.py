import shutil
import gradio as gr
import os
import webbrowser
import subprocess
import datetime
import json
import requests
import soundfile as sf
import numpy as np
import yaml
from config import config

command = r"venv\python.exe train_ms.py"
with open('config.yml', mode="r", encoding="utf-8") as f:
    configyml=yaml.load(f,Loader=yaml.FullLoader)
cfg_path=os.path.join(configyml["dataset_path"],'config.json')        
configjson = json.load(open(cfg_path))
if not configjson["train"]["skip_optimizer"]:
    configjson["train"]["skip_optimizer"]=True
    with open(cfg_path, 'w', encoding='utf-8') as f:
        json.dump(configjson, f, indent=2, ensure_ascii=False)
    print("已经修改配置文件！\n")
shutil.copy('./pretrained_models/D_0.pth',os.path.join(os.path.join(configyml["dataset_path"],configyml["train_ms"]["model"]),'D_0.pth'))
shutil.copy('./pretrained_models/G_0.pth',os.path.join(os.path.join(configyml["dataset_path"],configyml["train_ms"]["model"]),'G_0.pth'))
shutil.copy('./pretrained_models/DUR_0.pth',os.path.join(os.path.join(configyml["dataset_path"],configyml["train_ms"]["model"]),'DUR_0.pth'))
print("已经复制了底模\n")