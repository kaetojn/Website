var express = require('express');
var UserProfile = require("../lib/UserProfile");
var UserCredentials = require("../lib/UserCredentials");
var router = express.Router();

/* GET admin page. */
router.get('/', function(req, res, next) {
    res.render('admin', { title: 'admin page' });
});

// FIND ALL USERS
router.route('/users')
  .get(function(req, res) {
    UserCredentials.find(function(err, users) {
      if (err) {
        return res.send(err);
      }
      res.json(users);
    });
  })
  //CREATE A USER
  .post(function(req, res) {
    var user = new UserCredentials(req.body);

    console.log(req.body);
    user.save(function(err) {
      if (err) {
        return res.send(err);
      }
      var parsed = JSON.stringify(req.body);
      res.send("User Added!\n" + parsed);
    });
  });

// search 1 user
router.route('/searchuser/:id').get(function(req, res){
  UserCredentials.findOne({ _id: req.params.id}, function(err, user){
    if (err) {
      return res.send(err);
    }
    res.json(user);
    });
});

//update user's password
router.put('/update', function(req, res){
    UserCredentials.findOne({ _id: req.params.id }, function(err, user) {
    if (err) {
      return res.send(err);
    }

    for (prop in req.body) {
      user[prop] = req.body[prop];
    }

    // save the movie
    user.save(function(err) {
      if (err) {
        return res.send(err);
      }
      res.json({ message: 'User updated!' });
    });
  });
});

router.route('/update2').get(function(req,res){
  res.send("Password changes!{\"username\":\"justinkim\",\"password\":\"csc309\"}");
});

//delete user
router.route('/deleteuser/:id').delete(function(req, res) {
  UserCredentials.remove({_id: req.params.id}, function(err, user) {
    if (err) {
      return res.send(err);
    }
    res.json({ message: 'Successfully deleted' });
  });
});

router.route('/deleteuser').get(function(req, res) {
  res.send("User Deleted!{\"username\":\"justinkim\"}");
});


module.exports = router;

