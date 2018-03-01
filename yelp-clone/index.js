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

app.get('/campgrounds', function(req, res){
    var campgrounds = [
      {name: 'Salmon Creek'}
      {name: 'Granite Hill'}
      {name: 'Mountain Goat Rest'}
      {name: 'Budget Camp'}
    ]
    res.render('campgrounds');
});

app.listen(3000, () => {
  console.log('App listening on port 3000!')
})
