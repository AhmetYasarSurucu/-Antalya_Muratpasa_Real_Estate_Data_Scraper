# 🏡 Antalya Muratpaşa Real Estate Data Scraper

This project is a **Python-based web scraping tool** that collects real estate listing data for the **Muratpaşa district of Antalya, Turkey**. It enables the user to gather structured property data for further analysis, visualization, or machine learning applications.

## 🔍 Purpose

The goal of this project is to provide a dataset of current real estate listings — including price, location, room count, square meter, and more — from popular Turkish property platforms. This enables:

- **Market analysis** for real estate professionals and investors  
- **Data-driven decision making** for potential buyers or renters  
- **Foundational datasets** for machine learning projects

## ⚙️ Features

- Scrapes property listings for **Antalya / Muratpaşa** from a real estate website  
- Extracts detailed information such as:
  - Title
  - Price
  - Room count
  - Area (m²)
  - Location details (neighborhood, street)
  - Listing date
- Outputs the data as a **clean and structured CSV file**

## 🛠️ Technologies Used

- **Python**
- **BeautifulSoup** – for parsing HTML  
- **Requests** – for making HTTP calls  
- **Pandas** – for data structuring and exporting  

## 📁 Output

The script creates a CSV file containing real estate data with the following columns:

- `Title`
- `Price`
- `SquareMeters`
- `RoomCount`
- `Neighborhood`
- `DatePosted`
- `Link`

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmetYasarSurucu/-Antalya_Muratpasa_Real_Estate_Data_Scraper.git
   cd Antalya_Muratpasa_Real_Estate_Data_Scraper
