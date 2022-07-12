# CSCI 355/655
# Summer 2022
# Assignment 3 - Scraping, HTML, and CSS
# Gabriel Rubio Alvarado

import os
import webbrowser
import requests
import html5lib
from bs4 import BeautifulSoup
import texttable as tt
import csv

from fileinput import filename

TAG_DOCTYPE = '<!DOCTYPE html>'
TAG_HTML = 'html'
TAG_HEAD = 'head'
TAG_BODY = 'body'
TAG_TABLE = 'table'
TAG_TH = 'th'
TAG_TD = 'td'
TAG_TR = 'tr'
TAG_PAR = 'p'
TAG_H1 = 'h1'  # HTML supports six default heading tags H1, H2, H3, H4, H5, and H6
TAG_BR = 'br'
TAG_LINK = 'link'


def write_file(file_name, message):
    f = open(file_name, 'w')
    f.write(message)
    f.close()

def create_element(tag, content,  attributes="", end_tag=True):
    element = "<" + tag + " " + attributes + ">"
    if end_tag:
        element += content + "</" + tag + ">"
    return element + "\n"


def create_elements(tag, list_contents):
    elements = ''
    for content in list_contents:
        elements += create_element(tag, content)
    return elements


def create_table(headers, data):
    rows = create_elements(TAG_TH, headers)
    for datum in data:
        tds = create_element(TAG_TD, datum)
        row = create_elements(TAG_TR, tds)
        rows += row
        table = create_element(TAG_TABLE, rows)
    return table


def open_file_in_browser(file_name):
    url = 'file:///' + os.getcwd() + '/' + file_name
    webbrowser.open_new_tab(url)


def main():

    open_file_in_browser("HelloWorld.html")
    head = create_element(TAG_HEAD, '')
    p = create_element(TAG_PAR, 'Hello Gabriel')
    body = create_element(TAG_BODY, p)
    message = TAG_DOCTYPE + create_element(TAG_HTML, head + body)
    # write_file("Gabriel.html", message)
    # open_file_in_browser("Gabriel.html")


    row0 = create_elements(TAG_TH, ['Firstname', 'Lastname', 'Age'])
    row1 = create_elements(TAG_TD, ['Jill', 'Smith', '50'])
    row2 = create_elements(TAG_TD, ['Eve', 'Jackson', '94'])
    rows = create_elements(TAG_TR, [row0, row1, row2])
    table = create_element(TAG_TABLE, rows)
    head = create_element(TAG_HEAD, '')
    heading = create_element(TAG_H1, "People and their ages")
    body = create_element(TAG_BODY, heading + table)
    message = create_element(TAG_HTML, head + body)
    write_file("People.html", message)
    open_file_in_browser("People.html")



    headers = ["State", "Abbreviation", "Capital"]
    data = [["Alaska", "AK", "Juneau"], "New York", "NY", "Albany"]
    table = create_table(headers, data)
    heading = create_element(TAG_H1, "United States")
    # head = create_element(TAG_HEAD, '')
    link_attributes = 'rel="stylesheet" href = "MyStyle.css"'
    link = create_element(TAG_LINK, "", link_attributes, end_tag=False)
    head = create_element(TAG_HEAD, link)
    body = create_element(TAG_BODY, heading + table)
    message = create_element(TAG_HTML, head + body)
    write_file("States.html", message)
    open_file_in_browser("States.html")


if __name__ == "__main__":
    main()
