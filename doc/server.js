var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql2');
var path = require('path');
var connection = mysql.createConnection({
                host: '35.184.94.222',
                user: 'root',
                password: 'password',
                database: 'projectdb'
});

connection.connect;


var app = express();

// set up ejs view engine 
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
 
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(__dirname + '../public'));

app.get('/', function(req, res) {
  res.send(`
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Fetch SQL Data</title>
  </head>
  <body>
      <h1>Welcome to the Data Fetching App</h1>
      <button onclick="fetchData()">Fetch Data</button>
      <pre id="results"></pre>
      
      <script>
          function fetchData() {
              fetch('/fetch-data')
                  .then(response => response.json())
                  .then(data => {
                      const results = document.getElementById('results');
                      results.textContent = JSON.stringify(data, null, 2);
                  })
                  .catch(error => {
                      console.error('Error fetching data:', error);
                      document.getElementById('results').textContent = 'Failed to fetch data.';
                  });
          }
      </script>
  </body>
  </html>
  `);
});

/* GET data for SQL query */
app.get('/fetch-data', function(req, res) {
  var sql = 'SELECT ingredients.ingredientName, AVG(pantry.quantity) as avgQuantity FROM pantry JOIN ingredients ON pantry.ingredientID = ingredients.ingredientID GROUP BY ingredients.ingredientID LIMIT 15;';
  connection.query(sql, function(err, results) {
      if (err) {
          console.error('Error fetching data:', err);
          res.status(500).send({ message: 'Error fetching data', error: err });
          return;
      }
      res.json(results);
  });
});




app.listen(80, function () {
    console.log('Node app is running on port 80');
});
