const express     = require('express');
const app         = express();
const bodyParser  = require('body-parser');
const mongoose    = require('mongoose');

mongoose.Promise = global.Promise
mongoose.connect('mongodb://localhost/yelp-clone');
mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection Error:'))
mongoose.set('debug', true)

app.use(bodyParser.urlencoded({extended: true}));

// app.js
app.set('view engine', 'ejs')

require('./controllers/campgrounds')(app);

app.listen(3000, () => {
  console.log('App listening on port 3000!')
});
