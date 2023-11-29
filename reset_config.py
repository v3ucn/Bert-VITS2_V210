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

with open('config.yml', mode="r", encoding="utf-8") as f:
    configyml=yaml.load(f,Loader=yaml.FullLoader)
cfg_path=os.path.join(configyml["dataset_path"],'config.json')   
configjson = json.load(open(cfg_path))
if configjson["train"]["skip_optimizer"]:
    configjson["train"]["skip_optimizer"]=False
    with open(cfg_path, 'w', encoding='utf-8') as f:
        json.dump(configjson, f, indent=2, ensure_ascii=False)
    print("已经修改配置文件！\n")
