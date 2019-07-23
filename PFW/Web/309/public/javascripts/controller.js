var mainApp = angular.module("mainApp", ["ngSanitize"]);
var reviews
// studentController defined as a JavaScript object with $scope as argument.
         
mainApp.controller('profileController', ['$scope', '$http', function($scope, $http) {
   angular.element(document).ready(function () {
      $http.get('/UserProfile')
      .then(function(response){
         var user = response.data;
         $scope.name = (user.firstname + " " + user.lastname).toUpperCase();
         $scope.description = user.description;
         $scope.age = user.age;
         $scope.location = user.location;
         $scope.education = user.education;
         $scope.degree = user.degree;
         $scope.specialties = user.specialties;

         $scope.reviews = "<h1>Reviews</h1><br /><br />"
         for (var i = 0; i < user.reviews.length; i++) {
             $scope.reviews += '<div class="review">';
             $scope.reviews += '<h3>' + user.reviews[i].username + '</h3>';
             $scope.reviews += '<p><strong>'+ user.reviews[i].stars + 
                '/5</strong> ' + user.reviews[i].body + '</p>';
             $scope.reviews += '</div>';
         }
      });
   });
}]);
