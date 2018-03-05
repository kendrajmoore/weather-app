const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: true}));

// app.js
app.set('view engine', 'ejs')

var campgrounds = [
  {name: 'Salmon Creek', image: 'https://unsplash.com/photos/h4bBVo_CpqQ' },
  {name:  'Goat', image: 'https://unsplash.com/photos/ZuZK8D55_cw'},
  {name:  'Boat', image: 'https://unsplash.com/photos/aCVIH_FuyjY'}
]

app.get('/', (req, res) => {
  res.render('landing');
});

app.get('/campgrounds', (req,res) => {
     res.render('campgrounds', { campgrounds: campgrounds});
});

app.post('/campgrounds', (req, res) => {
  var name = req.body.name;
  var newCampground = { name: name };
  campgrounds.push(newCampground);
  res.redirect('/campgrounds')
})

app.get('/campgrounds/new', (req, res) => {
  res.render('new.ejs');
})

app.listen(3000, () => {
  console.log('App listening on port 3000!')
});
