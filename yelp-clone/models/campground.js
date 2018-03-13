const mongoose = require('mongoose');
const    Schema = mongoose.Schema;


const CampgroundSchema = new mongoose.Schema({
  name: String,
  image: String
});


module.exports = mongoose.model('Campground', CampgroundSchema);
