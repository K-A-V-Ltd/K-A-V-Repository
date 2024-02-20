 [![temp-Imagemgp-J5-I.avif](https://i.postimg.cc/3J7zrZCg/temp-Imagemgp-J5-I.avif)](https://postimg.cc/kD1TfKH4)


# Description 

**K\*A*V** is a logistics console application designed to be used by employees of a large Australian company aiming to expand its activities to the freight industry. 
The app helps manage the delivery of packages between hubs in major Australian cities. 
An employee can record the details of a delivery package, create and search for suitable delivery routes,
and inspect the current state of delivery packages, transport vehicles and delivery routes. 

# Usage
The application supports 9 commands: `RegisterPackage`, `CreateRoute`, `SearchRoute`, `AssignTruck`, `AssignPackage`, `ViewPackageInfo`, `ViewActiveRoutes`, `ViewUnassignedPackages` and `BulkAssign`
\
##  1. RegisterPackage command
\
This command allows an employee to record the information of a package and its sender, effectively registering it in the system. It accepts 7 parameters: `start location` `end location` `weight` `first name` `last name` `phone` `email`\
\
`start location`: should be one of the following: Sydney, Melbourne, Adelaide, AliceSprings, Brisbane, Darwin or Perth\
\
`end location`: should be one of the following: Sydney, Melbourne, Adelaide, AliceSprings, Brisbane, Darwin or Perth\
\
`weight`: should be above 0.5 kg\
\
`first name`: should be between 2 and 10 characters long\
\
`last name`: should be between 2 and 10 charactes long\
\
`phone`: should be 10 digits\
\
`email`: should include **@gmail.com** or **@yahoo.com**


**Example** 

```
registerPackage Sydney Brisbane 23.2 David Wilson 0478963214 david.wilson@gmail.com`
```

**Output**

```
Package #1 successfully registered.
```

## 2. CreateRoute command
\
This command lets an employee create a new route. It requires a minimum of 5 parameters: `month` `day` `time` `location` `location` (a minimum of two locations).
\
`location`: should be one of the following: Sydney, Melbourne, Adelaide, AliceSprings, Brisbane, Darwin or Perth\


**Example** 

```
createRoute Mar 11 12:30 Sydney Brisbane Adelaide Perth
```


**Output**

```
Route #1 created.
```



## 3. SearchRoute command
\
This command allows a user to search for a suitable route for a package that includes two specific locations in a particular order. 
It accepts 2 parameters: `location` `location`.

**Example**

```
SearchRoute Brisbane Perth
```

**Output** 
```
Route ID: 1
Sydney (Mar 11 12:30) -> Brisbane (Mar 11 22:56) -> Adelaide (Mar 12 21:05) -> Perth (Mar 14 05:06)
```

## 4. AssignTruck command
\
This command allows an employee to automatically assign a truck to a particular route based on capacity, range and time availability.
It accepts 1 parameter: `route ID`

**Example**

```
AssignTruck 1
```

**Output**

```
Truck #1001 successfully assigned to route #1
```

## 5. AssignPackage command
\
This command lets an employee assign a package to a particular route. 
It accepts 2 parameters: `package ID` `route ID`

**Example** and **Output**

```
registerPackage Brisbane Perth 19.7 James Taylor 0489753102 james.taylor@gmail.com
Package #2 successfully registered.
AssignPackage 2 1
Package #2 successfully assigned to route #1.
```

## 6. ViewPackageInfo 
\
This command allows an employee to get detailed information about a particular package. 
It requires a `package ID`.

**Example**

```
ViewPackageInfo 2
```

**Output**

```
ID: 2
Weight: 19.7
Destination: Perth
ETA: Mar 14 05:06
Status: on its way
-----contact info-----
Name: James Taylor
Phone: 0489753102
E-mail: james.taylor@gmail.com
```

**Note** 

The status of a package will be either `not assigned yet`, `on its way` or `delivered on date/time`, depending on whether the package is assigned and depending on the progress of the route. 


## 7. ViewUnassignedPackages
\
This command allows an employee to take a look at all packages that are yet to be assigned.

**Example**

```
registerPackage Adelaide Brisbane 13.4 Ethan Jackson 0432109876 ethan.jackson@gmail.com
Package #1 successfully registered.
registerPackage AliceSprings Perth 29.2 Mia Thomas 0467890123 mia.thomas@gmail.com
Package #2 successfully registered.
registerPackage Brisbane Darwin 13.5 Sophia Martinez 0423568970 sophia.martinez@gmail.com
Package #3 successfully registered.
ViewUnassignedPackages
```

**Output**

```
ID: 1 Location: Adelaide
ID: 2 Location: Alicesprings
ID: 3 Location: Brisbane
```

## 8. BulkAssign
\
This command allows an employee to assign multiple packages to one route. 
It accepts a minmum of 3 parameters: `route ID` and a minimum of 2 `package ID`s. 

**Example**

```
BulkAssign 1 2 3 5 4 7 8 6 9 11
```

**Output**

```
8 packages successfully assigned to route #1: 2, 3, 5, 4, 7, 8, 6, 9
The following packages were not found: 11.
```

**Note:** The console returns a confirmation of which packages were assigned and indicates if there was a problem retrieving a package. 


## 9. ViewActiveRoutes 
\
This command allows a supervisor to take a look at all the routes currently in progress, displaying their stops, delivery weight and the expected next stop. 

**Example** and **Ouput**

```
ViewActiveRoutes
Route ID: 1
Brisbane (Mar 14 14:30) -> Perth (Mar 16 16:03) -> Sydney (Mar 18 14:12)
Delivery Weight: 523.5 
Next Stop: Perth             
```
