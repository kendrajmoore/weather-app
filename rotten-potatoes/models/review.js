const mongoose = require('mongoose');
const    Schema = mongoose.Schema;

var ReviewSchema = new Schema({
    title             : { type: String, required: true }
  , movieTitle      : { type: String, required: true }
  , description     : { type: String, required: true }
});



module.exports = mongoose.model('Review', ReviewSchema);
