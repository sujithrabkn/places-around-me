# Places Around Me
## AIM:
To develop a website to display details about the places around my house.

## Design Steps:

### Step 1:
Clone the places-around-me repository into the folder named 'EX04'.Perform the necessary changes in settings.py.
### Step 2:
Create a folder named 'static' in which a folder named 'html' has to be created and under which all the required html files are to be included.
### Step 3:
Code the main html program for the website and link all the other 5 html codes created regarding the places description.
### Step 4:
Edit the readme.md file and push the files to the GitHub to display the contents for the same.

## Code:

### In map.html:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My City</title>
    </head>
    <body>
        <h1 align="center">
            <font colour="red"><b>Thiruvallur</b></font>
        </h1>
        <h3 align="center">
            <font colour="blue"><b>Sujithra B K N(22008582)</b></font>
        </h3>
        <center>
            <img src="/static/images/map.png" usemap="#MyCity" height="920" width="1323">
            <map name="MyCity">
            <area shape="rectangle" coords="287,194,337,244" href="/static/html/place1.html" title="School">
            <area shape="rectangle" coords="504,567,554,617" href="/static/html/place2.html" title="Cake fest">
            <area shape="rectangle" coords="665,563,715,613" href="/static/html/place3.html" title="Park">
            <area shape="rectangle" coords="161,778,211,828" href="/static/html/place4.html" title="restaurant">
            <area shape="rectangle" coords="1106,627,1156,677" href="/static/html/place5.html" title="temple">
        </center>
    </body>
</html>
```
### In place1.html:
```
<!DOCTYPE html>
<html lang="en">
<head>
<title>School</title>
</head>
<body bgcolor="yellow">
<h1 align="center">
<font color="red"><b>Thiruvallur</b></font>
</h1>
<h3 align="center">
<font color="blue"><b>Shree Niketan School</b></font>
</h3>
<hr size="3" color="red">
<p align="justify">
<font face="Tahoma" size="5">
Shree Niketan realizes the importance of the holistic development of the students. Emphasis is laid on shaping students into smart individuals with strong commitment to their chosen goals. Individual sports like, Archery, Skating, Tennis are a part of physical education for all age groups, aimed at grooming the students on self-confidence, fitness and skill sets under the expert guidance of the professional trainers.
The School has plans to build synthetic Tennis Courts for students eager to train in this elite sport. Quality training is also provided in athletics, track and field events in the vast playground of the school. Similarly, a skating rink is to be designed for students to train in roller-skating. Shree Niketan does not miss a chance to make schooling for the students memorable in their lifetime.
At Shree Niketan, students are taught to love and respect nature. Tree planting, rainwater harvesting, organic farming and so on are not only taught but students are encouraged to implement these activities in their neighbourhood.
Shree Niketan practices what it preaches. Students are also taken to nearby hamlets as a part of community service. Patriotism is also inculcated in the students of the school by providing NCC training that forms the fourth line of defense. Inculcating such habits right from the impressionable age help them grow with an understanding of their role and responsibility towards the society they live in.
</font>
</p>
</body>
</html>
```
### In place2.html:
```
<!DOCTYPE html>
<html lang="en">
<head>
<title>cake fest</title>
</head>
<body bgcolor="pink">
<h1 align="center">
<font color="red"><b>Thiruvallur</b></font>
</h1>
<h3 align="center">
<font color="blue"><b>cake fest</b></font>
</h3>
<hr size="3" color="red">
<p align="justify">
<font face="Arial" size="5">
<b>
It is located in thiruvallur.
Can celebrate your happiness with their tasty and yummy cakes.
Fest of cakes.
</b>
</font>
</p>
</body>
</html>
```
### In place3.html:
```
<!DOCTYPE html>
<html lang="en">
<head>
<title>Park</title>
</head>
<body bgcolor="yellow">
<h1 align="center">
<font color="red"><b>Thiruvallur</b></font>
</h1>
<h3 align="center">
<font color="blue"><b>Park</b></font>
</h3>
<hr size="3" color="red">
<p align="justify">
<font face="Tahoma" size="5">
A park is an area of natural, semi-natural or planted space set aside for human enjoyment and recreation or for the protection of wildlife or natural habitats. Urban parks are green spaces set aside for recreation inside towns and cities. National parks and country parks are green spaces used for recreation in the countryside. State parks and provincial parks are administered by sub-national government states and agencies. Parks may consist of grassy areas, rocks, soil and trees, but may also contain buildings and other artifacts such as monuments, fountains or playground structures. Many parks have fields for playing sports such as baseball and football, and paved areas for games such as basketball. Many parks have trails for walking, biking and other activities. Some parks are built adjacent to bodies of water or watercourses and may comprise a beach or boat dock area. Urban parks often have benches for sitting and may contain picnic tables and barbecue grills. 
</font>
</p>
</body>
</html>

### In place4.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Restaurant</title>
</head>
<body bgcolor="yellow">
<h1 align="center">
<font color="red"><b>Thiruvallur</b></font>
</h1>
<h3 align="center">
<font color="blue"><b>AK Garden</b></font>
</h3>
<hr size="3" color="red">
<p align="justify">
<font face="Tahoma" size="5">
Restaurant is completely filled natural plants with impeccable ambience to give pleasure to our customers and kids who can really enjoy your leisure & valuable time. They are trying to give best in class, quality, quantity, value of your money.
</font>
</p>
</body>
</html>
```
### In place5.html:
```
<!DOCTYPE html>
<html lang="en">
<head>
<title>Temple</title>
</head>
<body bgcolor="yellow">
<h1 align="center">
<font color="red"><b>Thiruvallur</b></font>
</h1>
<h3 align="center">
<font color="blue"><b>Saibaba Temple</b></font>
</h3>
<hr size="3" color="red">
<p align="justify">
<font face="Tahoma" size="5">
Vishwaroopa Sai Baba Temple, Tiruvallur is situated at Tiruvallur in India. 
It is located at No 1, Velavan Street, Valasaravakkam, Thiruvallur district,
Tamilnadu Pincode of Vishwaroopa Sai Baba Temple, Tiruvallur is 600087 in India</font>
</p>
</body>
</html>
```
## Output:

### Map:
![41](https://user-images.githubusercontent.com/119477857/215445574-517f20e1-a0ad-483a-9aa6-519e8eb46950.jpg)

### place:

![42](https://user-images.githubusercontent.com/119477857/215445608-b6524c85-7408-49ab-8b8e-98f696542672.jpg)

### html validator:
![out6](https://user-images.githubusercontent.com/119477857/215445163-47999d31-eab5-4acb-9482-9dd2295bc721.jpg)

## Result:
Image mapping website created and executed successfully.
