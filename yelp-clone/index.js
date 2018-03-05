const express = require('express');
const app = express();

// app.js
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
  res.render('landing');
});

app.get('/campgrounds', (req,res) => {

    var campgrounds = [
      {name: 'Salmon Creek', image: 'https://unsplash.com/photos/h4bBVo_CpqQ' },
      {name:  'Goat', image: 'https://unsplash.com/photos/ZuZK8D55_cw'},
      {name:  'Boat', image: 'https://unsplash.com/photos/aCVIH_FuyjY'}
    ]
     res.render('campgrounds', {campgrounds: campgrounds});
});

app.listen(3000, () => {
  console.log('App listening on port 3000!')
});
