var mongoose = require("mongoose");

//Schema and Database for Profile Page
var UserProfile = mongoose.model("userprofile", new mongoose.Schema({
    username: {type: String, required: true, unique: true},
    firstname: {type: String, required: true},
    lastname: {type: String, required: true},
    specialties: {type: String, required: true},
    description: {type: String, required: true},
    age: {type: String, required: true},
    location: {type: String, required: true},
    education: {type: String, required: true},
    degree: {type: String, required: true},
    reviews: [{stars: Number, username: String, body: String}],
    email: String
}));

module.exports = UserProfile;
