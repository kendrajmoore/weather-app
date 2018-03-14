const mongoose = require('mongoose');
const    Schema = mongoose.Schema;


const userSchema = new mongoose.Schema({
  email: String,
  name: String
});


module.exports = mongoose.model('User', userSchema);
