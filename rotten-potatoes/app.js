const express        = require('express');
const app            = express();
const methodOverride = require('method-override');
const bodyParser     = require('body-parser');


app.use(methodOverride('_method'));
app.use(bodyParser.urlencoded({ extended: true }));



// app.js
const exphbs = require('express-handlebars');

const mongoose = require('mongoose');
mongoose.Promise = global.Promise
mongoose.connect('mongodb://localhost/rotten-potatoes');
mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection Error:'))
mongoose.set('debug', true)

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');


app.listen(3000, () => {
  console.log('App listening on port 3000!')
})
