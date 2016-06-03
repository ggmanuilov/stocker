#!/usr/bin/env python3
import pprint
import os
from PIL import Image


class Thumb:
    @staticmethod
    def exist(file_origin, dist_path, stock):
        """
        Проверит существование тумьбочки, если есть то вернет false
        :param dist_path:
        :param file_origin:
        :param stock:
        :return: bool
        """
        file_name = str(os.path.split(file_origin)[-1]).split(".")[0]

        postfix = Thumb.get_postfix(file_origin, stock)
        if str(file_origin).endswith(postfix) is True:
            return True

        file_name = "".join((file_name, Thumb.get_postfix(file_origin, stock)))
        return os.path.isfile(os.path.join(dist_path, file_name))

    @staticmethod
    def create(file_origin, dist_path, stock):
        """
        Create thumbal image
        :param file_origin:   файл оригинал
        :param dist_path:     директория сохранения
        """

        if Thumb.exist(file_origin, dist_path, stock) is True:
            return True

        img = Image.open(file_origin)
        img_org_width = img.size[0]
        img_org_height = img.size[1]
        if img_org_width > img_org_height:
            wpercent = (stock.width / float(img_org_width))
            hsize = int((float(img_org_height) * float(wpercent)))
            img = img.resize((stock.width, hsize), Image.ANTIALIAS)
            img_thumb = Image.new('RGBA', (stock.width, stock.height), 'white')
            offset = (0, int((stock.height - img.size[1]) / 2))
        else:
            wpercent = (stock.height / float(img_org_height))
            hsize = int((float(img_org_width) * float(wpercent)))
            img = img.resize((hsize, stock.height), Image.ANTIALIAS)
            img_thumb = Image.new('RGBA', (stock.width, stock.height), 'white')
            offset = (int((stock.width - img.size[0]) / 2), 0)
        img_thumb.paste(img, offset)
        # extension = os.path.splitext(file_origin)[-1].lower()
        file_name = str(os.path.split(file_origin)[-1]).split(".")[0]
        postfix = Thumb.get_postfix(file_origin, stock)

        file_name = "".join((file_name, postfix))

        img_thumb.save(os.path.join(dist_path, file_name))

    @staticmethod
    def get_postfix(file_origin, stock):
        """
        Вернет постфикс создаваемой тумбочки.
        :param stock:
        :param file_origin:
        :return:
        """
        extension = os.path.splitext(file_origin)[-1].lower()

        postfix = str("").join(("_", str(stock.width), "x", str(stock.height), "_", stock.postfix, extension))

        return postfix
