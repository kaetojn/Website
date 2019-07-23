var mongoose = require('mongoose');
//Schema and Database for Admin
var userSchema = new mongoose.Schema({
    username: {type: String, required: true, unique: true}
});

var User = mongoose.model('myuser', userSchema);
module.exports = User;