**Task 1**

I'm not gonna go through what HTTP means so let's just straight away go for the answers:

Answers:

What does HTTP stand for?
```
HyperText Transfer Protocol
```
What does the S in HTTPS stand for?
```
secure
```
On the mock webpage on the right there is an issue, once you've found it, click on it. What is the challenge flag?

just click the lock...

```
THM{INVALID_HTTP_CERT}
```

**Task 2**

nope, not going through this either

What HTTP protocol is being used in the above example?
```
HTTP/1.1
```
What response header tells the browser how much data to expect?
```
Content-Length
```

**Task 3**

**GET Request**

This is used for getting information from a web server.  

**POST Request**

This is used for submitting data to the web server and potentially creating new records  

**PUT Request**

This is used for submitting data to a web server to update information

**DELETE Request**  

This is used for deleting information/records from a web server.

Answers:

What method would be used to create a new user account?
```
POST
```
What method would be used to update your email address?
```
PUT
```
What method would be used to remove a picture you've uploaded to your account?
```
DELETE
```
What method would be used to view a news article?
```
GET
```

**Task 4**

**HTTP Status Codes:**

In the previous task, you learnt that when a HTTP server responds, the first line always contains a status code informing the client of the outcome of their request and also potentially how to handle it. These status codes can be broken down into 5 different ranges:

| **100-199 - Information Response** | These are sent to tell the client the first part of their request has been accepted and they should continue sending the rest of their request. These codes are no longer very common. |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **200-299 - Success**              | This range of status codes is used to tell the client their request was successful.                                                                                                    |
| **300-399 - Redirection**          | These are used to redirect the client's request to another resource. This can be either to a different webpage or a different website altogether.                                      |
| **400-499 - Client Errors**        | Used to inform the client that there was an error with their request.                                                                                                                  |
| **500-599 - Server Errors**        | This is reserved for errors happening on the server-side and usually indicate quite a major problem with the server handling the request.                                              |
**Common HTTP Status Codes:**  

| **200 - OK**                     | The request was completed successfully.                                                                                                                                                                                       |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **201 - Created**                | A resource has been created (for example a new user or new blog post).                                                                                                                                                        |
| **301 - Moved Permanently**      | This redirects the client's browser to a new webpage or tells search engines that the page has moved somewhere else and to look there instead.                                                                                |
| **302 - Found**                  | Similar to the above permanent redirect, but as the name suggests, this is only a temporary change and it may change again in the near future.                                                                                |
| **400 - Bad Request**            | This tells the browser that something was either wrong or missing in their request. This could sometimes be used if the web server resource that is being requested expected a certain parameter that the client didn't send. |
| **401 - Not Authorised**         | You are not currently allowed to view this resource until you have authorised with the web application, most commonly with a username and password.                                                                           |
| **403 - Forbidden**              | You do not have permission to view this resource whether you are logged in or not.                                                                                                                                            |
| **405 - Method Not Allowed**     | The resource does not allow this method request, for example, you send a GET request to the resource /create-account when it was expecting a POST request instead.                                                            |
| **404 - Page Not Found**         | The page/resource you requested does not exist.                                                                                                                                                                               |
| **500 - Internal Service Error** | The server has encountered some kind of error with your request that it doesn't know how to handle properly.                                                                                                                  |
| **503 - Service Unavailable**    | This server cannot handle your request as it's either overloaded or down for maintenance.                                                                                                                                     |
Answers:

What response code might you receive if you've created a new user or blog post article?
```
201
```
What response code might you receive if you've tried to access a page that doesn't exist?
```
404
```
What response code might you receive if the web server cannot access its database and the application crashes?
```
503
```
What response code might you receive if you try to edit your profile without logging in first?
```
401
```

**Task 5**

**Common Request Headers**

﻿These are headers that are sent from the client (usually your browser) to the server.  

**Host:** Some web servers host multiple websites so by providing the host headers you can tell it which one you require, otherwise you'll just receive the default website for the server.  

**User-Agent:** This is your browser software and version number, telling the web server your browser software helps it format the website properly for your browser and also some elements of HTML, JavaScript and CSS are only available in certain browsers.  

**Content-Length:** When sending data to a web server such as in a form, the content length tells the web server how much data to expect in the web request. This way the server can ensure it isn't missing any data.

**Accept-Encoding:** Tells the web server what types of compression methods the browser supports so the data can be made smaller for transmitting over the internet.

**Cookie:** Data sent to the server to help remember your information (see cookies task for more information).  

**Common Response Headers**

These are the headers that are returned to the client from the server after a request.

**Set-Cookie:** Information to store which gets sent back to the web server on each request (see cookies task for more information).  

**Cache-Control:** How long to store the content of the response in the browser's cache before it requests it again.  

**Content-Type:** This tells the client what type of data is being returned, i.e., HTML, CSS, JavaScript, Images, PDF, Video, etc. Using the content-type header the browser then knows how to process the data.  

**Content-Encoding:** What method has been used to compress the data to make it smaller when sending it over the internet.

Answers:

What header tells the web server what browser is being used?
```
User-Agent
```
What header tells the browser what type of data is being returned?
```
Content-Type
```
What header tells the web server which website is being requested?
```
Host
```

**Task 6**

Answers:

Which header is used to save cookies to your computer?
```
Set-Cookie
```

**Task 7**

Honestly everything here is pretty straight forward, so I won't go through.

Make a GET request to /room

![Output](Images/36.png)

Answers:

```
THM{YOU'RE_IN_THE_ROOM}
```

Make a GET request to /room

![Output](Images/37.png)
![Output](Images/38.png)

Answers:

```
THM{YOU_FOUND_THE_BLOG}
```

Make a DELETE request to /user/1

![Output](Images/39.png)

Answers:

```
THM{USER_IS_DELETED}
```

Make a PUT request to /user/2 with the username parameter set to admin

Answers:

```
THM{USER_HAS_UPDATED}
```

![Output](Images/40.png)
![Output](Images/41.png)

POST the username of thm and a password of letmein to /login
![Output](Images/43.png)
![Output](Images/44.png)

Answers:

```
THM{HTTP_REQUEST_MASTER}
```

