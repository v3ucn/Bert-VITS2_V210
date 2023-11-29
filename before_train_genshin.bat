@echo off
chcp 65001

call .\venv\python.exe transcribe_genshin.py

@echo 处理完毕，请按任意键继续

call .\venv\python.exe preprocess_text.py

@echo 处理完毕，请按任意键继续
call pause

call .\venv\python.exe bert_gen.py

@echo 处理完毕，请按任意键继续
call pause

call .\venv\python.exe emo_gen.py

@echo 处理完毕，请按任意键关闭
call pause