from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
def scrape():
    title = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
