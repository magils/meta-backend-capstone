# Meta Backend Capstone Project

## Endpoints

### Menu Items

**Get/Create Menu Items**

**Methods: GET/POST**

`http://localhost:8000/restaurant/menu-items`


**Single Menu Items**

**Methods: GET/PUT/DELETE**

`http://localhost:8000/restaurant/menu-items/<int:pk>`


**Create/Update Menu Item Payload**
```
{
    "title": "Test Menu Item 3",
    "price": 54.32,
    "inventory": 321
}
```


### Booking

**Get/Create Bookings**

**Methods: GET/POST**

`localhost:8000/restaurant/booking/table`


**Single Menu Items**

**Methods: GET/PUT/DELETE**

`localhost:8000/restaurant/booking/table/<int:pk>`


**Create/Update Menu Item Payload**
```
{
    "name": "Test booking 2",
    "no_of_guest": 6,
    "booking_date": "2023-11-04T07:08:00Z"
}
```

### Database Config

```
    NAME: LittleLemon,
    USER: littlelemon,
    PASSWORD: littlelemon@123,
    HOST: 127.0.0.1,
    PORT: 3307
```

### Database Docker Compose 

Run this command in the root folder:

```
    docker-compose up -d
```

### Run App

```
    python manage.py runserver
```