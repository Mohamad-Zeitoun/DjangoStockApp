from django.shortcuts import render
import yfinance as yf
import datetime
from .forms import StockForm
from .models import StockData
from django.http import JsonResponse
from datetime import  timedelta
import pandas 

# Create your views here.

def index(request):
    
    form = StockForm()

    return render(request, "stockapp/index.html", {"form": form})






def search(request):
    if request.method=="POST":
        
        ticker_symbol = request.POST.get("ticker_symbol")
        fromDate = request.POST.get("fromDate")
        toDate=request.POST.get("toDate")
        

        try:

            StockData.objects.all().delete()

             # Convert string dates to  datetime objects
            start_date = datetime.datetime.strptime(fromDate, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(toDate, "%Y-%m-%d")

            # Fetch stock data using yfinance
            stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
            
            

            
            
             # Convert DataFrame to list of dictionaries for bulk insertion
            stock_data_list = stock_data.to_dict('records')
            
            # Create StockData objects from each dictionary
            stock_objects = []
            day = 0
            for row in stock_data_list:
                
                
                stock_object = StockData(
                    ticker_symbol=ticker_symbol,
                    date=stock_data.index[day],  # Assuming 'Date' is the date column name
                    open_price=row[('Open',ticker_symbol)],
                    close_price=row[('Close',ticker_symbol)],
                )
                day = day +1 
                stock_objects.append(stock_object)
                
            
            # Bulk insert StockData objects
            StockData.objects.bulk_create(stock_objects) 
            
            # Print the open and close prices
            
            tickerData =  StockData.objects.all()
            
            context = list(tickerData.values())  # Convert to a list of dictionaries
       
            
            return JsonResponse(context,safe=False)
        except:
                
            return JsonResponse({"status": "Error"})
    

