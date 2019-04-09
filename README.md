This is the project repo for Huifang Wang. Here are some instructions on running the script and the approach of the solution. 

1. My bash script run.sh use python3 to run python as follows: 
   $ python3 ./src/Purchase.py
   If the test system use different name, please change to the right name. Then compile it and run:
   $ chmod +x run.sh
   $ ./run.sh

2. The python script Purchase.py currently reads order_products__train.csv dataset, which has been renamed as order_products.csv.
   In my own test folder: under the insight_testsuite/testsmyowntest/, the Purchase.py script reads the simple test dataset provided by insightDataScience.

3. In my Purchase.py script, I search through each product from order_products list and find the department that the product belongs to from product list. Then I calculate the total number of products for each department. Based on 'reordered' flag I could calculate the total number of the first time ordered products. The percentage is calculated by dividing number of the first time orders over total number of orders. 
