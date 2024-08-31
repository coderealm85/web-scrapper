import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Function to scrape the website
def scrape_website(url):
    # Use Selenium to handle dynamic content
    driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
    driver.get(url)
    time.sleep(3)  # Allow some time for the page to load

    # Use BeautifulSoup for HTML parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Example: Extract product names and prices
    products = []
    for item in soup.find_all('div', class_='product-card'):  # Replace with actual HTML class or tag
        product_name = item.find('h2', class_='product-name').text.strip()  # Replace with actual HTML class or tag
        product_price = item.find('span', class_='product-price').text.strip()  # Replace with actual HTML class or tag
        products.append({'Product Name': product_name, 'Price': product_price})
    
    return products

# Function to start scraping and display data in the text box
def start_scraping():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        scraped_data = scrape_website(url)
        display_data(scraped_data)  # Display data in text box
        messagebox.showinfo("Success", "Data scraped and displayed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display scraped data in the text box
def display_data(data):
    # Clear the previous content
    result_text.delete(1.0, tk.END)
    
    # Format and display data
    for item in data:
        result_text.insert(tk.END, f"Product Name: {item['Product Name']}\n")
        result_text.insert(tk.END, f"Price: {item['Price']}\n")
        result_text.insert(tk.END, "-"*40 + "\n")  # Separator for clarity

# Setting up the main GUI window
root = tk.Tk()
root.title("Web Scraper Tool")

# URL input field
tk.Label(root, text="Enter the URL to scrape:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Start scraping button
tk.Button(root, text="Start Scraping", command=start_scraping).pack(pady=20)

# Text box to display results
result_text = scrolledtext.ScrolledText(root, width=70, height=20)
result_text.pack(pady=10)

root.mainloop()
