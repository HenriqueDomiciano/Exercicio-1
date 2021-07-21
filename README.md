# Exercicio1
 Dashboard of cases, tests and vaccination of covid-19 made with vue.js 
## Introduction and how to run the API 
 
 First to run the API you should install the packages in requirements.txt

 
after that you run the API with py main.py (This project uses python 3 so if you have python 2 on your machine replace py with python3)
After we run the API make sure its running on the adress 'http://127.0.0.1:5000/'
 # Methods of the API

  * /General
    * GET:
        returns all the data in the database
    * POST:
    * args:
        --- table : can have 3 values : 'cases','vaccines','type_vaccines'
                option :
                    vaccines - needs an csv file with the vaccination data 
                    cases - needs an csv file with the cases data 
                    type_vaccines - needs an csv file with the types of vaccines per country 
        obs: Make sure your are using data taken from: 
        --'https://www.kaggle.com/hussainaliarif/largest-covid19-world-dataset'
        --'https://www.kaggle.com/gpreda/covid-world-vaccination-progress'
        or in the same pattern and headers so the site and the API can communicate properly. Be careful with this method because it can cause some main problems on the database because the data is replaced inside the database not appended
  * /Country
    * GET:
    *  args:
     --- name : Must be equals to the name of the country in english 
     --- ISO : Must be equal to the country Alpha3 ISO code 
     --- is_vaccines : Required and can have 2 values: 'cases' and 'vaccines' 

    after you make the request the API should return the data in json format of the solicited country. Remember don't use name and ISO together this can cause some trouble and only use one country at a time.
* /Date 
    * GET :
    * args : 
     -- date : you should send an date with the format YYYY-MM-DD

Remember that this API uses HTTP basic Authentication and that the username is admin and the password is suadmin if you want to use this in your local machine change in main.py the key dictionary second value to suadmin so you can use the API

# The vue.js dashboard :
Here is the heart of the website where everything is shown to the user 

* Main libraries used :
    * Chart.js
    * Axios 
    * moment

* Chart.js: was used to build the charts and the line plot 
* Axios : was used to make the request to the API
* moment: is used to format the date in the data.

The web application has a simple but effective layout maybe this is the part where it must be improved.

# How to run the website in your local machine.

First make sure to have npm installed on your machine and that you install the packages required running npm install.
Second go to the folder exercicio1 and type on the terminal:npm run serve
if everything is okay then you should get an ip adress to go to the website on your local network.

# Improvements that need to be done if the website goes live 
* Change the database from sqlite to another form such as PostgreSQL this maybe nedded when the site gets a hosting and thats why the post request in \General is of such importance 
* Second improve the CSS, thats a weakness of the website.
* Make it a little bit faster by getting the API call with only the data required not all the data of that Country.
* Use a JWT with an API key to improve security, this would also require building an login and user methods so that the JWT could be used and also be able to get the number of users and requests can be tracked.
* Build the capacity to have multiple countries in the charts and also to be able to add countries for better comparison.
