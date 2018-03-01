const express = require('express')
const app = express()

// app.js
const exphbs = require('express-handlebars');

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');


//server
app.get('/', (req, res) => {
  res.render('home.handlebars')
})

app.listen(3000, () => {
  console.log('App listening on port 3000!')
})
