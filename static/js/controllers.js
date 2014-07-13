'use strict';

angular.module('superheroSelector', ['ui.bootstrap'])

.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
})

.controller('selectTypeCtrl', function ($scope, $http) {

    $scope.test = 'hello';

    $http.post('/ajax/availableTypes')
        .success(function (data) {
            $scope.heroes = data.heroes;
            $scope.villains = data.villains;
        });
});