**Fetch score**
----
  Returns scores for current users previous games in speciefied map in JSON.

* **URL**

  /scores/:mapId

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `mapId=[integer]`
   
   **Optional:**
    
    None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 OK <br/>
    **Content:**    
```json  
[
    {
        "gameId": "1",
        "timestamp": "2013-01-16T08:16:59.844Z",
        "score": "32",
    },
    {
        "gameId": "2",
        "timestamp": "2013-01-16T08:17:59.844Z",
        "score": "132",
    },
    {
        "gameId": "3",
        "timestamp": "2013-01-18T08:16:59.844Z",
        "score": "1322",
    }
]
```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br/>
    **Content:** `{ "message" : "No scores found for the user." }`

  OR

  * **Code:** 405 METHOD NOT ALLOWED <br/>
    **Content:** `{ "message" : "This resource only supports GET and POST methods." }`

  OR
  
  * **Code:** 401 UNAUTHORIZED <br/>
    **Content:** `{ "message" : "You must be logged in to access scores." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/scores/2",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**Add score**
----
  Add new score to database.

* **URL**

  /scores/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   None
   
   **Optional:**
    
    None

* **Data Params**

```json
    {
        "mapId" : [integer],
        "score" : [integer]
    } 
```

* **Success Response:**

  * **Code:** 200 OK <br/>
    **Content:** `{ "message" : New score added successfully.}`

 
* **Error Response:**

    * **Code:** 400 BAD REQUEST <br/>
    **Content:** `{ "message" : "Malformed syntax in request POST" }`

  OR
  * **Code:** 405 METHOD NOT ALLOWED <br/>
    **Content:** `{ "message" : "This resource only supports GET and POST methods." }`

  OR
  
  * **Code:** 401 UNAUTHORIZED <br/>
    **Content:** `{ "message" : "You must be logged in to access scores." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/scores/",
      dataType: "json",
      type : "POST",
      data : {
        "mapId" : "3",
        "score" : "421"
      },
      success : function(r) {
        console.log(r);
      }
    });
  ```

