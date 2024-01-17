# coding:utf-8

import os
import random
import argparse
import glob
import shutil


# xmlファイルからデータセットを作る
def split_train_val_from_xml(xml_file_path, txt_save_path):
    # 訓練セットと検証セットの割合
    trainval_percent = 0.9
    train_percent = 0.9

    total_xml = os.listdir(xml_file_path)
    if not os.path.exists(txt_save_path):
        os.makedirs(txt_save_path)

    num = len(total_xml)
    list_index = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list_index, tv)
    train = random.sample(trainval, tr)

    file_trainval = open(txt_save_path + "/trainval.txt", "w")
    file_test = open(txt_save_path + "/test.txt", "w")
    file_train = open(txt_save_path + "/train.txt", "w")
    file_val = open(txt_save_path + "/val.txt", "w")

    for i in list_index:
        name = total_xml[i][:-4] + "\n"
        if i in trainval:
            file_trainval.write(name)
            if i in train:
                file_train.write(name)
            else:
                file_val.write(name)
        else:
            file_test.write(name)

    file_trainval.close()
    file_train.close()
    file_val.close()
    file_test.close()


def split_images(sets, txt_save_path, original_image_path):
    for set in sets:
        # フォルダの作成
        if not os.path.exists(f"images/{set}_image/"):
            os.makedirs(f"./images/{set}_image/")
        datasets_path = txt_save_path + set + ".txt"
        with open(datasets_path, "r") as file:
            image_numbers = file.read().splitlines()

        for number in image_numbers:
            source_path = os.path.join(original_image_path, f"{number}.jpg")
            destination_path = os.path.join(f"./images/{set}_image/", f"{number}.jpg")

            # ファイルをコピーする
            shutil.copy(source_path, destination_path)


if __name__ == "__main__":
    # 各ファイルのコピー先ディレクトリを定義
    xml_file_path = "./Annotations/"
    txt_save_path = "./DatasetSplit/"
    original_image_path = "./original"
    sets = ["train", "test", "trainval", "val"]

    split_train_val_from_xml(xml_file_path, txt_save_path)
    # split_images(sets, txt_save_path, original_image_path)
