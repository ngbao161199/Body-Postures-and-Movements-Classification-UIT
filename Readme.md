# Classification-of-Body-Postures-and-Movements-UIT
- Class: CS313.K11.KHCL
- Lecturer: Ms. Nguyễn Thị Anh Thư

## Group 4:
<ul>
    <li> Nguyễn Ôn Ngọc Bảo - @ngbao161199
    <li> Trần Việt Hùng - @bittervirgin
    <li> Nguyễn Tấn Phát - @Mercersi
</ul>

![](https://camo.githubusercontent.com/65858ba290493d538f380d452b846488c221b17e/68747470733a2f2f692e696d6775722e636f6d2f69356a306868432e706e673f31)

## Requirements packages for project:
- Flask==1.0.2
- numpy==1.16.4
- matplotlib==3.0.3
- pandas==0.24.2
- scikit_learn==0.21.3

## Dataset we use:
- PUC-Rio Data Set
- Website: http://archive.ics.uci.edu/ml/datasets/Wearable+Computing%3A+Classification+of+Body+Postures+and+Movements+%28PUC-Rio%29

## How to run web application of this project (created by Flask)

- Clone this git project, cd to project directory. Use this command ``python main-api.py`` 
- Go to this link: http://127.0.0.1:5000/ or http://localhost:5000/

![](https://i.imgur.com/8WCYlDD.png?1)

### Progress of Flask app
- [X] Build Home landing Page **(home.html)**
    - [X] On home landing page have slide image
    - [X] On home landing page have chossing box for us to choose algorihm  and Submit button
    - [X] With Submit button, we need it to redirrect to another page to show accuracy, MSE, cofusion_matrix,... of model in JSON format.

![](https://camo.githubusercontent.com/65858ba290493d538f380d452b846488c221b17e/68747470733a2f2f692e696d6775722e636f6d2f69356a306868432e706e673f31)

- [X] Build About landing Page **(about.html)**
    - [X] Showing basic information about this project, lecturer and team member.
    - [X] Decorate this page

![](https://i.imgur.com/X4L7JnI.png?1)

- [X] Build Data Visualization landing Page **(data.html)**
    - [X] Showing process of our team when process and modify the data (Generated directly from Jupyter Notebook).
    
 ![](https://i.imgur.com/tmvl3T8.png?1)
    
- [X] Build Test Algorithm (Manual) Page **(algo.html)**
    - [X] A site for user input attribute manually and choose algorithms.
    - [X] With Submit button, the site will return class result predicted by algorihms.

![](https://i.imgur.com/GyV2TN5.png?1)
 
- [X] Build Test Algorithm (Multiple) Page **(algo_with_file.html)**    
    - [X] Users given number of data will be used and choose algorithms.
    - [X] With Submit button, the site will return accuracy in JSON format after training by algorihms.

![](https://i.imgur.com/urdkYxk.png?1)

- [X] Build Contact landing Page **(contact.html)**
    - [X] Create a form for anyone to fill to connect with our team member.

![](https://i.imgur.com/IAEBZuo.png?1)
