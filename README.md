## yolo trainingは別リポジトリ

## finetuning 
```bash
コンテナ内で実行
root@a70c5c57b1c2:/src/api/detect# 
$ yolo task=detect mode=train model=yolov8n.pt data=/src/api/detect/datasets/data.yaml epochs=30
```