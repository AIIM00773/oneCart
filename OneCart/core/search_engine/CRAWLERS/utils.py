
import os
import sys

# ensure project root is on sys.path 
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# set Django settings 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OneCart.settings")

import django
django.setup()

# now imports will work
from data_pipeline.models import Markets, Categories, Brands, Items, Countries

import json, glob
from data_pipeline.models import Items, Brands, Categories  # Ensure these are properly imported

all_files = []



# Load JSON files
with open("anisuma.json", "r") as FL1:
    all_files.append(json.load(FL1))


with open("phoneplacekenya.json", "r") as FL2:
    all_files.append(json.load(FL2))


with open("markets.json", "r") as FL3:
    FL3 = json.load(FL3) 
    print (FL3)

# Loop through each record in the list
for record_ in FL3:

    Name = record_.get("Name")
    Description = record_.get("Description")
    Country = record_.get("Country")
    Link = record_.get("Link")

        
    # Check if itembrand_ exists and create if it doesn't exist
    if Name and Description and  Country and Link :
        
        existingMarkets = Markets.objects.filter(market_name=Name , market_link = Link, market_description =Description, market_country=Country)
            
        if not existingMarkets.exists():
            Markets.objects.create(market_name=Name , market_link = Link, market_description =Description, market_country=Country) 
            print(f"Market place : {Name}")
    else:
        continue 
            
            
            
  
  
  
with open("countries.json", "r") as FL4:
    FL4 = json.load(FL4) 
    print (FL4)


# Loop through each record in the list
for record_ in FL4:

    Name = record_.get("country_name")
    Code = record_.get("country_code")
    Short = record_.get("country_short")


    # Check if itembrand_ exists and create if it doesn't exist
    if Name and Code and  Short :
        
        ExixtingCountry = Countries.objects.filter(country_name=Name , country_code = Code, country_short =Short )
            
        if not ExixtingCountry.exists():
            Countries.objects.create(country_name=Name,country_code = Code, country_short =Short ) 
            print(f"Country Name : {Name}")
    else:
        continue 
            
  
  
  
              

# Debugging output
print(f"Number of Lists: {len(all_files)}")
print("_________________")

# Loop through each file
for file_ in all_files:
    print(f"Length of Individual List: {len(file_)}")
    print("********")

    # Loop through each record in the list
    for record_ in file_:
        itemname_ = record_.get("product_Name")
        itembrand_ = record_.get("product_Brand")
        itemcategory_ = record_.get("product_Category")
        itemsource_ = record_.get("product_Source_URL")
        itemllink_ = record_.get("product_Link")
        itemimagesouce_ = record_.get("product_Image_Link")
        
        
        
        
        


        # Check if itembrand_ exists and create if it doesn't exist
        if itembrand_:
            try:
                existingBrand = Brands.objects.get(brand_name=itembrand_)
            except Brands.DoesNotExist:
                Brands.objects.create(brand_name=itembrand_) 
                print(f"Created new Brand: {itembrand_}")
        else:
            continue 
            
            
            
                    
        
        # Check if itembrand_ exists and create if it doesn't exist
        if itembrand_:
            try:
                existingBrand = Brands.objects.get(brand_name=itembrand_)
            except Brands.DoesNotExist:
                Brands.objects.create(brand_name=itembrand_) 
                print(f"Created new Brand: {itembrand_}")
        else:
            continue 



        # Check if itemcategory_ exists and create if it doesn't exist
        if itemcategory_:
            category_in_list = itemcategory_.strip().split(",")
            
            for category_token in category_in_list:
                try:
                    existingCategory = Categories.objects.get(category_name=category_token)
                except Categories.DoesNotExist:
                    Categories.objects.create(category_name=category_token) 
                    print(f"Created new Category: {category_token}")
        else:
            continue 
            
            
            
            

        # Check if all required fields are available before creating the record
        if itemname_ and itembrand_ and itemcategory_ and itemsource_ and itemllink_ and itemimagesouce_:
            
            # Check if the item already exists in the database
            existing_item = Items.objects.filter(
                item_name=itemname_,
                item_image_link=itemimagesouce_,
                item_brand=itembrand_,
                item_category=itemcategory_,
                item_origin=itemsource_,
                item_link=itemllink_
            )
            
            # If the item doesn't exist, create it
            if not existing_item.exists():
                Items.objects.create(
                    item_name=itemname_,
                    item_image_link=itemimagesouce_,
                    item_brand=itembrand_,
                    item_description=None,  # None, or an empty string "" if you prefer
                    item_category=itemcategory_,
                    item_origin=itemsource_,  # Make sure this field exists in your model
                    item_link=itemllink_
                )
                print(f"Created new Item Record: {itemname_}")
            else:
                print(f"Item {itemname_} already exists in the database.")
        else:
            print(f"Skipping record due to missing data: {record_}")

# Optionally print out all item names after processing
print("Item Names:")
items = Items.objects.all()
for item in items:
    print(item.item_name)





