import csv
import json
import os
import random
import re
import tkinter
import warnings
from collections import Counter
from time import sleep
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
from tkinter.ttk import *
import urllib.parse
import ijson
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from lxml import html
from pandas.core.common import SettingWithCopyWarning
from progress.bar import Bar
from requests.exceptions import ConnectionError
from difflib import SequenceMatcher
from selenium.common.exceptions import NoSuchElementException

m = tkinter.Tk()
m.title('Feeds Tool v1.0')

img = b'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'

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.simplefilter(action="ignore", category=XMLParsedAsHTMLWarning)
warnings.simplefilter(action="ignore", category=UserWarning)
warnings.simplefilter(action="ignore", category=FutureWarning)


def openme():
    ipfilename = filedialog.askopenfilename(title="Select file", filetypes=([("excel files", "*.xlsx")]))
    pathi.delete(0, END)
    pathi.insert(0, ipfilename)


def openref():
    ipfilename = filedialog.askopenfilename(title="Select file", filetypes=(
        ("excel files", "*.xlsx"), ("txt file", "*.txt"), ("csv files", "*.csv*"), ("all files", "*.*")))
    pathr.delete(0, END)
    pathr.insert(0, ipfilename)


def jsonfile():
    file_var = filedialog.askopenfilename(filetypes=[('JSON File', '.json')])
    pathj.delete(0, END)
    pathj.insert(0, file_var)


def saveme():
    opfilename = filedialog.asksaveasfilename(title="Save as file",
                                              filetypes=([("excel files", "*.xlsx"), ("CSV", "*.csv")]))
    patho.delete(0, END)
    patho.insert(0, opfilename)


def diff_bot():
    if patho.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for output file')
    if pathi.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for input file')
    else:
        global market_place_input
        json_file = open("inputs.json", "rb")
        inputs = json.load(json_file)
        global market_place, pos_currency
        market_place_input = askstring("Input", "Enter Markertplace name")
        n = 5
        while n > 0:
            try:
                if market_place_input:
                    for text in inputs["marketplace"]:
                        if text.lower().strip() == market_place_input.lower():
                            market_place = inputs["marketplace"][text][0]
                            pos_currency = inputs["marketplace"][text][1]
                            break
                if market_place:
                    ip_data = pd.read_excel(pathi.get())
                    ip_data["pos_currency"] = pos_currency
                    mandatory_dp1 = ['brand_name', 'title', 'brand']
                    mandatory_dp2 = ['model', 'part_number', 'external_id']
                    present_dp = ""
                    mand_count1 = 0
                    mand_count2 = 0
                    for i in mandatory_dp1:
                        if i in ip_data.columns:
                            mand_count1 += 1
                    for i in mandatory_dp2:
                        if i in ip_data.columns:
                            mand_count2 += 1

                    if mand_count1 == 2:
                        if mand_count2 > 0:
                            for j in mandatory_dp2:
                                if j in ip_data.columns:
                                    present_dp = j
                                    break
                            if "concat" not in ip_data.columns:
                                if "brand_name" in ip_data.columns:
                                    ip_data["concat"] = ip_data['brand_name'].fillna("").astype(str).replace('nan','') + " " + ip_data['title'].fillna("").astype(str).replace('nan','') + " " + ip_data[present_dp].fillna("").astype(str).replace('nan','')
                                elif "brand" in ip_data.columns:
                                    ip_data["concat"] = ip_data['brand'].fillna("").astype(str).replace('nan','') + " " + ip_data['title'].fillna("").astype(str).replace('nan','') + " " + ip_data[present_dp].fillna("").astype(str).replace('nan','')
                            bar = Bar('Generating google URL : ', max=len(ip_data))

                            # remove duplicate words
                            # for ind in range(len(ip_data.index)):
                            #     input = ip_data["concat"][ind].split(" ")
                            #     UniqW = Counter(input)
                            #     ip_data["concat"][ind] = " ".join(UniqW.keys())
                            ip_data["google_url"] = ""
                            for ind in ip_data.index:
                                ip_data["google_url"][ind] = market_place + "/search?q=" + urllib.parse.quote(
                                    ip_data['concat'][ind])
                                bar.next()
                            bar.finish()
                        del market_place

                    ip_data.to_excel(re.sub("_google_urls.xlsx|_google_urls|.xlsx", "", patho.get()) + "_google_urls.xlsx", index=False)
                    messagebox.showinfo('Alert', "Diff-Bot Url's generated")
                    break
            except NameError:
                messagebox.showerror('Error', 'Enter a valid marketplace name')
                break

            # Diffbot URl
            # https://www.diffbot.com/dev/login/?forward=/dev/bulk/
            # a27e5774de3e4c4e8d044e6b3ce467e3
            # Name of the job:, product API, URLS, Querystring : fields=dom, email id : job completion, click -> start bulk job


def scrape():
    if not os.path.isfile(pathi.get()):
        messagebox.showerror('Input File Missing', 'Please choose input file')
    elif pathi.get() == '':
        messagebox.showerror('Please choose input file')
    elif patho.get() == '':
        messagebox.showerror('Please specify location and name for output file')
    else:
        urls = []
        json_file = open(".\inputs.json", "rb")
        inputs = json.load(json_file)

        ip_data1 = pd.read_excel(pathi.get())
        for url in ip_data1["product_url"]:
            urls.append(url)

        with open(r'.\restriction.txt', 'r') as key2:
            rst = csv.reader(key2)
            restrictions = []
            for restriction in rst:
                restrictions.append(''.join(restriction))

        user_agent_list = [
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            # Firefox
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
            'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        ]
        crawl_response = open(patho.get() + '_crawl_response.txt', 'a')
        required_dp = ['brand_name', 'manufacturer_name', 'external_id', 'model',
                       'part_number', 'brand'
                                      'color_name', 'size', 'item_package_quantity']
        available_dp = []
        for dp1 in required_dp:
            for dp2 in ip_data1.columns:
                if dp1 == dp2:
                    available_dp.append(dp1)

        for col in ip_data1.columns:
            if "check" in col or "null_count" in col:
                ip_data1.drop(col, inplace=True, axis=1)
        output_data = ip_data1.copy()

        for i in available_dp:
            output_data.insert(len(output_data.columns), i + "_check", '')

        output_data['title_check'] = ""
        output_data["final_rating"] = ""

        ind = -1
        if len(output_data.columns) + 1 > len(ip_data1.columns):
            print("Total number of rows : ", ip_data1[ip_data1.columns[len(ip_data1.columns) - 1]].count())
            bar = Bar('Scrape : ', max=ip_data1[ip_data1.columns[len(ip_data1.columns) - 1]].count())
            for n1 in output_data["product_url"]:
                ind += 1
                if "http" in str(output_data["product_url"][ind]):
                    try:
                        user_agent = random.choice(user_agent_list)
                        headers = {'User-Agent': user_agent}
                        response = requests.get(n1, headers=headers, allow_redirects=True, timeout=30)
                        crawl_response.write(n1 + "," + str(response.status_code) + '\n')
                        soup = BeautifulSoup(response.content, "lxml")
                        [x.extract() for x in soup.findAll(['script', 'style'])]
                        html1 = soup.findAll(text=True)
                        html_document = response.text
                        scan = []
                        scan1 = []
                        clean = 0
                        clean1 = ''
                        for count2, line in enumerate(html1):  # each element count
                            if clean == 0:
                                for restriction in restrictions:
                                    if restriction in line.lower():
                                        clean = count2
                                        break
                            else:
                                break
                        for count3, line in enumerate(html1):
                            if clean == 0:
                                if '{' in line:
                                    continue
                                if '}' in line:
                                    continue
                                if len(line) > 2:
                                    scan1.append(line.lower().strip())
                            if clean > 0:
                                if count3 == clean:
                                    break
                                else:
                                    if '{' in line:
                                        continue
                                    if '}' in line:
                                        continue
                                    if len(line) > 2:
                                        scan1.append(line.lower().strip())

                        for eachline1 in scan1:
                            if '. ' in eachline1:
                                dept = eachline1.split('. ')
                                for sentence in dept:
                                    scan.append(sentence)
                            else:
                                scan.append(eachline1)
                        clean1 = ''.join(str(v) for v in scan)
                        matched_count = 0

                        if output_data["url_title"][ind]:
                            s = SequenceMatcher(None, str(output_data["url_title"][ind]).lower(),
                                                str(output_data["title"][ind]).lower())
                            if s.ratio() * 100 >= 95:
                                output_data['title_check'][ind] = "Matched"
                                matched_count += 1
                            elif s.ratio() * 100 >= 30:
                                output_data['title_check'][ind] = "Partial match"
                                matched_count += 0.5
                            else:
                                output_data['title_check'][ind] = "Not-matched"

                        for av in available_dp:
                            for key in inputs["keywords"]:
                                if key == av:
                                    for value in inputs["keywords"][av]:
                                        check = re.search(str(value).lower() + ".*" + str(output_data[av][ind]).lower(),
                                                          clean1.lower())
                                        if check is not None:
                                            output_data[av + "_check"][ind] = "Matched"
                                            matched_count += 1
                                            break
                                        else:
                                            output_data[av + "_check"][ind] = "Not-matched"

                        output_data["final_rating"][ind] = (matched_count / (len(available_dp) + 1)) * 100

                    except requests.HTTPError as inst:
                        crawl_response.write(str(n1) + "," + str(inst) + '\n')
                        sleep(0.4)
                    except requests.exceptions.ReadTimeout as inst1:
                        crawl_response.write(str(n1) + "," + str(inst1) + '\n')
                        sleep(0.4)
                    except requests.exceptions.TooManyRedirects as inst2:
                        crawl_response.write(str(n1) + "," + str(inst2) + '\n')
                    except (ConnectionError, ConnectionResetError) as cnn:
                        crawl_response.write(str(n1) + "," + str(cnn) + '\n')
                        sleep(1)
                    except IndexError as ind:
                        crawl_response.write(str(n1) + "," + str(ind) + '\n')
                    except requests.exceptions.ContentDecodingError as Decodeerr:
                        crawl_response.write(str(n1) + "," + str(Decodeerr) + '\n')
                    except NoSuchElementException as e:
                        crawl_response.write(str(n1) + "," + str(e) + '\n')
                    except ValueError as f:
                        crawl_response.write(str(n1) + "," + str(f) + '\n')
                    bar.next()
            crawl_response.close()

            writer = pd.ExcelWriter(re.sub("_scrape.xlsx|_scrape|.xlsx", "", patho.get()) + "_scrape.xlsx", engine='xlsxwriter')
            output_data.to_excel(writer, sheet_name='Scraped Data', index=False)
            writer.save()
            bar.finish()
            messagebox.showinfo('Alert', "Scrape Completed")
        else:
            print("No Dp's to check")


def parser():
    if patho.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for output file')
    if pathi.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for input file')
    else:
        print("Reading your Input file.. Please wait..!!")
        ip_data = pd.read_excel(pathi.get())
        json_file = open(".\input_schema.json", "rb")
        inputs = json.load(json_file)

        for column in ip_data:
            for i in inputs["drop_schema"]:
                if "Unnamed" in str(column):
                    ip_data.drop(column, inplace=True, axis=1)
                elif str(i).lower() == column.lower() or str(i).lower() in column.lower():
                    print("Dropping column", column)
                    ip_data.drop(column, inplace=True, axis=1)

        for column in ip_data:
            for json_key in inputs["schema_rename"]:
                for check in inputs["schema_rename"][json_key]:
                    if str(re.sub(r'(\_[0-9]$)|[0-9]', '', column)).lower().strip() == str(check).lower():
                        print("Renaming", column, "to :", json_key)
                        ip_data.rename(columns={column: json_key}, inplace=True)
                        break

        if 'is_pos_data' not in ip_data.columns:
            ip_data["is_pos_data"] = "Y"

        if 'pos_currency' not in ip_data.columns:
            ip_data["pos_currency"] = ""

        # ip_data = ip_data.dropna(subset=['brand','brand_name','manufacturer_name'], how='all')
        # ip_data = ip_data.dropna(subset=['brand_name'])
        # ip_data = ip_data.dropna(subset=['manufacturer_name'])

        if 'title' not in ip_data.columns:
            print('Generating title :', len(ip_data), 'processing ', end='')
            ip_data["title"] = ""

            if 'brand_name' in ip_data.columns:
                # ip_data["brand_name"] = ip_data['brand_name'].values.astype(str)
                if 'part_number' in ip_data.columns:
                    ip_data["title"] = ip_data['brand_name'].astype(str) + " " + ip_data['part_number'].astype(
                        str).fillna("")
                elif 'model' in ip_data.columns:
                    ip_data["title"] = ip_data['brand_name'].astype(str) + " " + ip_data['model'].astype(
                        str).fillna("")
                else:
                    ip_data["title"] = "Need brand and part number/model data points"

            elif 'brand' in ip_data.columns:
                # ip_data["brand"] = ip_data['brand'].values.astype(str)
                if 'part_number' in ip_data.columns:
                    ip_data["title"] = ip_data['brand'].astype(str) + " " + ip_data['part_number'].astype(
                        str).fillna("")
                elif 'brand' in ip_data.columns and 'model' in ip_data.columns:
                    ip_data["title"] = ip_data['brand'].astype(str) + " " + ip_data['model'].astype(
                        str).fillna("")
                else:
                    ip_data["title"] = "Need brand and part number/model data points"
            print(': completed')

        if 'title' in ip_data.columns:
            print('title check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"(\s[Ss][Tt][Dd])|[#$@~]|(\s[1]\s[Mm][Uu]).*"
            ip_data["title_check"] = ip_data['title'].str.contains(reg)
            ip_data.loc[(ip_data.title_check == True), 'title_check'] = 'Junk'
            ip_data.loc[ip_data['title'].isnull(), 'title_check'] = 'Blank'
            ip_data.loc[(ip_data.title_check == False), 'title_check'] = ''
            ip_data["title_Junks"] = ip_data['title'].str.findall(reg)
            print(': completed')

        if 'sku' not in ip_data.columns:
            ip_data["sku"] = ""
            print('Generating sku : processing', end=' ')

            if 'external_id' in ip_data.columns:
                ip_data["sku"] = ip_data['external_id'].values.astype(str)
                ip_data["sku"] = ip_data['sku'].str.replace(r'(\..*)', '')
                ip_data.loc[ip_data["sku"] == "nan", "sku"] = ""
            elif 'brand_name' in ip_data.columns:
                if 'title' in ip_data.columns and 'model' in ip_data.columns:
                    ip_data["sku"] = ip_data['title'].astype(str) + " " + ip_data['brand_name'].astype(
                        str).fillna("") + " " + ip_data['model'].astype(str)
                elif 'title' in ip_data.columns and 'product_category' in ip_data.columns:
                    ip_data["sku"] = ip_data['title'].astype(str) + " " + ip_data['brand_name'].astype(
                        str).fillna("") + " " + ip_data['product_category'].astype(str)
                else:
                    ip_data["sku"] = ip_data["title"].values.astype(str)
                    ip_data.loc[ip_data["sku"].isna, "sku"] = ""

            elif 'brand' in ip_data.columns:
                if 'title' in ip_data.columns and 'model' in ip_data.columns:
                    ip_data["sku"] = ip_data['title'].astype(str) + " " + ip_data['brand'].astype(
                        str).fillna("") + " " + ip_data['model'].astype(str)
                elif 'title' in ip_data.columns and 'product_category' in ip_data.columns:
                    ip_data["sku"] = ip_data['title'].astype(str) + " " + ip_data['brand_name'].astype(
                        str).fillna("") + " " + ip_data['product_category'].astype(str)
                else:
                    ip_data["sku"] = ip_data["title"].values.astype(str)
            print(': completed')

        if 'sku' in ip_data.columns:
            print('sku check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([_@./#&+])"
            ip_data["sku_check"] = ip_data['sku'].str.contains(reg)
            ip_data.loc[(ip_data.sku_check == True), 'sku_check'] = 'Junk'
            ip_data.loc[ip_data['sku'].isnull(), 'sku_check'] = 'Blank'
            ip_data.loc[(ip_data.sku_check == False), 'sku_check'] = ''
            ip_data["sku_Junks"] = ip_data['sku'].str.findall(reg)
            print(': completed')

        if 'brand_name' in ip_data.columns:
            print('brand_name_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([_@./#&+])"
            ip_data["brand_name_check"] = ip_data['brand_name'].str.contains(reg)
            ip_data.loc[(ip_data.brand_name_check == True), 'brand_name_check'] = 'Junk'
            ip_data.loc[ip_data['brand_name'].isnull(), 'brand_name_check'] = 'Blank'
            ip_data.loc[(ip_data.brand_name_check == False), 'brand_name_check'] = ''
            ip_data["brand_name_Junks"] = ip_data['brand_name'].str.findall(reg)
            print(': completed')

        elif 'brand' in ip_data.columns:
            print('brand_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([_@./#&+])"
            ip_data["brand_check"] = ip_data['brand'].str.contains(reg)
            ip_data.loc[(ip_data.brand_check == True), 'brand_check'] = 'Junk'
            ip_data.loc[ip_data['brand'].isnull(), 'brand_check'] = 'Blank'
            ip_data.loc[(ip_data.brand_check == False), 'brand_check'] = ''
            ip_data["brand_Junks"] = ip_data['brand'].str.findall(reg)
            print(': completed')

        if 'bread_crumb1' in ip_data.columns:
            print('bread_crumb1_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"[\'@_!$#%^&*+=;()<>\[\]?/\|}{~:\€\£%]"
            ip_data["bread_crumb1_check"] = ip_data['bread_crumb1'].str.contains(reg)
            ip_data.loc[(ip_data.bread_crumb1_check == True), 'bread_crumb1_check'] = 'Junk'
            ip_data.loc[ip_data['bread_crumb1'].isnull(), 'bread_crumb1_check'] = 'Blank'
            ip_data.loc[(ip_data.bread_crumb1_check == False), 'bread_crumb1_check'] = ''
            ip_data["bread_crumb1_Junks"] = ip_data['bread_crumb1'].str.findall(reg)
            print(': completed')

        if 'bread_crumb2' in ip_data.columns:
            print('bread_crumb2_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"[\'@_!$#%^&*+=;()<>\[\]?/\|}{~:\€\£%]"
            ip_data["bread_crumb2_check"] = ip_data['bread_crumb2'].str.contains(reg)
            ip_data.loc[(ip_data.bread_crumb2_check == True), 'bread_crumb2_check'] = 'Junk'
            ip_data.loc[ip_data['bread_crumb2'].isnull(), 'bread_crumb2_check'] = 'Blank'
            ip_data.loc[(ip_data.bread_crumb2_check == False), 'bread_crumb2_check'] = ''
            ip_data["bread_crumb2_Junks"] = ip_data['bread_crumb2'].str.findall(reg)
            print(': completed')

        if 'bread_crumb3' in ip_data.columns:
            print('bread_crumb3_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"[\'@_!$#%^&*+=;()<>\[\]?/\|}{~:\€\£%]"
            ip_data["bread_crumb3_check"] = ip_data['bread_crumb3'].str.contains(reg)
            ip_data.loc[(ip_data.bread_crumb3_check == True), 'bread_crumb3_check'] = 'Junk'
            ip_data.loc[ip_data['bread_crumb3'].isnull(), 'bread_crumb3_check'] = 'Blank'
            ip_data.loc[(ip_data.bread_crumb3_check == False), 'bread_crumb3_check'] = ''
            ip_data["bread_crumb3_Junks"] = ip_data['bread_crumb3'].str.findall(reg)
            print(': completed')

        if 'remaining_bread_crumbs' in ip_data.columns:
            print('remaining_bread_crumbs_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"[\'@_!$#%^&*+=;()<>\[\]?/\|}{~:\€\£%]"
            ip_data["remaining_bread_crumbs_check"] = ip_data['remaining_bread_crumbs'].str.contains(reg)
            ip_data.loc[(ip_data.remaining_bread_crumbs_check == True), 'remaining_bread_crumbs_check'] = 'Junk'
            ip_data.loc[ip_data['remaining_bread_crumbs'].isnull(), 'remaining_bread_crumbs_check'] = 'Blank'
            ip_data.loc[(ip_data.remaining_bread_crumbs_check == False), 'remaining_bread_crumbs_check'] = ''
            ip_data["remaining_bread_crumbs_Junks"] = ip_data['remaining_bread_crumbs'].str.findall(reg)
            print(': completed')

        if 'external_id' in ip_data.columns:
            ip_data["external_id"] = ip_data['external_id'].values.astype(str)
            ip_data["external_id"] = ip_data['external_id'].str.replace(r'(\..*)', '')
            ip_data.loc[ip_data["external_id"] == "nan", "external_id"] = ""
            print('external_id_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([A-Za-z_@./#&+-])"
            ip_data["external_id_check"] = ip_data['external_id'].str.contains(reg)
            ip_data.loc[(ip_data.external_id_check == True), 'external_id_check'] = 'Junk'
            ip_data.loc[ip_data['external_id'].isnull(), 'external_id_check'] = 'Blank'
            ip_data.loc[(ip_data.external_id_check == False), 'external_id_check'] = ''
            ip_data["external_id_Junks"] = ip_data['external_id'].str.findall(reg)
            print(': completed')

        if 'model' in ip_data.columns:
            print('model_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([Mm][Uu][Ll][Tt][Ii])|([Mm][Mm])|([Mm][Ll])|([Kk][Gg])|([_@\/#&+\(\)])"
            ip_data["model_check"] = ip_data['model'].str.contains(reg)
            ip_data.loc[(ip_data.model_check == True), 'model_check'] = 'Junk'
            ip_data.loc[ip_data['model'].isnull(), 'model_check'] = 'Blank'
            ip_data.loc[(ip_data.model_check == False), 'model_check'] = ''
            ip_data["model_Junks"] = ip_data['model'].str.findall(reg)
            print(': completed')

        if 'part_number' in ip_data.columns:
            print('part_number_check : ', len(ip_data), 'rows processing', end=' ')
            ip_data["part_number"] = ip_data['part_number'].values.astype(str)
            ip_data.loc[ip_data["part_number"] == "nan", "part_number"] = ""
            ip_data["part_number"] = ip_data['part_number'].str.replace(r'(\..*)', '')
            reg = r"([Mm][Uu][Ll][Tt][Ii])|([Mm][Mm])|([Mm][Ll])|([Kk][Gg])|([_@\/#&+\(\)])"
            ip_data["part_number_check"] = ip_data['part_number'].str.contains(reg)
            ip_data.loc[(ip_data.part_number_check == True), 'part_number_check'] = 'Junk'
            ip_data.loc[ip_data['part_number'].isnull(), 'part_number_check'] = 'Blank'
            ip_data.loc[(ip_data.part_number_check == False), 'part_number_check'] = ''
            ip_data["part_number_Junks"] = ip_data['part_number'].str.findall(reg)
            print(': completed')

        if 'has_retail_offer' in ip_data.columns:
            print('part_number_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([_@\/#&+\(\)])"
            ip_data["has_retail_offer_check"] = ip_data['has_retail_offer'].str.contains(reg)
            ip_data.loc[(ip_data.has_retail_offer_check == True), 'has_retail_offer_check'] = 'Junk'
            ip_data.loc[ip_data['has_retail_offer'].isnull(), 'has_retail_offer_check'] = 'Blank'
            ip_data.loc[(ip_data.has_retail_offer_check == False), 'has_retail_offer_check'] = ''
            ip_data["has_retail_offer_Junks"] = ip_data['has_retail_offer'].str.findall(reg)
            print(': completed')

        if 'has_3p_offer' in ip_data.columns:
            print('has_3p_offer_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([_@\/#&+\(\)])"
            ip_data["has_3p_offer_check"] = ip_data['has_3p_offer'].str.contains(reg)
            ip_data.loc[(ip_data.has_3p_offer_check == True), 'has_3p_offer_check'] = 'Junk'
            ip_data.loc[ip_data['has_3p_offer'].isnull(), 'has_3p_offer_check'] = 'Blank'
            ip_data.loc[(ip_data.has_3p_offer_check == False), 'has_3p_offer_check'] = ''
            ip_data["has_3p_offer_Junks"] = ip_data['has_3p_offer'].str.findall(reg)
            print(': completed')

        if 'list_price' in ip_data.columns:
            print('list_price_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([A-Za-z_@\/#&+\(\)])"
            ip_data["has_3p_offer_check"] = ip_data['list_price'].str.contains(reg)
            ip_data.loc[(ip_data.list_price_check == True), 'list_price_check'] = 'Junk'
            ip_data.loc[ip_data['list_price'].isnull(), 'list_price_check'] = 'Blank'
            ip_data.loc[(ip_data.list_price_check == False), 'list_price_check'] = ''
            ip_data["list_price_Junks"] = ip_data['list_price'].str.findall(reg)
            print(': completed')

        if 'deprecated_our_price' in ip_data.columns:
            print('deprecated_our_price_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([A-Za-z_@\/#&+\(\)])"
            ip_data["deprecated_our_price_check"] = ip_data['deprecated_our_price'].str.contains(reg)
            ip_data.loc[(ip_data.deprecated_our_price_check == True), 'deprecated_our_price_check'] = 'Junk'
            ip_data.loc[ip_data['deprecated_our_price'].isnull(), 'deprecated_our_price_check'] = 'Blank'
            ip_data.loc[(ip_data.deprecated_our_price_check == False), 'deprecated_our_price_check'] = ''
            ip_data["deprecated_our_price_Junks"] = ip_data['deprecated_our_price'].str.findall(reg)
            print(': completed')

        if 'offering_availability' in ip_data.columns:
            print('offering_availability_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([Ii][Nn])?([Oo][Uu][Tt]\s[Oo][Ff])?\s[Ss][Tt][Oo][Cc][Kk]"
            ip_data["offering_availability_check"] = ip_data['offering_availability'].str.contains(reg)
            ip_data.loc[(ip_data.offering_availability_check == True), 'offering_availability_check'] = 'Junk'
            ip_data.loc[ip_data['offering_availability'].isnull(), 'offering_availability_check'] = 'Blank'
            ip_data.loc[(ip_data.offering_availability_check == False), 'offering_availability_check'] = ''
            ip_data["offering_availability_Junks"] = ip_data['offering_availability'].str.findall(reg)
            print(': completed')

        if 'color_name' in ip_data.columns:
            print('color_name_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"([0-9_@./#&+-])"
            ip_data["color_name_check"] = ip_data['color_name'].str.contains(reg)
            ip_data.loc[(ip_data.color_name_check == True), 'color_name_check'] = 'Junk'
            ip_data.loc[ip_data['color_name'].isnull(), 'color_name_check'] = 'Blank'
            ip_data.loc[(ip_data.color_name_check == False), 'color_name_check'] = ''
            ip_data["color_name_Junks"] = ip_data['color_name'].str.findall(reg)
            print(': completed')

        if 'url' in ip_data.columns:
            print('url_check : ', len(ip_data), 'rows processing', end=' ')
            reg = r"((SMTQUERY).){3,}"
            ip_data["url_check"] = ip_data['url'].str.contains(reg)
            ip_data.loc[(ip_data.url_check == True), 'url_check'] = 'Junk'
            ip_data.loc[ip_data['url'].isnull(), 'url_check'] = 'Blank'
            ip_data.loc[(ip_data.url_check == False), 'url_check'] = ''
            ip_data["url_Junks"] = ip_data['url'].str.findall(reg)
            print(': completed')

        if 'size' in ip_data.columns:
            print('size_check : ', len(ip_data), 'rows processing', end=' ')
            ip_data["size"] = ip_data['size'].values.astype(str)
            ip_data.loc[ip_data["size"] == "nan", "size"] = ""
            ip_data["size"] = ip_data['size'].str.replace(r'(\..*)', '')
            reg = r"([Mm][Uu][Ll][Tt][Ii])|([Mm][Ll])|([Kk][Gg])|([_@.\/#&+\(\)])"
            ip_data["size_check"] = ip_data['size'].str.contains(reg)
            ip_data.loc[(ip_data.size_check == True), 'size_check'] = 'Junk'
            ip_data.loc[ip_data['size'].isnull(), 'size_check'] = 'Blank'
            ip_data.loc[(ip_data.size_check == False), 'size_check'] = ''
            ip_data["size_Junks"] = ip_data['size'].str.findall(reg)
            print(': completed')

        # checking null count
        print('Counting null : ', len(ip_data), 'rows processing', end=' ')
        ip_data['null_count'] = (len(ip_data.columns) - 1) - (ip_data.count(axis='columns') - 1)
        print(": completed")

        if 'manufacturer_name' in ip_data.columns and "brand_name" in ip_data.columns:
            ip_data['brand_name'] = ip_data['brand_name'].fillna(ip_data['manufacturer_name'])
        if 'manufacturer_name' in ip_data.columns and "brand" in ip_data.columns:
            ip_data['brand'] = ip_data['brand'].fillna(ip_data['manufacturer_name'])

        if "brand" in ip_data.columns:
            index_remove = ip_data[
                (ip_data['brand'] == "その他") | (ip_data['brand'] == 'others') | (ip_data['brand'] == '(others)')].index
            ip_data.drop(index_remove, inplace=True)
        if "brand_name" in ip_data.columns:
            index_remove = ip_data[(ip_data['brand_name'] == "その他") | (ip_data['brand_name'] == 'others') | (
                        ip_data['brand_name'] == '(others)')].index
            ip_data.drop(index_remove, inplace=True)
        if "manufacturer_name" in ip_data.columns:
            index_remove = ip_data[
                (ip_data['manufacturer_name'] == "その他") | (ip_data['manufacturer_name'] == 'others') | (
                            ip_data['manufacturer_name'] == '(others)')].index
            ip_data.drop(index_remove, inplace=True)

        print("Exporting DataFrame to Excel, Please wait")
        ip_data = ip_data.sort_values(by='null_count')
        writer = pd.ExcelWriter(re.sub("_data_parser.xlsx|_data_parser|.xlsx", "", patho.get()) + "_data_parser.xlsx")
        ip_data.to_excel(writer, sheet_name='data_parser', index=False)
        writer.save()

        # taking sample data
        df_sample = ip_data.head(2000)
        writer = pd.ExcelWriter(re.sub("_Sample_data.xlsx|_Sample_data|.xlsx", "", patho.get()) + "_Sample_data.xlsx")
        df_sample.to_excel(writer, sheet_name='sample_data', index=False)
        writer.save()
        print("DataFrame is written to Excel File successfully.")
        messagebox.showinfo('Alert', 'Data parser completed')


def compare():
    if patho.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for output file')
    if pathr.get() == '':
        messagebox.showerror('Json File Name Missing', 'Please specify location and name for Json output file')
    if pathi.get() == '':
        messagebox.showerror('Input File Name Missing', 'Please specify location and name for Input file')
    else:
        ip_data1 = pd.read_excel(pathr.get())
        ip_data1.dropna(inplace=True)
        ip_data2 = pd.read_excel(pathi.get())
        print('comparing JSON & Raw data : ', end=' ')
        final_op = ip_data2.merge(ip_data1, on='concat', how='left')
        for column in final_op:
            if column == "diffbot_url":
                final_op.drop(column, inplace=True, axis=1)
        print(len(ip_data2), 'rows processing', end=' ')
        final_op.to_excel(re.sub("_compare_data.xlsx|_compare_data|.xlsx", "", patho.get()) + "_compare_data.xlsx", index=False)
        print(' : completed')
        messagebox.showinfo('Alert', "Compare data completed")


def Offline_search():
    if patho.get() == '':
        messagebox.showerror('Output File Name Missing', 'Please specify location and name for output file')
    if pathj.get() == '':
        messagebox.showerror('Json File Name Missing', 'Please specify location and name for Json file')
    else:
        data = ijson.items(open(pathj.get(), 'r', encoding='utf-8'), 'item')
        json_file = open(pathj.get(), "rb")
        print('Loading JSON.....')
        inputs = json.load(json_file)
        bar = Bar('JSON to Excel : ', max=len(inputs))
        with open(patho.get() + '.txt', 'w', encoding='utf-8', newline='') as file:
            datasheet = csv.writer(file, delimiter=';')
            datasheet.writerow(['diffbot_url', 'concat', 'url_title', 'product_url'])
            count = 0
            for row in data:
                count += 1
                key = row['pageUrl']
                keyword = row['pageUrl'].split('q=')[1].replace('+', ' ').replace('compatible models', '')
                page = html.fromstring(row['dom'])
                url = page.xpath(
                    "(//div//a[h3])[not(contains(.,'Images ')) and not(contains(@style,'display:none')) and not(contains(@href,'amazon')) and not(contains(@href,'youtube')) and not(contains(@href,'ebay'))and not(contains(@href,'google'))and not(contains(@href,'facebook'))and not(contains(@href,'twitter')) and not(contains(@href,'quora'))and not(contains(@href,'wiki')) and not(contains(.,'uestion'))and not(contains(.,'eviews'))and not(contains(.,'itemap'))and not(contains(.,'gov'))and not(contains(.,'xml'))and not(contains(.,'/tag'))and not(contains(.,'/docs'))and not(contains(.,'review'))and not(contains(.,'dailymotion'))]")
                useful = "(//div//a[h3])[not(contains(.,'Images ')) and not(contains(@style,'display:none')) and not(contains(@href,'amazon')) and not(contains(@href,'youtube')) and not(contains(@href,'ebay'))and not(contains(@href,'google'))and not(contains(@href,'facebook'))and not(contains(@href,'twitter')) and not(contains(@href,'quora'))and not(contains(@href,'wiki')) and not(contains(.,'uestion'))and not(contains(.,'eviews'))and not(contains(.,'itemap'))and not(contains(.,'gov'))and not(contains(.,'xml'))and not(contains(.,'/tag'))and not(contains(.,'/docs'))and not(contains(.,'review'))and not(contains(.,'dailymotion'))]"
                j = 1
                for j in range(len(url)):
                    title = page.xpath('(' + useful + '/h3)[' + str(j) + ']//text()')
                    prod_url = page.xpath('(' + useful + '/@href)[' + str(j) + ']')
                    datasheet.writerow([key, urllib.parse.unquote(keyword), "".join(title), "".join(prod_url)])
                bar.next()
            bar.finish()

        df = pd.read_csv(patho.get() + ".txt", sep=';')
        prod_reg = re.compile(
            '(.*collection.*)|(.*/?p=.*)|(.*varumarken.*)|(.*prodotti.*)|(.*produto.*)|(.*productos.*)|(.*[Ss][Kk][Uu].*)|(.*_p/.*)|(.*producto.*)|(.*pid=.*)|(.*prodotto.*)|(.*partnumber.*)|(.*product_info.*)|(.*produtos.*)|(.*variantId.*)|(.*/?product-page.*)|(.*/produkte/.*)|(.*variantID.*)|(.*[Pp]rodukt.*)|(.*[Ss]eries.*)|(.*[Aa]rticulo.*)|(.*pd=)|(.*[Pp]roduktliste.*)|(.*\.[Ss]how.*)|([0-9]{8,})|(.*/o/.*)|(.*model.*)|(.*accessories.*)|(.*node.*)|(.*[Vv]ariant.*)|(.*/f/.*)|(.*shop.*)|(.*/[Ss]tore.*)|(.*[Oo]rder.*)|(.*content.*)|(.*id=.*)|(.*/[Ii]tem/.*)|(.*/aid.*)|(.*/pd.*)|(.*/view/.*)|(.*/csp.*)|(.*/-p[0-9]+.*)|(.*/g/.*)|(.*/[Ss]upplies/.*)|(.*part.*)|(.*p=[0-9A-Z]+)|(.*/.*/mpid:.*)|(.*/detail.*)|(.*/details/index/[0-9]+/.*)|.*/dp/.*|(.*/ITEM/.*)|(.*/p/.*)|(.*\/prod\-.*)|(.*\-model\-.*)|(.*idProduct=.*)|.*=product:([A-Z0-9]+)\-.*|.*&itemID=.*|(.*ID=[0-9]+)|.*&prodID=.*|.*(/ITEM/).*|.*(/p/).*|.*(/p/|/productdetail/).*|.*(/Product).*|.*(/product/).*|.*(/product/|Product_Code=).*|.*(/Product/Detail|CItem=).*|.*(/product[0-9]+|products\_id=[0-9]+).*|.*(/[Pp]roducts/).*|.*(\/productdisplay\/).*|.*(goodsp?=).*|.*(Item=).*|.*(PID\-).*|.*(productId=|/prod\_|/product\_).*|.*(productid=).*|.*/.*Item=.*|.*/.*product=([0-9]+)|.*DetailsProduit.*|.*model/show/.*|.*/products/.*|.*/[0-9]+/artikel\.htm.*|.*/[Pp]roduct|.*/[Pp]roduct/.*|.*/[Pp]roduct\.aspx.*|.*/[Pp]roduct\.aspx.*|.*/catalog/product/.*|.*/detail.*|.*/details/.*|.*/goods/.*|.*/item/([^/]+)/.*|.*/ITEM/.*|.*/item\-(D|d)etails\.asp.*|.*/item\-details\.asp.*|.*/item_.*|.*/itemDetailInit.*|.*/items/.*|.*/itm/.*|.*/pages/detail.*|.*/PartDetail/.*|.*/prod/.*|.*/[Pp]roduct.*[Ss][Kk][Uu]=.*|.*/prodotto/.*|.*/Product|.*/product.*|.*/product/details.*|.*/product\-detail/.*|.*/product\-information/.*|.*/ProductDisplay/.*|.*/producto.*|.*/producto?/.*|.*/productos/.*|.*/Product-Page/.*|.*/products/detail.*|.*/Products/Detail/.*|.*/products/details/.*|.*/products/product\.asp\?ID=.*|.*/products\.php.*|.*/products_id/.*|.*/products_id/[0-9]+.*|.*/produit/.*|.*/produit/p[0-9]+/.*|.*/produit\-.*|.*/produits/.*|.*/produkt/.*|.*/produkt/[0-9]+/.*|.*productId\=.*|.*/shop/products/.*|.*/shopdetail/.*|.*/shopping/product/.*|.*\-(item|sku)\-.*|.*\/Details.*|.*\?itemid.*|.*\?itemId\=.*|.*\?pid=[0-9]+.*|.*\?prodId\=[0-9]+|.*\?product_id=.*|.*\?productid=[\d]+.*|.*\_[pP]roduct\.aspx\?id\=.*|.*artikelnummer=[0-9]+.*|.*GOODS_NO=.*|.*idproduct=.*|.*idProducto\=.*|.*itemcode.*|.*itemdetail\.do.*|.*ItemID=.*|.*proddetails\.aspx\?pid=.*|.*prodId=.*|.*ProdNr.*|.*Prodotti\.aspx.*|.*product\_detail.*|.*PRODUCT\_ID.*|.*product\_id\=.*|.*products_id=.*|.*produit.*|.*produits.*|.*produkt\-.*|.*produkt=.*|.*promoCode=.*|.*sku\_detail.*')
        df['product_pattern'] = ""
        bar = Bar('Validation Product URLS : ', max=len(df))
        for ind in df.index:
            if "pdf" in str(df['product_url'][ind]):
                df['product_pattern'][ind] = "No-Pattern"
            elif prod_reg.match(str(df['product_url'][ind])) is not None:
                df['product_pattern'][ind] = "Pattern"
            else:
                df['product_pattern'][ind] = "No-Pattern"
            bar.next()
        bar.finish()
        os.remove(patho.get() + ".txt")
        df.drop(df[df['product_pattern'] == 'No-Pattern'].index, inplace=True)
        df.drop('product_pattern', inplace=True, axis=1)
        df.to_excel(re.sub("_JSON_to_Excel.xlsx|_JSON_to_Excel|.xlsx", "", patho.get()) + "_JSON_to_Excel.xlsx", index=False)
        messagebox.showinfo('Alert', "Json file converted")


m.geometry('750x250')
m.resizable(False, False)
m.configure(background='ivory4')
img = tkinter.PhotoImage(data=img)
panel = tkinter.Label(m, image=img)
# panel.place(x=680, y=250)
panel.place(x=600, y=200)
button10 = tkinter.Button(m, text='Chose input file', bg='RoyalBlue2', fg='white', width=15, command=openme)
button10.place(x=30, y=15)
pathi = Entry(m, width=70)
pathi.place(x=160, y=15)

button13 = tkinter.Button(m, text='Chose JSON file', bg='RoyalBlue2', fg='white', width=15, command=jsonfile)
button13.place(x=30, y=50)
pathj = Entry(m, width=70)
pathj.place(x=160, y=50)

button14 = tkinter.Button(m, text='Choose JSON Output', bg='RoyalBlue2', fg='white', width=15, command=openref)
button14.place(x=30, y=85)
pathr = Entry(m, width=70)
pathr.place(x=160, y=85)

button12 = tkinter.Button(m, text='Save Output As', bg='RoyalBlue2', fg='white', width=15, command=saveme)
button12.place(x=30, y=120)
patho = Entry(m, width=70)
patho.place(x=160, y=120)

button20 = tkinter.Button(m, text='Data Parser', bg='RoyalBlue2', fg='white', width=18, command=parser)
button20.place(x=600, y=10)
button22 = tkinter.Button(m, text='Convert JSON', bg='RoyalBlue2', fg='white', width=18, command=Offline_search)
button22.place(x=600, y=80)
button23 = tkinter.Button(m, text='Compare Data', bg='RoyalBlue2', fg='white', width=18, command=compare)
button23.place(x=600, y=115)
button24 = tkinter.Button(m, text='Diff-BOT urls', bg='RoyalBlue2', fg='white', width=18, command=diff_bot)
button24.place(x=600, y=45)
button25 = tkinter.Button(m, text='Run Scrape', bg='RoyalBlue2', fg='white', width=18, command=scrape)
button25.place(x=600, y=150)
cred = Label(m, text="Copyright© A Product of SMT, Amazon India Pvt. Ltd. All Rights Reserved. ", font=("Arial", 10))
cred.place(x=100, y=230)
m.mainloop()
