'use strict';

angular.module('superheroSelector', ['ui.bootstrap'])

.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
})

.config(function ($locationProvider) {
    $locationProvider.html5Mode(true);
})

.controller('selectTypeCtrl', function ($scope, $http) {

    $http.post('/ajax/availableTypes')
        .success(function (data) {
            $scope.heroes = data.heroes;
            $scope.villains = data.villains;
        });
})

.controller('selectCharacterCtrl', function ($scope, $http, $location, $modal) {

    $http.post('/ajax/characters', { 'characterType': $location.search()['type'] })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });

    $scope.preview = function (character) {
        var modalInstance = $modal.open({
            templateUrl: 'templates/preview.html',
            controller: 'previewCtrl',
            size: 'lg',
            resolve: {
                character: function () {
                    return character;
                },
                userId: function () {
                    return $location.search()['id']
                }
            }
        });
    };
})

.controller('previewCtrl', function ($scope, $modalInstance, $http, character, userId) {

    $scope.character = character;
    $scope.userId = userId;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.confirm = function () {
        $http.post('/ajax/select', { 'userId': $scope.userId, 'characterId': $scope.character.id })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    };

});