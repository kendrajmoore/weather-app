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

const campgroundSchema = new mongoose.Schema({
  name: String,
  image: String
});

let Campground = mongoose.model('Campground', campgroundSchema);

let campgrounds = [
  {name: 'Salmon Creek', image: 'https://res.cloudinary.com/simpleview/image/fetch/c_fill,f_auto,h_452,q_75,w_982/http://res.cloudinary.com/simpleview/image/upload/v1469218578/clients/lanecounty/constitution_grove_campground_by_natalie_inouye_417476ef-05c3-464d-99bd-032bb0ee0bd5.png' },
  {name:  'Goat', image: 'https://www.reserveamerica.com/webphotos/NH/pid270015/0/540x360.jpg'},
  {name:  'Boat', image: 'https://i.pinimg.com/originals/ab/5e/c4/ab5ec4ff722b1f65b855af71ba78c6fc.jpg'}
]

app.get('/', (req, res) => {
  res.render('landing');
});

app.get('/campgrounds', (req,res) => {
     res.render('campgrounds', { campgrounds: campgrounds});
});

app.post('/campgrounds', (req, res) => {
  var name = req.body.name;
  var image = req.body.image;
  var newCampground = { name: name, image: image };
  campgrounds.push(newCampground);
  res.redirect('/campgrounds')
})

app.get('/campgrounds/new', (req, res) => {
  res.render('new.ejs');
})

app.listen(3000, () => {
  console.log('App listening on port 3000!')
});
