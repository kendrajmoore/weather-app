const Campground = require('../models/campground.js');

module.exports = (app) => {
//INDEX
  app.get('/', (req, res) => {
   Campground.find().then((campgrounds) => {
    res.render('landing', { campgrounds: campgrounds });
  }).catch((err) => {
    console.log(err);
  })
})


//CREATE
  app.post('/campgrounds', (req, res) => {
    Campground.create(req.body).then((campground) => {
      res.redirect('/campgrounds/' + campground._id) // Redirect to reviews/:id
    }).catch((err) => {
      console.log(err.message)
    })
  })

//SHOW

app.get('/campgrounds/:id', (req, res) => {
  Campground.findById(req.params.id).then((campground) => {
    res.render('campgrounds-show', { campground: campground })
  }).catch((err) => {
    console.log(err.message);
  })
})

//EDIT
app.get('/campgrounds/:id/edit',  (req, res) => {
  Campground.findById(req.params.id, (err, campground) => {
    res.render(' campgrounds-edit', { campground: campground });
  })
})

//NEW
  app.get('/campgrounds/new', (req, res) => {
    res.render('new');
  })
//UPDATE
  app.put('/campgrounds/:id', (req, res) => {
    Review.findByIdAndUpdate(req.params.id, req.body).then((campground) => {
      res.redirect('/campgrounds/' + campground._id)
    }).catch((err) => {
      console.log(err.message)
    })
})


//DELETE
  app.delete('/campgrounds/:id', (req, res) => {
    console.log("DELETE review")
    Campground.findByIdAndRemove(req.params.id).then((campground) => {
      res.redirect('/');
    }).catch((err) => {
      console.log(err.message);
    })
  })


}
