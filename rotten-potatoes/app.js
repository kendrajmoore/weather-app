const express = require('express');
const app = express();
const methodOverride = require('method-override');
const bodyParser = require('body-parser');


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


const Review = mongoose.model('Review', {
  title: String,
  description: String,
  movieTitle: String
});

app.get('/', (req, res) => {
  Review.find().then((reviews) => {
    res.render('reviews-index', {reviews: reviews});
  }).catch((err) => {
    console.log(err);
  })
})

app.post('/reviews', (req, res) => {
  Review.create(req.body).then((review) => {
    console.log(review)
    res.redirect('/reviews/' + review._id) // Redirect to reviews/:id
  }).catch((err) => {
    console.log(err.message)
  })
})

app.get('/reviews/:id', (req, res) => {
  Review.findById(req.params.id).then((review) => {
    res.render('reviews-show', { review: review })
  }).catch((err) => {
    console.log(err.message);
  })
})

app.get('/reviews/:id/edit', function (req, res) {
  Review.findById(req.params.id, function(err, review) {
    res.render('reviews-edit', {review: review});
  })
})

app.put('/reviews/:id', (req, res) => {
  Review.findByIdAndUpdate(req.params.id, req.body).then((review) => {
    res.redirect('/reviews/' + review._id)
  }).catch((err) => {
    console.log(err.message)
  })
})
//app.get('/reviews', (req, res) => {
  //res.render('reviews-index', { reviews: reviews });
//})

app.listen(3000, () => {
  console.log('App listening on port 3000!')
})
