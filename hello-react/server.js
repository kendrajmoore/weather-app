const express = require('express');

//Create our app

const app = express();
app.use(express.static('public'));

app.listen(3000, function () {
  console.log('React app on port 3000');
});
