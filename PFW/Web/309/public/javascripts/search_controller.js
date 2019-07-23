var searchApp = angular.module("searchApp", []);

searchApp.controller('searchctrl', ['$scope', '$http', function($scope, $http) {
    angular.element(document).ready(function () {
        $http.get('/SearchResults')
            .then(function(response){


                $scope.findMatching = function() {
                    var all_users = response.data; // gets all the users in the database
                    var matching_users = [];        // will store only matching users

                    angular.forEach(all_users, function(value, key){
                        var searchbar = $scope.text;
                        console.log(searchbar);

                        searchbar = searchbar.toLowerCase();

                        if (value.firstname.toLowerCase().indexOf(searchbar) > -1 && searchbar.length > 0) {
                            matching_users.push(value);
                        }
                        else if (value.lastname.toLowerCase().indexOf(searchbar) > -1 && searchbar.length > 0) {
                            matching_users.push(value);
                        }
                        else if (value.specialties.toLowerCase().indexOf(searchbar) > -1 && searchbar.length > 1) {
                            matching_users.push(value);
                        }
                        else if (value.education.toLowerCase().indexOf(searchbar) > -1 && searchbar.length > 2) {
                            matching_users.push(value);
                        }
                    });
                    $scope.results = matching_users;
                };
            });
    });
}]);